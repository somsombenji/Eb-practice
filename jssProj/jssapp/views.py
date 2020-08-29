from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .forms import JssForm, CommentForm
from .models import Jasoseol, Comment

def index(request):
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss':all_jss})

@login_required
def create(request):
    if request.method=="POST":
        filled_form = JssForm(request.POST)
        if not request.user.is_authenticated:
            redirect('login')
        if filled_form.is_valid():
            temp_form = filled_form.save(commit=False)
            temp_form.author=request.user
            temp_form.save()
            return redirect('index')
    jss_form = JssForm()
    return render(request, 'create.html',{'jss_form':jss_form})

def detail(request, jss_id):
    detail_jss = get_object_or_404(Jasoseol, pk=jss_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'detail_jss':detail_jss, 'comment_form':comment_form})

@login_required
def delete(request, jss_id):
    jss=Jasoseol.objects.get(pk=jss_id)
    if request.user == jss.author:
        jss.delete()
        return redirect('index')
    raise PermissionDenied

@login_required
def update(request, jss_id):
    my_jss = Jasoseol.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss)
    if request.method == "POST":
        updated_form = JssForm(request.POST, instance=my_jss)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')
        
    return render(request, 'create.html', {'jss_form':jss_form})

@login_required
def myindex(request):
    my_jss = Jasoseol.objects.filter(author=request.user)
    return render(request, 'index.html', {'all_jss':my_jss})

@login_required
def createComment(request, jss_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.jasoseol = Jasoseol.objects.get(pk=jss_id)
        temp_form.save()
        return redirect('detail', jss_id)

@login_required
def deleteComment(request, jss_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.user==comment.author:
        comment.delete()
        return redirect('detail', jss_id)
    else:
        raise PermissionDenied