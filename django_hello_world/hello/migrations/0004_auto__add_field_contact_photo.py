# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contact.photo'
        db.add_column('hello_contact', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(default='dummy.jpg', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Contact.photo'
        db.delete_column('hello_contact', 'photo')


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
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "'john_smith'", 'max_length': '100'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'hello.requests': {
            'Meta': {'ordering': "['id']", 'object_name': 'Requests'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'req': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['hello']