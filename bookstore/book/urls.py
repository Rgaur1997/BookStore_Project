from django.urls import path
from . import views

urlpatterns= [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
    path('book', views.BookList.as_view()),
    path('book/<int:pk>/', views.BookDetail.as_view()),
    path('order', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),
]