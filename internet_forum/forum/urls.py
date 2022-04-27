from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('new_thread/', views.new_thread, name='new_thread'),
    path('<int:thread_id>/new_post/', views.new_post, name='new_post'),
]
