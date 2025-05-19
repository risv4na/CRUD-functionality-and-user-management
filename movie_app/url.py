
from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('create',create, name='create'),
    path('edit/<pk>',edit, name='edit'),
    path('delete/<pk>', delete, name='delete'),
    path('add_censor_info/<pk>', add_censor_info, name='add_censor_info'),
    path('add_director_name/', add_director_name, name='add_director_name'),
    path('add_actor_name,', add_actor_name, name="add_actor_name"),
    path('', sign_up, name='sign_up'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout_view'),
]

