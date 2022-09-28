from django.urls import path

from .views import PageView, PostView, TagView

urlpatterns = [
    path('tag/', TagView.as_view({"get": "list"}), name="tag"),
    path('tag/<int:pk>/', TagView.as_view({"put": "update", "delete": "destroy", "get": "retrieve", "post": "create"}),
         name="tag_id"),
    path('post/', PostView.as_view({"get": "list"}), name="post"),
    path('post/<int:pk>/', PostView.as_view({"put": "update", "delete": "destroy", "get": "retrieve", "post": "create"}),
         name="post_id"),
    path('page/', PageView.as_view({"get": "list"}), name="page"),
    path('page/<int:pk>/', PageView.as_view({"put": "update", "delete": "destroy", "get": "retrieve", "post": "create"}),
         name="page_id")
]
