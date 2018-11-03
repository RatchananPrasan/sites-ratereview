from rest_framework import serializers
from .models import Recipe, Category, Rating,Images,FollowList,SaveList

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        recipe = Recipe
        category = Category
        rating = Rating
        images = Images
        followList = FollowList
        saveList = SaveList
        fields = '__all__'
    