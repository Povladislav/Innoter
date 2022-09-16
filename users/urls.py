from django.urls import path

from .views import LoginView, LogoutView, RegisterView, UserView,CurrentUserView

from .service import AdminLogic
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('ban/<int:id>/', AdminLogic.as_view(), name='ban'),
    path('curuser/', CurrentUserView.as_view(), name='ban'),
    path('user/', UserView.as_view({"get": "list"})),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<int:pk>/', UserView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"}))
]
