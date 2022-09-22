from django.urls import path

from .service import (accept_all_followers_page_view,
                      accept_follower_for_page_view, banpages_view,
                      banusers_view, followpage_view, like_post, show_news,
                      unlike_post)
from .views import login_view, logout_view, register_view, user_view

urlpatterns = [
    path('register/', register_view.as_view(), name='register'),
    path('login/', login_view.as_view(), name='login'),
    path('ban/user/<int:id>/', banusers_view.as_view(), name='ban_user'),
    path('ban/page/<int:id>/', banpages_view.as_view(), name='ban_page'),
    path('like/<int:pk>/', like_post.as_view(), name='like_post'),
    path('unlike/<int:pk>/', unlike_post.as_view(), name='unlike_post'),
    path('news/', show_news.as_view(), name='show_news_post'),
    path('follow/page/<int:id>/', followpage_view.as_view(), name='follow_page'),
    path('accept/page/<int:pk>/all/', accept_all_followers_page_view.as_view(), name='accept_all_folowers'),
    path('accept/page/<int:pk>/user/<int:idOfUser>/', accept_follower_for_page_view.as_view(),
         name='accept_particular_follower'),
    path('user/', user_view.as_view({"get": "list"})),
    path('logout/', logout_view.as_view(), name='logout'),
    path('user/<int:pk>/', user_view.as_view({"put": "update", "delete": "destroy", "get": "retrieve"}))
]
