from django.db import models
from user_accounts.models import CustomUser
# Create your models here.

class Comment(models.Model):
    comment_post_Id = models.BigIntegerField()
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_IP = models.CharField(max_length=100)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_date_gmt = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()


class CommentMeta(models.Model):
    comment_id = models.ForeignKey(Comment,on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()


class Post(models.Model):
    post_author = models.BigIntegerField()
    post_date = models.DateTimeField(auto_now_add=True)
    post_date_gmt = models.DateTimeField(auto_now_add=True)
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=20)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField(auto_now_add=True)
    post_modified_gmt = models.DateTimeField(auto_now_add=True)
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comments_count = models.ForeignKey(Comment,on_delete=models.CASCADE)


class PostMeta(models.Model):
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()

 
class Term(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

class TermMeta(models.Model):
    term_id = models.ForeignKey(Term,on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()

class Term_Taxonomy(models.Model):
    term_id = models.ForeignKey(Term,on_delete=models.CASCADE)
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    slug = models.CharField(max_length=200)
    parent = models.BigIntegerField()
    count = models.BigIntegerField()


class Term_Relationship(models.Model):
    term_taxonomy_Id = models.ForeignKey(Term_Taxonomy,on_delete=models.CASCADE)
    term_order = models.IntegerField()

class Option(models.Model):
    option_name = models.CharField(max_length=191)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)


class Link(models.Model):
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.TextField()
    link_visible = models.CharField(max_length=20)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField(auto_now_add=True)
    link_ref = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

