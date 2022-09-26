# Generated by Django 4.1.1 on 2022-09-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_feedback2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback2',
        ),
        migrations.AddField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='textarea',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
