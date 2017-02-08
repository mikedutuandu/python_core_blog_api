from urllib.parse import quote_plus
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post,Category,Media




def post_detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "vuivcl/post_detail.html", {
        "post": post,
    })


def post_list(request):
    template = 'vuivcl/post_list.html'
    page_template = 'vuivcl/post_list_page.html'
    posts = Post.objects.filter(draft=False).order_by('-created_date')
    if request.is_ajax():
        template = page_template
    return render(request,template,{
        'entry_list': posts,
        'page_template': page_template,
    })
def post_category_list(request,slug=None):
    template = 'vuivcl/post_list.html'
    page_template = 'vuivcl/post_list_page.html'
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.all().filter(category=category,draft=False).order_by('-created_date')
    if request.is_ajax():
        template = page_template
    return render(request,template,{
        'entry_list': posts,
        'page_template': page_template,
    })

