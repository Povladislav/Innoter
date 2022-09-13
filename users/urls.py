from django.urls import path

from .views import LoginView, RegisterView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/',UserView.as_view({"get": "list"})),
    path('user/<int:pk>/',UserView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"}))
]
