from django.urls import path

from blogs.views import blog_detail_view, BlogListView

app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('<int:pk>/', blog_detail_view, name='detail'),
]
