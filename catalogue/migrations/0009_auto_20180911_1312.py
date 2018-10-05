# Generated by Django 2.1 on 2018-09-11 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_piece_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piece',
            name='feature',
        ),
        migrations.AddField(
            model_name='piece',
            name='feature',
            field=models.CharField(blank=True, choices=[('sop', 'soprano'), ('crn', 'cornet'), ('flg', 'flugel horn'), ('tnr', 'tenor horn'), ('brt', 'baritone'), ('eu', 'euphonium'), ('tbn', 'trombone'), ('btb', 'bass trombone'), ('efb', 'e-flat bass'), ('bfb', 'b-flat bass'), ('kit', 'drum kit'), ('tmp', 'timpani')], help_text='Select solo instrument', max_length=3),
        ),
    ]