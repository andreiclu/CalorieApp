# Generated by Django 4.0.4 on 2022-05-10 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_food_calories_food_carbohydrate_food_protein_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitytype',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='lifestyle',
            field=models.CharField(choices=[('lightly_active', 'Lightly active'), ('moderately_active', 'Moderately active'), ('active', 'Active'), ('very_active', 'Very active')], max_length=100),
        ),
    ]
