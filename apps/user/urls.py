from django.urls import path
from apps.user.views import CustomUserListAPIViews, CustomUserDetailAPIViews


app_name = "apps.user"
urlpatterns = [
    path('', CustomUserListAPIViews.as_view(), name='users_list'),
    path('<int:pk>', CustomUserDetailAPIViews.as_view(), name='user_detail'),
]
