#!/bin/bash
name=`date +%Y-%m-%d`
python manage.py show_models_objects 2> $name.dat