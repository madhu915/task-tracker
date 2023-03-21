# Generated by Django 4.0.6 on 2023-03-21 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0010_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAuth.task')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
