# Generated by Django 3.1.3 on 2020-11-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='college_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='degree',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='designation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='mobile',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='total_experience',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ResumeDetail',
        ),
    ]
