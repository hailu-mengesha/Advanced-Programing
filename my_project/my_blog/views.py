from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm,PostUpdateForm
# Create your views here.
def index(request):
    posts=Post.objects.all()
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('index')
    else:
        form=PostForm()
    context={
        'posts':posts,
        'form':form
    }
    return render(request,'my_blog/index.html',context)

#def about(request):
 #   return HttpResponse('<h1 style="color:blue">about page</h1>')

def post_detail(request,pk):
    post=Post.objects.get(id=pk)
    context={
        'post':post,

    }
    return render(request,'my_blog/post_detail.html',context)

def post_edit(request,pk):
    post=Post.objects.get(id=pk)
    if request.method=='POST':
        form=PostUpdateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail',pk=post.id)
    else:
        form=PostUpdateForm(instance=post)
    context={
        'post':post,
        'form':form

    }
    return render(request,'my_blog/post_edit.html',context)


def post_delete(request,pk):
    post=Post.objects.get(id=pk)
    if request.method=='POST':
        post.delete()
        return redirect('index')
    context={
        'post':post
    }
    return render(request,'my_blog/post_delete.html',context)


