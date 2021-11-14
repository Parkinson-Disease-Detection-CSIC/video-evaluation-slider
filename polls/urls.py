from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5
    path('<int:sub_num>/', views.backwards_redirect, name='redirect'),
    # ex: /polls/5/details
    path('<int:sub_num>/details', views.backwards_redirect, name='redirect'),
    # ex: /polls/5/general
    path('<int:sub_num>/general', views.backwards_redirect, name='redirect'),
    # ex: /polls/5/symptoms
    path('<int:sub_num>/symptoms', views.backwards_redirect, name='redirect'),
    # ex: /polls/5/general/details
    path('<int:sub_num>/<str:input_type>/details', views.details, name='details'),
    # ex: /polls/5/general/evaluate/
    path('<int:sub_num>/<str:input_type>/evaluate', views.evaluate, name='evaluate'),
]
