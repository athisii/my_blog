from django.urls import path
from .views import (PostListView,
                    PostDetaiView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    SearchPostListView
                    )
from .import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('$', SearchPostListView.as_view(), name='search-post'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetaiView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about')
]
