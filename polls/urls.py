from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/results/
    path('results/', views.results, name='results'),
    # ex: /polls/5/
    path('<int:sub_num>/', views.detail, name='detail'),
    # ex: /polls/5/evaluate/
    path('<int:sub_num>/evaluate/', views.evaluate, name='evaluate'),
]
