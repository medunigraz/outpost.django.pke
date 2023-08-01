import logging
from pathlib import Path

from braces.views import LoginRequiredMixin
from django.core.cache import cache
from django.http import (
    FileResponse,
    HttpResponse,
)
from django.utils.decorators import method_decorator
from django.views.generic import View
from outpost.django.base.mixins import HttpBasicAuthMixin

from .conf import settings
from .tasks import XMLTask

logger = logging.getLogger(__name__)


class XMLView(HttpBasicAuthMixin, LoginRequiredMixin, View):
    def get(self, request):
        response = HttpResponse()
        response["Content-Type"] = "application/xml"
        response["X-Path"] = __file__
        xml = cache.get(settings.PKE_CACHE_KEY, None)
        if not xml:
            xml = XMLTask().run()
        response.write(xml)
        return response


class SchemaView(View):
    def get(self, request):
        schema = Path(__file__).with_name("schema.xsd")
        response = FileResponse(schema.open("rb"))
        response["Content-Type"] = "application/xml"
        response["Cache-Control"] = "public,max-age=604800"
        return response
