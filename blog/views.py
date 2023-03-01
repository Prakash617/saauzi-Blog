from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response


class Comment_Viewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Comment_Serializer


class CommentMeta_Viewset(viewsets.ModelViewSet):
    queryset = CommentMeta.objects.all()
    serializer_class = CommentMeta_Serializer

class Author_Viewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = Author_Serializer


class Post_Viewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Post_Serializer

class PostMeta_Viewset(viewsets.ModelViewSet):
    queryset = PostMeta.objects.all()
    serializer_class = PostMeta_Serializer

class Term_Viewset(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = Term_Serializer

class TermMeta_Viewset(viewsets.ModelViewSet):
    queryset = TermMeta.objects.all()
    serializer_class = TermMeta_Serializer


class Category_Viewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer

class Option_Viewset(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = Option_Serializer

class Link_Viewset(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = Link_Serializer
