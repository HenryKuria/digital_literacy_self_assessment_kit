# Generated by Django 3.1.4 on 2021-01-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kit', '0005_auto_20210106_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer_type',
            field=models.CharField(choices=[('RADIO', 'RADIO'), ('SELECT', 'SELECT')], default='RADIO', max_length=10),
        ),
    ]
