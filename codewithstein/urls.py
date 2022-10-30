
from django.contrib import admin
from django.urls import path

from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.frontpage, name='frontpage'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),
]
