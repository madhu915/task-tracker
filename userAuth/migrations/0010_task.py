# Generated by Django 4.0.6 on 2023-03-21 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0009_alter_intern_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='NA', max_length=255)),
                ('assigned_date', models.DateField(auto_now_add=True)),
                ('started_date', models.DateField(blank=True, null=True)),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('completion_status', models.BooleanField(default=False)),
                ('progress_status', models.CharField(max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('internid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userAuth.intern')),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tasks',
            },
        ),
    ]
