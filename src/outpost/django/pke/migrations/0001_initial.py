# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-22 09:01
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings


class Migration(migrations.Migration):

    ops = [
        (
        '''
        CREATE SCHEMA IF NOT EXISTS pke;
        ''',
        '''
        DROP SCHEMA IF EXISTS pke;
        ''',
        ),
        (
            '''
            CREATE FOREIGN TABLE "pke"."anzeigen" (
                ID numeric,
                TYP numeric,
                TYP_TXT varchar,
                KENNUNG varchar,
                TITEL varchar,
                DATUM timestamp,
                ZEIT_VON timestamp,
                ZEIT_BIS timestamp,
                GEBAEUDE varchar,
                RAUM varchar,
                RAUM_BEZ varchar,
                TERMINART varchar
            )
            SERVER sqlalchemy OPTIONS (
                tablename 'PKE_ANZEIGEN_V',
                db_url '{}'
            );
            '''.format(settings.MULTICORN.get('campusonline')),
            '''
            DROP FOREIGN TABLE IF EXISTS "pke"."anzeigen";
            ''',
        ),
        (
            '''
            CREATE FOREIGN TABLE "pke"."vortragende" (
                ID numeric,
                NAME varchar,
                TYP varchar
            )
            SERVER sqlalchemy OPTIONS (
                tablename 'PKE_ANZEIGEN_VORTRAGENDE_V',
                db_url '{}'
            );
            '''.format(settings.MULTICORN.get('campusonline')),
            '''
            DROP FOREIGN TABLE IF EXISTS "pke"."vortragende";
            ''',
        ),
    ]

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            [forward for forward, reverse in ops],
            [reverse for forward, reverse in reversed(ops)]
        )
    ]