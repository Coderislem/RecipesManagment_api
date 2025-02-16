from django.db import models
from django.contrib.auth.models import  User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Cuisine_Type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Meal_Type(models.TextChoices):
    BREAKFAST = 'B','Breakfast'
    LUNCH = 'L','Lunch'
    DINNER = 'D','Dinner'
    SNACK = 'S','Snack'

    def __str__(self):
        return self.value

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cuisine_type = models.ForeignKey(Cuisine_Type, on_delete=models.SET_NULL, null=True,blank=True)
    ingredients = models.ManyToManyField(Ingredient)
    meal_type = models.CharField(max_length=1, choices=Meal_Type.choices)
    preparation_time = models.PositiveIntegerField(
        help_text="Enter time in minutes",
        validators=[MinValueValidator(1), MaxValueValidator(1440)]
        )
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)