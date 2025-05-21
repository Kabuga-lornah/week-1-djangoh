from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem
from .forms import FoodItemForm
from django.utils.timezone import localdate

def food_list(request):
    today = localdate()
    foods = FoodItem.objects.filter(date_added=today)
    total_calories = sum(food.calories for food in foods)
    return render(request, 'calorie_tracker/food_list.html', {
        'foods': foods,
        'total_calories': total_calories
    })

def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm()
    return render(request, 'calorie_tracker/add_food.html', {'form': form})

def delete_food(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    food.delete()
    return redirect('food_list')

def reset_calories(request):
    today = localdate()
    FoodItem.objects.filter(date_added=today).delete()
    return redirect('food_list')
