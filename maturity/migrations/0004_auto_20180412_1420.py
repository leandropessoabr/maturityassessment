# Generated by Django 2.0.4 on 2018-04-12 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maturity', '0003_auto_20180412_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assessment',
            old_name='Assessment Date',
            new_name='assessment_date',
        ),
    ]
