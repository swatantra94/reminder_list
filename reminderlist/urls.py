from django.urls import path
from reminderlist import views

urlpatterns = [
    path('todo/',views.index,name='index'),
    path('activity/<int:pk>/',views.activity,name='get_activity'),
    path('activity/create/',views.create,name='create_activity'),
    path('activity/delete/<int:pk>/',views.delete,name='delete_activity'),
    path('wall/',views.wall),

]