# Generated by Django 4.2.5 on 2023-09-20 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0003_alter_profil_photo_alter_profil_type_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Code',
        ),
    ]
