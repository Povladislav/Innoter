from django.urls import path

from .views import TagView

urlpatterns = [
    path('tag/', TagView.as_view({"get": "list", "post": "create"})),
    path('tag/<int:pk>', TagView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"}))
]
