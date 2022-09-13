from django.urls import path
from .views import CreateTag

urlpatterns = [
    path('tags/', CreateTag.as_view(), name="create_tag")
]
