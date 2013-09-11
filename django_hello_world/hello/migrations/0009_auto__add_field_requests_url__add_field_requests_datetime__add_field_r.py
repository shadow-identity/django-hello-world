# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Requests.url'
        db.add_column(u'hello_requests', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Requests.datetime'
        db.add_column(u'hello_requests', 'datetime',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 9, 11, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Requests.method'
        db.add_column(u'hello_requests', 'method',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'Requests.user'
        db.add_column(u'hello_requests', 'user',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Requests.url'
        db.delete_column(u'hello_requests', 'url')

        # Deleting field 'Requests.datetime'
        db.delete_column(u'hello_requests', 'datetime')

        # Deleting field 'Requests.method'
        db.delete_column(u'hello_requests', 'method')

        # Deleting field 'Requests.user'
        db.delete_column(u'hello_requests', 'user')


    models = {
        u'hello.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "'mail@example.com'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'default': "'jabber@example.com'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "'john_smith'", 'max_length': '100'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'hello.requests': {
            'Meta': {'ordering': "['id']", 'object_name': 'Requests'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'req': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'hello.state': {
            'Meta': {'object_name': 'State'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'record_id': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['hello']