# Generated by Django 2.1 on 2018-09-04 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20180904_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='composer',
            field=models.ManyToManyField(help_text='Select one or more names', to='catalogue.Person'),
        ),
    ]
