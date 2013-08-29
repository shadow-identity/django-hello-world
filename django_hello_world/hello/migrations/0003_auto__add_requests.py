# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Requests'
        db.create_table('hello_requests', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('req', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('hello', ['Requests'])


    def backwards(self, orm):
        # Deleting model 'Requests'
        db.delete_table('hello_requests')


    models = {
        'hello.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'default': "'mail@example.com'", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'default': "'jabber@example.com'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "'john_smith'", 'max_length': '100'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'hello.requests': {
            'Meta': {'object_name': 'Requests'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'req': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['hello']