from django.shortcuts import render
from django.views.generic import ListView

from blogs.models import Blog, BlogStatus, Category, Tag


class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/blogs-list.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        return Blog.objects.filter(status=BlogStatus.PUBLISHED).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.filter(parent=None).order_by('-id')
        context["tags"] = Tag.objects.all().order_by('-id')
        context["recent_posts"] = Blog.objects.order_by('-created_at')[:2]
        return context


def blog_detail_view(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return render(request, 'shared/404.html')

    context = {
        "categories": Category.objects.filter(parent=None),
        "tags": Tag.objects.all(),
        "recent_posts": Blog.objects.order_by('-created_at')[:2],
        "blog": blog,
        "related_news": Blog.objects.filter(categories__in=blog.categories.values_list('id', flat=True)).exclude(
            id=blog.id).distinct()[:3]
    }

    return render(
        request, 'blogs/blog-detail.html',
        context
    )
