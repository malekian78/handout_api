from django.contrib import admin
from .models import Author, Category, Handout, Tag

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Handout)
admin.site.register(Tag)
