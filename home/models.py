from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Food(models.Model):
    name = models.CharField(max_length=100)
    serving_size = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)
    total_fats = models.FloatField(default=0)
    carbohydrate = models.FloatField(default=0)
    protein = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name}'


_LIFESTYLE_CHOICES = (
    ('lightly_active', 'Lightly active'), ('moderately_active', 'Moderately active'), ('active', 'Active'),
    ('very_active', 'Very active'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(('male', 'Male'), ('female', 'Female')), null=True, blank=True)
    lifestyle = models.CharField(max_length=100, choices=_LIFESTYLE_CHOICES, null=True, blank=True)
    goal_weight = models.FloatField(null=True, blank=True, default=0)
    calorie_goal = models.FloatField(null=True, blank=True, default=0)


class ProfileInfoPerDay(models.Model):
    calories = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fats = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        unique_together = ('profile', 'date')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    title = models.CharField(max_length=128, default="")
    calories = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    proteins = models.FloatField(default=0)
    fats = models.FloatField(default=0)


class FoodPerMeal(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    number = models.FloatField()


class ActivityType(models.Model):
    name = models.CharField(max_length=100)
    calories_burned_per_kg = models.FloatField()


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
