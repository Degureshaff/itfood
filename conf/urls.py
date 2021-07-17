"""itfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appfood import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('log/',views.log),
    path('eda/category/<int:category_id>',views.get_foods_by_category),
    path('eda/detail/<int:food_id>',views.food_detail_view),
    path('eda/card/add/<int:food_id>', views.add_to_card),
    path('eda/card/del/<int:food_id>', views.del_to_card),
    path('eda/card/remove/<int:food_id>', views.remove_to_card),
    path('eda/card/view/',views.card_view),
    path('order/add/', views.order_add),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
