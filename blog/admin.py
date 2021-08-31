
# Register your models here.
from django.contrib import admin
from .models import Post,Gallery


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'picture')
    # fields = ['image']
    # readonly_fields = ['image_tag']
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


# admin.site.register(Post, PostAdmin)
admin.site.register(Gallery)