# Generated by Django 4.1.2 on 2023-03-24 12:18

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_merge_20230324_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='dateInvested',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2023, 3, 24))]),
        ),
        migrations.DeleteModel(
            name='InvestorIndividual',
        ),
    ]