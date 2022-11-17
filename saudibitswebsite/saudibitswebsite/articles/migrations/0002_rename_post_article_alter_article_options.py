# Generated by Django 4.1.3 on 2022-11-06 08:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Article',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_on']},
        ),
    ]
