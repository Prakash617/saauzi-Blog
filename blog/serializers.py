from .models import *
from rest_framework import serializers


class Comment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentMeta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CommentMeta
        fields = '__all__'

class Post_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

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

class Term_Taxonomy_Serializer(serializers.ModelSerializer):
     class Meta:
        model = Term_Taxonomy
        fields = '__all__'

class Term_Relationship_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Term_Relationship
        fields = '__all__'

class Option_Serializer(serializers.ModelSerializer):
     class Meta:
        model = Option
        fields = '__all__'

class Link_Serializer(serializers.ModelSerializer):
     class Meta:
        model = Link
        fields = '__all__'