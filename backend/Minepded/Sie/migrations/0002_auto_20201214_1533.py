# Generated by Django 3.1.4 on 2020-12-14 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_projet', models.CharField(max_length=200)),
                ('promoteur', models.CharField(max_length=200)),
                ('intitule', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RenameField(
            model_name='thematique',
            old_name='name',
            new_name='intitule',
        ),
    ]
