from django.urls import path

from .views import page_view, post_view, tag_view

urlpatterns = [
    path('tag/', tag_view.as_view({"get": "list", "post": "create"})),
    path('tag/<int:pk>', tag_view.as_view({"put": "update", "delete": "destroy", "get": "retrieve"})),
    path('post/', post_view.as_view({"get": "list", "post": "create"})),
    path('post/<int:pk>', post_view.as_view({"put": "update", "delete": "destroy", "get": "retrieve"})),
    path('page/', page_view.as_view({"get": "list", "post": "create"})),
    path('page/<int:pk>', page_view.as_view({"put": "update", "delete": "destroy", "get": "retrieve"}))
]
