from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'cafe_core_app'
urlpatterns = [
    path('', views.menu, name='menu'),
    path('menu', views.menu, name='menu'),
    path('meals/<meal_category>', views.meal_category, name='meal_category'),
    path('meal/<int:meal_id>', views.meal, name='meal'),
    path('meal_statistics', views.meal_statistics, name='meal_statistics'),
    path('grafic/<int:meal_id>', views.GraphsViewBar, name='grafic'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
