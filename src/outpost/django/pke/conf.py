import os

from appconf import AppConf
from django.conf import settings


class PKEAppConf(AppConf):
    CACHE_KEY = 'pke'
    FOREIGN_KEY = 'id'

    class Meta:
        prefix = 'pke'
