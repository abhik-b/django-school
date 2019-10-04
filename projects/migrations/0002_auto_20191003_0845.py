# Generated by Django 2.2.6 on 2019-10-03 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classs', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=120)),
                ('subject', models.CharField(max_length=250)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classs.Classs')),
            ],
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
