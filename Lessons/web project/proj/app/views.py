from datetime import datetime
from http.client import NOT_FOUND
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Author
from .forms import AddPost

# Create your views here.
def home(request):
    return render(request, 'home.html')

# def posts(request):
#     posts = Post.objects.all().order_by('issued')
#     post_list = ""

#     for post in posts:
#         post_list += f"<li><h3>{post.title}</h3><p>by {post.author.name}</p><p>{post.id}</p></li>"
#         print(type(post.id))

#     response = f"<h1>Posts:</h1><ul>{post_list}</ul>"
#     return HttpResponse(response)

# def post(request, id):
#     try:
#         post = Post.objects.get(id=id)
#         response = f"<h3>{post.title}</h3><p>by {post.author.name}</p><p>{post.content}</p>"
#     except:
#         response = "<h3>The post was not found</h3>"

#     return HttpResponse(response)

def posts(request):
    all_posts = Post.objects.all().order_by('-issued')
    return render(request, 'posts.html', {'posts':all_posts})

def post(request, id):
    try:
        post = Post.objects.get(id=id)
        return render(request, 'post.html', {'post':post})
    except:
        return NOT_FOUND

def add_post(request):
    form = AddPost()

    if request.method == 'POST':
        form = AddPost(request.POST, request.FILES)

        if form.is_valid():
            new_post = Post()
            new_post.title = form.cleaned_data['title']
            new_post.subtitle = form.cleaned_data['subtitle']
            new_post.content = form.cleaned_data['content']
            new_post.image = form.cleaned_data['image']
            new_post.post_theme = form.cleaned_data['post_theme']
            new_post.author = Author.objects.all()[0]
            new_post.issued = datetime.now()

            new_post.save()

            return redirect('posts')

    return render(request, 'add_post.html', {'form':form})