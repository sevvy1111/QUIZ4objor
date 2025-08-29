from django.urls import path
from .views import PostListView, PostDetailSlugView, PostDeleteView, PostUpdateView, PostCreateView
app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<str:slug>/', PostDetailSlugView.as_view(), name='post-detail'),
    path('<str:slug>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('<str:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
]