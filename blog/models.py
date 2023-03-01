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
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return self.comment_author
     

class CommentMeta(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()

    def __str__(self):
        return self.comment

class Author(models.Model):
    name = models.CharField(max_length=250)
    website = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    linkdin = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Term(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    def __str__(self):
        return self.name
        

class Post(models.Model):
    # user = models.Foreignkey(CustomUser,relative_name = 'user', on_delete = models.CASCADE )
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    post_date_gmt = models.DateTimeField(auto_now_add=True)
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    reading_time = models.CharField(max_length=100,null=True)
    POST = (("Draft","Draft"),("published","published"),("Scheduled","Scheduled"))
    post_status = models.CharField(max_length=20,choices=POST, default="published")
    comment_status = models.ForeignKey(Comment, related_name='comment', on_delete=models.CASCADE)
    PING = (("Draft","Draft"),("published","published"),("Scheduled","Scheduled"))
    ping_status = models.CharField(max_length=200,choices=PING, default="published")
    post_password = models.CharField(max_length=20, null=True, blank=True)
    post_name = models.CharField(max_length=200, null=True, blank=True)
    to_ping = models.TextField(null=True, blank=True)
    pinged = models.TextField(null=True, blank=True)
    post_modified = models.DateTimeField(auto_now_add=True)
    post_modified_gmt = models.DateTimeField(auto_now_add=True)
    post_content_filtered = models.TextField(null=True, blank=True)
    post_parent = models.BigIntegerField(null=True, blank=True)
    guid = models.CharField(max_length=255, null=True, blank=True)
    menu_order = models.IntegerField(null=True, blank=True)
    post_type = models.CharField(max_length=20, null=True, blank=True)
    post_mime_type = models.CharField(max_length=100, null=True, blank=True)
    comments_count = models.ForeignKey(Comment,on_delete=models.CASCADE)
    category_name = models.ForeignKey('blog.Category',on_delete=models.CASCADE)



class PostMeta(models.Model):
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()
    
    def __str__(self):
        return self.meta_key
 
class Term(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    def __str__(self):
        return self.name

class TermMeta(models.Model):
    term_id = models.ForeignKey(Term,on_delete=models.CASCADE)
    meta_key = models.CharField(max_length=255)
    meta_value = models.TextField()

    def __str__(self):
        return self.meta_key

class Category(models.Model):
    term_id = models.ForeignKey(Term,on_delete=models.CASCADE)
    category_name = models.CharField(max_length=32)
    description = models.TextField()
    slug = models.CharField(max_length=200)
    parent = models.BigIntegerField()
    count = models.BigIntegerField()

    def __str__(self):
        return self.category_name


# class Term_Relationship(models.Model):
#     term_taxonomy_Id = models.ForeignKey(Term_Taxonomy,on_delete=models.CASCADE)
#     term_order = models.IntegerField()

class Option(models.Model):
    option_name = models.CharField(max_length=191)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    def __str__(self):
        return self.option_name


class Link(models.Model):
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.ImageField(upload_to='images/img')
    link_target = models.CharField(max_length=25)
    link_description = models.TextField()
    link_visible = models.CharField(max_length=20)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField(auto_now_add=True)
    link_ref = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    def __str__(self):
        return self.link_name

