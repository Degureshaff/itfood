from django.contrib import admin
from .models import FoodCategory,Food,Order,OrderDescription

admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(OrderDescription)


