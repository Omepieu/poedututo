# Generated by Django 4.2.5 on 2023-09-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0002_alter_lesson_options_alter_matiere_niveau'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_html', models.TextField(blank=True, max_length=800)),
                ('code_css', models.TextField(blank=True, max_length=800)),
                ('code_js', models.TextField(blank=True, max_length=800)),
            ],
        ),
    ]
