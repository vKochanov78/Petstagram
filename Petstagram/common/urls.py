from django.urls import path
from . import views

urlpatterns =[
    path('', views.home_page, name='home-page'),
    path('like/<int:photo_id>/', views.like_functionality, name='like'),
    path('share/<int:photo_id>/', views.share_functionality, name='share'),
    path('comment/<int:photo_id>/', views.add_comment, name='comment-view')
]