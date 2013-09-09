# -*- coding: utf-8 -*-
from django.db import connection
from django.db.models import get_app, get_models

def db_table_exists(model=None, table=None):
    """ Verify the existence of table by model or by table
    """

    table_name = None
    tables = connection.introspection.table_names()

    if model is not None:
        opts = model._meta
        converter = connection.introspection.table_name_converter
        table_name = converter(opts.db_table) if opts.db_table else converter(opts.auto_created._meta.db_table)
    elif table is not None:
        table_name = table

    if table_name is None:
        raise Exception('You need to specify model or table')

    return table_name in tables

# if db_table_exists(table='docflow_document1'):
#     import docflow.projects.modules_1.signal_events
#     import docflow.projects.modules_1.signal_document
#
# if db_table_exists(get_project_model(1, 'Document')):
#     import docflow.projects.modules_1.signal_events
#     import docflow.projects.modules_1.signal_document﻿

print 'aldskfjlaksdjflksdajf'

app = get_app('hello')
all_exists = True
for model in get_models(app):
    print model, db_table_exists(model)
    all_exists = all_exists and db_table_exists(model)
if all_exists:
    import django_hello_world.hello.signals
