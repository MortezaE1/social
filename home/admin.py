from django.contrib import admin
from .models import Post, Comment, Vote

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updated')
    search_fields = ('slug','body')
    list_filter = ('updated',)
    prepopulated_fields = {'slug':('body',)}
    raw_id_fields = ('user',)
# admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','body', 'post', 'created', 'is_reply')
    raw_id_fields = ('post', 'user', 'reply')

# @admin.register(Vote)
# class VoteAdmin(admin.ModelAdmin):
#     # list_display = ('user', 'post')
#     pass
admin.site.register(Vote)