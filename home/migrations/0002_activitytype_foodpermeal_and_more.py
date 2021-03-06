# Generated by Django 4.0.4 on 2022-04-18 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('calories_burned_per_kg', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodPerMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField()),
            ],
        ),
        migrations.RenameField(
            model_name='food',
            old_name='categorie',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6),
        ),
        migrations.DeleteModel(
            name='Food_per_meal',
        ),
        migrations.AddField(
            model_name='foodpermeal',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.food'),
        ),
        migrations.AddField(
            model_name='foodpermeal',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.meal'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.activitytype'),
        ),
        migrations.DeleteModel(
            name='Activity_type',
        ),
    ]
