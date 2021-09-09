from django.urls import path
from .views import *
urlpatterns = [
    path('', home , name="home"),
    path('blog/<int:id>/<str:slug>/', blog , name="blog"),
    path('category/<int:id>/<str:slug>/', category , name="category"),
    path('tag/<str:slug>/', tags , name="tags"),
]
