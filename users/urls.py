from django.urls import path

from .service import BanPages, BanUsers
from .views import (CurrentUserView, LoginView, LogoutView, RegisterView,
                    UserView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('ban/user/<int:id>/', BanUsers.as_view(), name='banUser'),
    path('ban/page/<int:id>/', BanPages.as_view(), name='banPage'),
    path('curuser/', CurrentUserView.as_view(), name='ban'),
    path('user/', UserView.as_view({"get": "list"})),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<int:pk>/', UserView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"}))
]
