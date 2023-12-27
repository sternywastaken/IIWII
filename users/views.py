from django.shortcuts import render, redirect
from .forms import UserRegister, LoginForm, CreateRecordForm, PostComment
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'users/index.html', context={
        'posts': posts,
    })


def register(request):
    form = UserRegister()

    if request.method == "POST":
        form = UserRegister(request.POST)

        if form.is_valid():
            form.save()
            return redirect('user-login')

    return render(request, 'users/register.html', context={
        'form': form,
    })


def user_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

    return render(request, 'users/login.html', context={
        'form': form,
    })


def user_logout(request):
    logout(request)
    return redirect('user-login')


@login_required(login_url='user-login')
def dashboard(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'users/dashboard.html', context={
        'posts': posts,
    })


@login_required(login_url='user-login')
def create_post(request):
    form = CreateRecordForm()

    if request.method == "POST":
        user = User.objects.get(username=request.user)
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(
            title=title, content=content, author=user)
        post.save()
        return redirect('user-dashboard')

    return render(request, 'users/create_post.html', context={
        'form': form,
    })


def post_comment(request, id):
    form = PostComment()
    if request.method == "POST":
        post = Post.objects.get(id=id)
        comment = request.POST['comment']
        comm = Comment.objects.create(
            comment=comment, post=post)
        comm.save()
        return redirect('home')

    return render(request, 'users/comments.html', context={
        'form': form,
    })


def view_post(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post.id)
    return render(request, 'users/post.html', context={
        'post': post,
        'comments': comments,
    })


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('user-dashboard')
