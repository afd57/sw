from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('display/', views.BookListView.as_view(), name='books')
]
