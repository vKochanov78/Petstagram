from django.urls import path, include

from . import views

urlpatterns = [
    path('add/', views.add_photo, name='add-photo'),
    path('<int:pk>/', views.photo_details_page, name='photo-details-page'),
    path('edit/<int:pk>/', views.photo_edit_page, name='photo-edit-page'),
    path('delete/<int:pk>/', views.delete_photo, name='delete-photo'),
    ]


# urlpatterns = [
#     path('add/', views.add_photo, name='add-photo'),
#     path('<int:pk>/', include([
#         path('', views.photo_details_page, name='photo-details-page'),
#         path('edit/', views.photo_edit_page, name='photo-edit-page'),
#         path('delete/<int:pk>/', views.delete_photo, name='delete-photo')
#     ]))
# ]