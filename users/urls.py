from django.urls import path

from .service import BanPagesView, BanUsersView, FollowPageView
from .views import LoginView, LogoutView, RegisterView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('ban/user/<int:id>/', BanUsersView.as_view(), name='banUser'),
    path('ban/page/<int:id>/', BanPagesView.as_view(), name='banPage'),
    path('follow/page/<int:id>/', FollowPageView.as_view(), name='followPage'),
    path('user/', UserView.as_view({"get": "list"})),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<int:pk>/', UserView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"}))
]
