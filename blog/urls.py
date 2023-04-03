from django.urls import path

from .views import PageView, PostView, TagView

urlpatterns = [
    path('tag/', TagView.as_view({"get": "list"}), name="tag"),
    path('tag/<int:id>/', TagView.as_view({"put": "update", "delete": "destroy", "get": "retrieve", "post": "create"}),
         name="tag_id"),
    path('post/', PostView.as_view({"get": "list"}), name="post"),
    path('post/<int:id>/',
         PostView.as_view({"put": "update", "delete": "destroy", "get": "retrieve", "post": "create"}),
         name="post_id"),
    path('page/', PageView.as_view({"get": "list"}), name="page"),
    path('page/<int:id>/',
         PageView.as_view({"put": "update", "delete": "destroy", "get": "retrieve", "post": "create"}),
         name="page_id")
]
