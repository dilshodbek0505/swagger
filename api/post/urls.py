from django.urls import path
from .views import PostApi, CommentApi, CommentEditApi, PostEditApi

urlpatterns = [
    path("post/", PostApi.as_view()),
    path("post/details/<int:pk>/", PostEditApi.as_view()),
    path('comment/', CommentApi.as_view()),
    path("comment/details/<int:pk>/", CommentEditApi.as_view())
]
