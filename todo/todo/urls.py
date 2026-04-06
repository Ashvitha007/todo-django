from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.login),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginn, name='login'),
    path('todo/', views.todo, name='todo'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('logout/', views.logoutt, name='logout'),
    path('edit/<int:id>/', views.edit, name='edit'),
]
 