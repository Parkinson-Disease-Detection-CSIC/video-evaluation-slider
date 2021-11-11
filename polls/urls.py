from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/results/
    path('results/', views.results, name='results'),
    # ex: /polls/5/general
    path('<int:sub_num>/general', views.general, name='general'),
    # ex: /polls/5/symptoms
    path('<int:sub_num>/symptoms', views.symptoms, name='symptoms'),
    # ex: /polls/5/evaluate/
    path('<int:sub_num>/evaluate/', views.evaluate, name='evaluate'),
]
