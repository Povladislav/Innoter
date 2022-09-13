from django.urls import path

from .views import TagView

urlpatterns = [
    path('read/', TagView.as_view({"get": "list"}), name="read_tag"),
    path('create/', TagView.as_view({"post": "create"}), name="create_tag"),
    path('update/<int:pk>', TagView.as_view({"put": "update"}), name="update_tag"),
    path('delete/<int:pk>', TagView.as_view({"delete": "destroy"}), name="delete_tag"),
]
