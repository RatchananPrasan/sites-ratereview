from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.conf import settings
from .forms import RecipeInitialForm, ImageUploadForm, CategoryForm, TextForm, BaseTextFormSet, BaseCategoryFormSet, RatingForm
from .models import Recipe, Category, Images, FollowList, SaveList, Rating
from accounts.models import User
import random
import base64

# Create your views here.
def recipe_search(request):
    print(request.GET)
    return render(request, 'recipes/search.html')


def recipe_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    category_list = Category.objects.filter(recipe=recipe)
    all_rating = Rating.objects.filter(recipe=recipe)
    form = RatingForm()
    stars = recipe.get_rating_percent()
    
    if not request.user.is_authenticated:
        is_follow = False
        is_saved = False
        is_rate = False
    else:
        try:
            f = FollowList.objects.get(following=recipe.recipe_by, followed_by=request.user)
            is_follow = True
        except FollowList.DoesNotExist:
            is_follow = False
            
        try:
            s = SaveList.objects.get(recipe=recipe, saved_by=request.user)
            is_saved = True
        except SaveList.DoesNotExist:
            is_saved = False

        try:
            r = Rating.objects.get(recipe=recipe, recipe_rate_by=request.user)
            is_rate = r
        except Rating.DoesNotExist:
            is_rate = False
    
    return render(request, 'recipes/view.html', {'recipe':recipe, 'is_follow':is_follow, 'is_saved':is_saved, 'category_list':category_list,
                                                 'stars':stars, 'form':form, 'is_rate':is_rate, 'all_rating':all_rating})


@login_required
def recipe_follow(request, following, recipe_id):
    if request.method == "POST":
        follow_user = get_object_or_404(User, pk=following)
        if request.user != follow_user:
            FollowList.objects.create(following=follow_user, followed_by=request.user)
            
    return redirect('recipes:view', recipe_id)


@login_required
def recipe_unfollow(request, following, recipe_id):
    if request.method == "POST":
        follow_user = get_object_or_404(User, pk=following)
        if request.user != follow_user:
            f = FollowList.objects.get(following=follow_user, followed_by=request.user)
            f.delete()
    return redirect('recipes:view', recipe_id)


@login_required
def recipe_favourite(request, recipe_id):
    if request.method == "POST":
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        if request.user != recipe.recipe_by:
            SaveList.objects.create(recipe=recipe, saved_by=request.user)
            
    return redirect('recipes:view', recipe_id)


@login_required
def recipe_unfavourite(request, recipe_id):
    if request.method == "POST":
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        if request.user != recipe.recipe_by:
            s = get_object_or_404(SaveList, recipe=recipe, saved_by=request.user)
            s.delete()
            
    return redirect('recipes:view', recipe_id)


@login_required
def recipe_rate(request, recipe_id):
    if request.method == "POST":
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        if request.user != recipe.recipe_by:
            form = RatingForm(request.POST)
            if form.is_valid():
                rate = form.cleaned_data['rate']
                description = form.cleaned_data['description']
                Rating.objects.create(recipe=recipe, rate=rate, description=description, recipe_rate_by=request.user)

    return redirect('recipes:view', recipe_id)

@login_required
def recipe_create(request):
    ImageFormSet = formset_factory(ImageUploadForm)
    CategoryFormSet = formset_factory(CategoryForm, formset=BaseCategoryFormSet)
    TextFormSet = formset_factory(TextForm, formset=BaseTextFormSet)
    if request.method == "POST":
        recipe_initial_form = RecipeInitialForm(request.POST, prefix='recipe_initial')
        cover_image_form = ImageUploadForm(request.POST, request.FILES, prefix='cover_image')
        image_formset = ImageFormSet(request.POST, request.FILES, prefix='more_image')
        category_form_set = CategoryFormSet(request.POST, prefix='category')
        directions_form_set = TextFormSet(request.POST, prefix='directions')
        ingredients_form_set = TextFormSet(request.POST, prefix='ingredients')
        
        if all([recipe_initial_form.is_valid(),
                cover_image_form.is_valid(),
                image_formset.is_valid(),
                category_form_set.is_valid(),
                directions_form_set.is_valid(),
                ingredients_form_set.is_valid(),
               ]):
            title = recipe_initial_form.cleaned_data['title']
            description = recipe_initial_form.cleaned_data['description']
            calories = recipe_initial_form.cleaned_data['calories']
            prep_time = recipe_initial_form.cleaned_data['prep_time']
            serving = recipe_initial_form.cleaned_data['serving']
            
            directions_list = []
            for form in directions_form_set:
                if form.cleaned_data:
                    directions_list.append(form.cleaned_data['text'])
                    
            directions = Recipe.SPLITTER.join(directions_list)
            
            ingredients_list = []
            for form in ingredients_form_set:
                if form.cleaned_data:
                    ingredients_list.append(form.cleaned_data['text'])
                    
            ingredients = Recipe.SPLITTER.join(ingredients_list)
            
            r = Recipe.objects.create(title=title, description=description, calories=calories, prep_time=prep_time, serving=serving, ingredients=ingredients, directions=directions, recipe_by=request.user)
            
            catlist = []
            for form in category_form_set:
                if form.cleaned_data:
                    cat = form.cleaned_data['title']
                    if cat not in catlist:
                        catlist.append(cat)
                        Category.objects.create(title=cat, recipe=r)
            
            if cover_image_form.cleaned_data['image']:
                img_data64 = request.POST['cover_image_64'][23:]
                img_url = '\\media\\recipes\\cover_image\\' + title + '_' + str(random.randint(1,1000000)) + '.jpg'
                file_name = settings.MEDIA_ROOT + img_url
                with open(file_name, 'wb') as fh:
                    fh.write(base64.b64decode(img_data64))
                    r.cover_image = img_url
                    r.save()

            for form in image_formset:
                if form.cleaned_data:
                    Images.objects.create(image=form.cleaned_data['image'], recipe=r)
                    
            return redirect('recipes:view', r.id)
    else:
        recipe_initial_form = RecipeInitialForm(prefix='recipe_initial')
        cover_image_form = ImageUploadForm(prefix='cover_image')
        image_formset = ImageFormSet(prefix='more_image')
        category_form_set = CategoryFormSet(prefix='category')
        directions_form_set = TextFormSet(prefix='directions')
        ingredients_form_set = TextFormSet(prefix='ingredients')
    
    return render(request, 'recipes/create.html', {'recipe_initial_form':recipe_initial_form,
                                                   'cover_image_form':cover_image_form,
                                                   'image_formset':image_formset,
                                                   'category_form_set':category_form_set,
                                                   'directions_form_set':directions_form_set,
                                                   'ingredients_form_set':ingredients_form_set,
                                                  })
