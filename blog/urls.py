from django.urls import path
from .views import CreateTag,ReadTag

urlpatterns = [
    path('create/', CreateTag.as_view(), name="create_tag"),
    path('read/', ReadTag.as_view(), name="read_tag")
]
