# Generated by Django 3.0.6 on 2020-06-01 18:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0009_auto_20200530_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='answerpoint',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='question',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='questioncomment',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='questionpoint',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]