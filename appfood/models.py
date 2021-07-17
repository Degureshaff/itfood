from django.db import models
from django.db.models.deletion import CASCADE


class FoodCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='food_category/images')
    desc = models.TextField()
    class Meta:
        db_table = 'foods_categories'
    def __str__(self):
        return self.name

# - список блюд
#  - название
#  - картинка
#  - описание
#  - себестоимость
#  - продажная цена
#  - надбавка (в процентах)

class Food(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='foods/images')
    desc = models.TextField()
    food_category = models.ForeignKey(
        FoodCategory,
        db_column ='food_category_id',
        on_delete = CASCADE
    )
    food_cost = models.DecimalField(max_digits=9, decimal_places=4)
    sale_prise = models.DecimalField(max_digits=9, decimal_places=4)
    markup = models.FloatField()
    class Meta:
        db_table = 'foods'

    def __str__(self):
        return self.name

# - заказы
#  - имя заказчика
#  - телефон заказчика
#  - адрес заказчика
#  - местоположение (долгота, ширина)
#  - дата создания
#  - статус обработки
#  - сумма заказа



class Order(models.Model):
    client_name = models.CharField(max_length=255)
    client_fhone = models.CharField(max_length=255) 
    client_address = models.CharField(max_length=255) 
    client_location = models.CharField(max_length=255) 
    created_dt = models.DateTimeField()
    order_status = models.CharField(max_length=255)
    order_sum = models.DecimalField(max_digits=20, decimal_places=4)
    class Meta:
        db_table = 'orders'
    
    def __str__(self):
        return self.id+ ' -> ' +self.client_name

# - заказ_описание
#  - id заказ
#  - id блюда
#  - количество блюд

class OrderDescription(models.Model):
    order = models.ForeignKey(
        Order, 
        db_column='order_id', 
        on_delete=CASCADE
    )
    food = models.ForeignKey(
        Food, 
        db_column='food_id', 
        on_delete=CASCADE
    )
    amount = models.IntegerField()
    class Meta:
        db_table = 'orders_description'