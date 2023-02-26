from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('list_emp', views.list_emp, name='list_emp'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('remove_emp', views.remove_emp, name='remove_emp'),
    path('fetch_emp', views.fetch_emp, name='fetch_emp'),
    path('select_update_emp', views.select_update_emp, name='select_update_emp'),
    path('update_emp/<str:id>', views.update_emp, name='update_emp'),
]
