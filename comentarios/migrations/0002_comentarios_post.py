# Generated by Django 2.2.4 on 2019-08-07 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post', verbose_name='post'),
        ),
    ]
