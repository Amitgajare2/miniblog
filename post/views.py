from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category

def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'post/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        comment = request.POST.get('comment', '')

        if name and comment:
            Comment.objects.create(
                post=post,
                name=name,
                comment=comment
            )

            return redirect('post_detail', slug=post.slug)

    return render(request, 'post/detail.html', {'post': post})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)

    return render(request, 'post/category.html', {'category': category})