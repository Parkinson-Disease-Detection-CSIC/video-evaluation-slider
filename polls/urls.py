from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/general/details
    path('<int:sub_num>/<str:input_type>/details', views.details, name='details'),
    # ex: /polls/5/general/evaluate/
    path('<int:sub_num>/<str:input_type>/evaluate', views.evaluate, name='evaluate'),
]
