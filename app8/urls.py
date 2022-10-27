from django.urls import path
from . import views

app_name='app8'

urlpatterns=[
   path('',views.index,name='index'),
   path('show_form',views.show_form,name='show_form'),
   path('login',views.login,name='login'),
   path('home/<int:id>',views.home,name='home'),
   path('update/<int:id>',views.update,name='update'),
   path('display_users',views.display_users,name='display_users'),
   path('delete/<int:id>',views.delete,name='delete'),
   path('change_password/<int:id>',views.change_password,name='change_password'),
   path('logout',views.logout,name='logout'),
   path('image/',views.image,name='image'),
]