from django.urls import path
from .views import BlogView, BlogDetailView, BlogCreateView

urlpatterns = [
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogView.as_view(), name='home'),
]
