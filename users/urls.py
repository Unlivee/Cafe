from django.urls import path
from .views import RegisterView, LoginView, UserView, Logout

from rest_framework import routers
from .api import TodoViewSet


router = routers.DefaultRouter()
router.register('api/user', TodoViewSet, 'user')

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', Logout.as_view()),
]