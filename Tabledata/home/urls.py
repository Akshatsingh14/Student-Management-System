from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('2',views.pyspiders, name = 'pyspiders'),
    path('3',views.qspiders, name = 'qspiders'),
    path('4',views.jspiders, name = 'jspiders'),
    path('5',views.prospiders, name = 'prospiders'),
    path('one/<int:pk>', views.sngdetail, name = 'sngdetail'),
    path('two/<int:pk2>', views.update, name = 'update'),
    path('add', views.create, name = 'create'),
]