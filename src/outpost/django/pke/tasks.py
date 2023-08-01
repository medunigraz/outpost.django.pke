import logging

from celery import shared_task
from django.core.cache import cache
from django.db import connection
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from . import schema
from .conf import settings

logger = logging.getLogger(__name__)


def fetchdict(cursor):
    """
    Return all rows from a cursor as a dict.
    """
    columns = [col.name for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


class PKETasks:
    @shared_task(bind=True, ignore_result=True, name=f"{__name__}.PKE:hydrate")
    def hydrate(task):
        def event(data):
            key = settings.PKE_FOREIGN_KEY
            event = schema.TerminType()
            # kwargs = {k: v for k, v in data.items() if hasattr(event, k.upper())}
            for name in data.keys():
                if hasattr(event, name.lower()):
                    setattr(event, name.lower(), data.get(name))
            with connection.cursor() as cursor:
                cursor.execute(
                    f'SELECT * FROM "pke"."vortragende" WHERE {key.upper()} = %s',
                    [data.get(key)],
                )
                for row in fetchdict(cursor):
                    event.vortragender.append(lecturer(row))
            return event

        def lecturer(data):
            lecturer = schema.VortragenderType()
            for name in data.keys():
                if hasattr(lecturer, name.lower()):
                    setattr(lecturer, name.lower(), data.get(name))
            return lecturer

        logging.info("Generating new XML body")
        root = schema.MedienMonTermine()
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM "pke"."anzeigen" ORDER BY ZEIT_VON, ZEIT_BIS
                """
            )
            for row in fetchdict(cursor):
                root.termin.append(event(row))
        config = SerializerConfig(pretty_print=True)
        serializer = XmlSerializer(config=config)
        body = serializer.render(root, ns_map={None: schema.__NAMESPACE__})
        cache.set(settings.PKE_CACHE_KEY, body)
        logging.info(f"Finished generating new XML body with size {len(body)}")
        return body
