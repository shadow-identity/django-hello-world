# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contact.contacts'
        db.delete_column('hello_contact', 'contacts')

        # Adding field 'Contact.email'
        db.add_column('hello_contact', 'email',
                      self.gf('django.db.models.fields.CharField')(default='mail@example.com', max_length=100),
                      keep_default=False)

        # Adding field 'Contact.skype'
        db.add_column('hello_contact', 'skype',
                      self.gf('django.db.models.fields.CharField')(default='john_smith', max_length=100),
                      keep_default=False)

        # Adding field 'Contact.jabber'
        db.add_column('hello_contact', 'jabber',
                      self.gf('django.db.models.fields.CharField')(default='jabber@example.com', max_length=100),
                      keep_default=False)

        # Adding field 'Contact.other_contacts'
        db.add_column('hello_contact', 'other_contacts',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Contact.contacts'
        raise RuntimeError("Cannot reverse this migration. 'Contact.contacts' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Contact.contacts'
        db.add_column('hello_contact', 'contacts',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)

        # Deleting field 'Contact.email'
        db.delete_column('hello_contact', 'email')

        # Deleting field 'Contact.skype'
        db.delete_column('hello_contact', 'skype')

        # Deleting field 'Contact.jabber'
        db.delete_column('hello_contact', 'jabber')

        # Deleting field 'Contact.other_contacts'
        db.delete_column('hello_contact', 'other_contacts')


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
        }
    }

    complete_apps = ['hello']