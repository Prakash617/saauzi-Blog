from .models import *
from rest_framework import serializers
from collections import OrderedDict


class Comment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentMeta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CommentMeta
        fields = '__all__'

class Author_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class Post_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['post_password','post_name','to_ping','pinged','post_content_filtered','post_parent','guid','menu_order','post_type','post_mime_type']
        


class PostMeta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PostMeta
        fields = '__all__'

class Term_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'

class TermMeta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TermMeta
        fields = '__all__'

class Category_Serializer(serializers.ModelSerializer):
     class Meta:
        model = Category
        fields = '__all__'

# class Term_Relationship_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Term_Relationship
#         fields = '__all__'

class Option_Serializer(serializers.ModelSerializer):
     class Meta:
        model = Option
        fields = '__all__'

class Link_Serializer(serializers.ModelSerializer):
     class Meta:
        model = Link
        fields = '__all__'