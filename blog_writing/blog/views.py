from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Blog, Comment ,Category, Tag
# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .serializers import BlogListSerializer,BlogCategoryListSerializer,LoginSerializer,BlogTagListSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics, permissions, status,filters
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)



def Blogpage(request):
    blog_list = Blog.objects.all().order_by('-id')
    page = request.GET.get('page',1)
    paginator = Paginator(blog_list, 4)

    try:

        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)



    context = {


        'paginate':blogs,

    }
    return render(request, 'home.html', context)

def blogdetail(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    user = request.user
    new_comment = None
    comments = blog.comments.filter(active=True)
    try:
        next_blog = blog.get_next_by_timestamp()
    except Blog.DoesNotExist:
        next_blog = None

    try:
        previous_blog = blog.get_previous_by_timestamp()
    except Blog.DoesNotExist:
        previous_blog = None
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
                # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # Create Comment object but don't save to database yet

            # Assign the current post to the comment
            comment_form.instance.post = blog
            comment_form.instance.user= user

            # Save the comment to the database
            comment_form.save()
        else:
            comment_form = CommentForm()
    params = {
        'blog':blog,
        'next_blog': next_blog,
        'previous_blog': previous_blog,
        'comment_form' : comment_form,
        'new_comment': new_comment,
        'comments': comments,
    }

    return render(request,'blogdetail.html',params)

def searchblog(request):
    queryset = Blog.objects.order_by('timestamp')

    # General search
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__title__icontains=query)).distinct()
    tag_query = request.GET.get('tag_q')
    if tag_query:
        queryset = queryset.filter(Q(tags__title__icontains=tag_query)).distinct()

    context = {
       'search_results': queryset,
        'search_query': str(query) or str(tag_query)
         }
    return render(request,'search.html', context)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_post.html'
    fields = ['title','content','categories','tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog_post.html'
    fields = ['title','content','categories','tags',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog_delete_confirm.html'
    success_url = '/'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False

class BlogAPI(APIView):


    def get(self, request):

        # get the list of user with specified columns value
        categories = Blog.objects.all()
        serializer = BlogListSerializer(categories, many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

class BlogCategoryAPI(APIView):


    def get(self, request):

        # get the list of user with specified columns value
        categories = Category.objects.all()
        

        serializer = BlogCategoryListSerializer(categories, many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

class BlogTagAPI(APIView):


    def get(self, request):

        # get the list of user with specified columns value
        categories = Tag.objects.all()
        

        serializer = BlogTagListSerializer(categories, many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key,"username": user.username,"uid": user.id}, status=200)
