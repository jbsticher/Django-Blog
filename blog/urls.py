from .views import HomePageView, BlogDetailView
from django.urls import path

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),

]
