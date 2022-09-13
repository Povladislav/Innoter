from django.urls import path
from .views import CreateTag, ReadTag,UpdateTag

urlpatterns = [
    path('create/', CreateTag.as_view(), name="create_tag"),
    path('read/', ReadTag.as_view(), name="read_tag"),
    path('update/<int:pk>/', UpdateTag.as_view(), name="read_tag")
]
