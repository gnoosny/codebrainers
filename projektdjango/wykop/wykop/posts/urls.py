from django.urls import path

from wykop.posts.views import (DeletePost, PostCreate, PostList, PostView,
                               TopPostsList, UpdatePost, VoteView)

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('<int:pk>', PostView.as_view(), name='detail'),
    path('add', PostCreate.as_view(), name='add'),
    path('<int:pk>/update', UpdatePost.as_view(), name='update'),
    path('<int:pk>/delete', DeletePost.as_view(), name='delete'),
    path('vote/<int:post_pk>', VoteView.as_view(), name='vote'),
    path('top/', TopPostsList.as_view(), name='top-list')
]