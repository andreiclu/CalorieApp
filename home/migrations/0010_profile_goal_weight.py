# Generated by Django 4.0.4 on 2022-07-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_profileinfoperday_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='goal_weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]