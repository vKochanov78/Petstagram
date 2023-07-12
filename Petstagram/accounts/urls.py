from django.urls import path, include
from .views import LoginUserView, LogoutUserView, RegisterUserView, UserEditView, ProfileDetailView, ProfileDeleteView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', UserEditView.as_view(), name='profile-edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    ]))
    ]
