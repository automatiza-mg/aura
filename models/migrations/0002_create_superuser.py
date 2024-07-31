# your_app/migrations/000X_create_superuser.py

import os
# from dotenv import load_dotenv
from django.db import migrations
from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    User = get_user_model()
    # load_dotenv()
    username = 'admin' #os.environ.get('ADMIN_USERNAME')
    email = 'admin@example.com' # os.environ.get('ADMIN_EMAIL')
    password = '123456789SenhaForte'  # os.environ.get('ADMIN_PWD')
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
