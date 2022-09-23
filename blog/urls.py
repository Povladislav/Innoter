from django.urls import path

from .views import PageView, PostView, TagView

urlpatterns = [
    path('tag/', TagView.as_view({"get": "list", "post": "create"})),
    path('tag/<int:pk>', TagView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"})),
    path('post/', PostView.as_view({"get": "list", "post": "create"})),
    path('post/<int:pk>', PostView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"})),
    path('page/', PageView.as_view({"get": "list", "post": "create"})),
    path('page/<int:pk>', PageView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"}))
]
