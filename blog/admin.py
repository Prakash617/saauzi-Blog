from django.contrib import admin
from .models import *
# Register your models here.

model=[Comment,CommentMeta,Author,Post,PostMeta,Term,TermMeta,Category,Option,Link]


for x in model:
    admin.site.register(x)