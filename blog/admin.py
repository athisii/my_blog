from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['User', 'Email', 'approve']


admin.site.register(Comment, CommentAdmin)
