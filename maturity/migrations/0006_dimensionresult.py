# Generated by Django 2.0.4 on 2018-04-23 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maturity', '0005_assessment_current_assessment_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='DimensionResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maturity.Assessment')),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maturity.Dimension')),
            ],
        ),
    ]
