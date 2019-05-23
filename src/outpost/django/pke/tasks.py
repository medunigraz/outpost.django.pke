import logging
from collections import namedtuple
from datetime import timedelta

from celery.task import PeriodicTask
from django.core.cache import cache
from django.db import connection

from . import schema
from .conf import settings

logger = logging.getLogger(__name__)


def fetchdict(cursor):
    '''
    Return all rows from a cursor as a dict.
    '''
    columns = [col.name for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class XMLTask(PeriodicTask):
    run_every = timedelta(minutes=30)
    ignore_result = True

    def event(self, data):
        key = settings.PKE_FOREIGN_KEY
        event = schema.TerminType()
        for name in data.keys():
            if hasattr(event, name.upper()):
                setattr(event, name.upper(), data.get(name))
        with connection.cursor() as cursor:
            cursor.execute(
                f'SELECT * FROM "pke"."vortragende" WHERE {key.upper()} = %s',
                [
                    data.get(key)
                ]
            )
            for row in fetchdict(cursor):
                event.VORTRAGENDER.append(self.lecturer(row))
        return event

    def lecturer(self, data):
        lecturer = schema.VortragenderType()
        for name in data.keys():
            if hasattr(lecturer, name.upper()):
                setattr(lecturer, name.upper(), data.get(name))
        return lecturer

    def run(self, **kwargs):
        logging.info('Generating new XML body')
        root = schema.MEDIEN_MON_TERMINE()
        with connection.cursor() as cursor:
            cursor.execute(
                '''
                SELECT * FROM "pke"."anzeigen" ORDER BY ZEIT_VON, ZEIT_BIS
                '''
            )
            for row in fetchdict(cursor):
                root.TERMIN.append(self.event(row))
        body = root.toxml()
        cache.set(settings.PKE_CACHE_KEY, body)
        logging.info(f'Finished generating new XML body with size {len(body)}')
        return body
