# Generated by Django 4.2.5 on 2023-09-20 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='matiere',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matieres', to='cours.niveaux'),
        ),
    ]