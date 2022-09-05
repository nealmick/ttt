


from . import views

from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('ttt/move/', views.move , name='move'),
]
