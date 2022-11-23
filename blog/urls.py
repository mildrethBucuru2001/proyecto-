from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
urlpatterns=[
		path('post/new/', BlogCreateView.as_view(),
			name='post_new'),
		path('post/<int:pk>/', BlogDetailView.as_view(),
			name='post_detail'),
		path('',BlogListView.as_view(),name='home'),
		path('post/update/<int:pk>/', BlogUpdateView.as_view(),
			name='post_update'),
		path('post/delete/<int:pk>/', BlogDeleteView.as_view(),
			name='post_delete'),

]
