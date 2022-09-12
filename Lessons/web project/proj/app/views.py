from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author

# Create your views here.
def home(request):
    return render(request, 'home.html')

def posts(request):
    posts = Post.objects.all().order_by('issued')
    post_list = ""

    for post in posts:
        post_list += f"<li><h3>{post.title}</h3><p>by {post.author.name}</p><p>{post.id}</p></li>"
        print(type(post.id))

    response = f"<h1>Posts:</h1><ul>{post_list}</ul>"
    return HttpResponse(response)

def post(request, id):
    try:
        post = Post.objects.get(id=id)
        response = f"<h3>{post.title}</h3><p>by {post.author.name}</p><p>{post.content}</p>"
    except:
        response = "<h3>The post was not found</h3>"

    return HttpResponse(response)