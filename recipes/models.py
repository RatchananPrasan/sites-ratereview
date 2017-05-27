from django.db import models
from django.utils import timezone
from django.db.models import Avg
from accounts.models import User

# Create your models here.
class Recipe(models.Model):
    SPLITTER = '----------'
    pub_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    calories = models.PositiveIntegerField()
    prep_time = models.PositiveIntegerField()
    serving = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='media/recipes/cover_image',
                                    default='media/recipes/cover_image/default.jpg')
    
    recipe_by = models.ForeignKey(User, 
                                  on_delete=models.CASCADE,
                                  related_name = 'recipe_by')
    
    def get_rating(self):
        rating = Rating.objects.filter(recipe_id=self.id).aggregate(Avg('rate'))
        rate = rating['rate__avg']
        if rate == None:
            rate = 0
        return rate
    
    
    def get_image(self):
        images = Images.objects.filter(recipe_id=self.id)
        return images
    
    
    def get_ingredients_list(self):
        return self.ingredients.split(Recipe.SPLITTER)
    
    
    def get_directions_list(self):
        return self.directions.split(Recipe.SPLITTER)
    
    
    def get_all_rating(self):
        rating = Rating.objects.filter(recipe_id=self.id)
        return rating
    
    
    def get_rating_percent(self):
        total_rating = Rating.objects.filter(recipe_id=self.id).count()
        if total_rating == 0:
            return [0, 0, 0, 0, 0]
        
        result = []
        
        excellent_count = Rating.objects.filter(recipe_id=self.id, rate=Rating.EXCELLENT).count()
        very_good_count = Rating.objects.filter(recipe_id=self.id, rate=Rating.VERY_GOOD).count()
        good_count = Rating.objects.filter(recipe_id=self.id, rate=Rating.GOOD).count()
        fair_count = Rating.objects.filter(recipe_id=self.id, rate=Rating.FAIR).count()
        poor_count = Rating.objects.filter(recipe_id=self.id, rate=Rating.POOR).count()
        
        result.append((excellent_count / total_rating) * 100)
        result.append((very_good_count / total_rating) * 100)
        result.append((good_count / total_rating) * 100)
        result.append((fair_count / total_rating) * 100)
        result.append((poor_count / total_rating) * 100)
        
        return result
    
    
class Category(models.Model):
    SNACKS = 'Sn'
    BREAKFAST = 'Br'
    DESSERT = 'De'
    DINNER = 'Di'
    DRINKS = 'Dr'
    HEALTHY = 'He'
    LUNCH = 'Lu'
    SEAFOOD = 'Se'
    
    cat_choice = (
        (SNACKS, 'Snacks'),
        (BREAKFAST, 'Breakfast'),
        (DESSERT, 'Dessert'),
        (DINNER, 'Dinner'),
        (DRINKS, 'Drinks'),
        (HEALTHY, 'Healthy'),
        (LUNCH, 'Lunch'),
        (SEAFOOD, 'Seafood'),
    )
    
    title = models.CharField(max_length=5, choices=cat_choice)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    def __str__(self):
        for i in Category.cat_choice:
            if i[0] == self.title:
                return i[1]
    
    
class Rating(models.Model):
    POOR = 1
    FAIR = 2
    GOOD = 3
    VERY_GOOD = 4
    EXCELLENT = 5
    rate_choice = (
        (POOR, 'Poor'),
        (FAIR, 'Fair'),
        (GOOD, 'Good'),
        (VERY_GOOD, 'Very Good'),
        (EXCELLENT, 'Excellent'),
    )
    
    recipe = models.ForeignKey(Recipe, 
                               on_delete=models.CASCADE)
    rate = models.IntegerField(choices=rate_choice)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    recipe_rate_by = models.ForeignKey(User,
                                       on_delete=models.CASCADE,
                                       related_name='recipe_rate_by')
    
    class Meta:
        ordering = ['-pub_date']
    
    
class Images(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='media/recipes/images') 
    
    
class FollowList(models.Model):
    following = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='following')
    
    followed_by = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name='followed_by')
    
    
class SaveList(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE)
    
    saved_by = models.ForeignKey(User,
                                 on_delete=models.CASCADE)