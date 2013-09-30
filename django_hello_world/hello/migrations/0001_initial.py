# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'hello_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(default='mail@example.com', max_length=100)),
            ('skype', self.gf('django.db.models.fields.CharField')(default='john_smith', max_length=100)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(default='jabber@example.com', max_length=100)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(default='')),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'hello', ['Contact'])

        # Adding model 'Requests'
        db.create_table(u'hello_requests', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('req', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'hello', ['Requests'])

        # Adding model 'State'
        db.create_table(u'hello_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('record_id', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'hello', ['State'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'hello_contact')

        # Deleting model 'Requests'
        db.delete_table(u'hello_requests')

        # Deleting model 'State'
        db.delete_table(u'hello_state')


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