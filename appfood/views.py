from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FoodCategory,Food,Order,OrderDescription

def log(request):
    return render(request, 'login.html')

def home(request):
    # Из базы получаем все категорий еды
    foodCategory = FoodCategory.objects.all()
    foods = Food.objects.all()
    
    # показываем шаблон index.html и передаем ему foodCategories
    return render(request, 'index.html',{
        'foodCategories':foodCategory,
        'foods':foods
    })

# показываем список блюд по категорий
def get_foods_by_category(request,category_id):
    # мы получаем список блюд по категорию
    foods = Food.objects.all().filter(food_category_id = category_id)
    # получаем категорий еды
    category = FoodCategory.objects.get(id=category_id)
    FoodCategories = FoodCategory.objects.all()
    return render(request, 'foods_by_category.html',{
            'foods':foods,
            'category': category,
            'foodCategories': FoodCategories

    })


def food_detail_view(request, food_id):
    # получаем еду по id
    food = Food.objects.get(id = food_id)

    # Из базы получаем все категории еды (нужен для header)
    foodCategories = FoodCategory.objects.all()

    # Рендерим на шаблон food_detail.html
    return render(request,
        'food_detail.html',
        {
            'food': food,
            'foodCategories': foodCategories
        }
    )

# функция обрабатывает на добавление корзину
def add_to_card(request, food_id):
    cards = request.session.get('food_cards', [])
    # временно сохраняем товар в сессию пользователя
    cards.append(food_id)
    request.session['food_cards'] = cards

    # перенаправляем пользователя обратно на свою страницу 
    # после добавление еды на корзину
    prev = request.GET.get('prev')
    return redirect(prev)
# фунция обрабатывает на удаление корзину
def del_to_card(request, food_id):
    cards = request.session.get('food_cards', [])
    # временно сохраняем товар в сессию пользователя
    cards.remove(food_id)
    request.session['food_cards'] = cards

    # перенаправляем пользователя обратно на свою страницу 
    # после добавление еды на корзину
    prev = request.GET.get('prev')
    return redirect(prev)

# удаляем блюдо из корзины 
def remove_to_card(request, food_id):
    cards = request.session.get('food_cards', [])
    # временно сохраняем товар в сессию пользователя
    # удаляем из корзины все оставшие блюдо
    new_cards = []
    for card in cards:
        if card != food_id:
            new_cards.append(card)

    request.session['food_cards'] = new_cards

    # перенаправляем пользователя обратно на свою страницу 
    # после добавление еды на корзину
    prev = request.GET.get('prev')
    return redirect(prev)


# обработчик показа блюд в корзине
def card_view(request):
    foodCategories = FoodCategory.objects.all()
    
    #  id блюд которые находятся в корзине      
    foods_ids = request.session.get('food_cards', [])

    # все блюда и базы по food_ids
    card_foods = Food.objects.filter(id__in = foods_ids)
    for card_food in card_foods:
        card_food.count = foods_ids.count(card_food.id)
        card_food.sum = card_food.count * card_food.sale_prise
    
    return render(request, 
        'card_view.html',
        {
            'foods_ids': foods_ids,
            'card_foods': card_foods,
            'foodCategories':foodCategories            
        }
    )


def order_add(request):
    if request.method == 'POST':
        # id блюд которые находятся в корзине
        foods_ids = request.session.get('foods_cards',[]) 
        if len(foods_ids) == 0:
            messages.error(request, 'ваша корзина пустая',
            extra_tags='danger')
            prev = request.POST.get('prev_url')
            return redirect(prev)
        else:
         # принимаем данные клиента для добавление в базу
            client_name = request.POST.get('client_name')
            client_phone = request.POST.get('client_phone')
            client_address = request.POST.get('client_address')  
       