from django.urls import path

from .service import (AcceptAllFollowersPageView,
                      AcceptFollowerForPageView,
                      BanPagesView,
                      BanUsersView,
                      FollowpageView,
                      LikePostView,
                      ShowNewsView,
                      ShowLikedPosts,
                      SearchPageView,
                      UnlikePostView)
from .views import (LoginView,
                    LogoutView,
                    RegisterView,
                    UserView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('search/', SearchPageView.as_view(), name='search'),
    path('ban/user/<int:id>/', BanUsersView.as_view(), name='ban_user'),
    path('ban/page/<int:id>/', BanPagesView.as_view(), name='ban_page'),
    path('like/<int:id>/', LikePostView.as_view(), name='like_post'),
    path('unlike/<int:id>/', UnlikePostView.as_view(), name='unlike_post'),
    path('news/', ShowNewsView.as_view(), name='show_news_post'),
    path('liked/', ShowLikedPosts.as_view(), name='show_liked_post'),
    path('follow/page/<int:id>/', FollowpageView.as_view(), name='follow_page'),
    path('accept/page/<int:id>/all/', AcceptAllFollowersPageView.as_view(), name='accept_all_followers'),
    path('accept/page/<int:pk>/user/<int:id>/', AcceptFollowerForPageView.as_view(),
         name='accept_particular_follower'),
    path('users/', UserView.as_view({"get": "list"}),name="users"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<int:id>/', UserView.as_view({"put": "update", "delete": "destroy", "get": "retrieve"}))
]
