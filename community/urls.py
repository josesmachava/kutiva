from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('ask', views.ask_question, name='ask_question'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]