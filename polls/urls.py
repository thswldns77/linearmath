from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:exam_id>/', views.detail, name='detail'),
    path('<int:exam_id>/results/', views.results, name='results'),
    path('<int:exam_id>/score/', views.score, name='score'),

    ]  