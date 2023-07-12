from django.contrib import admin

from Petstagram.common.models import Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time_of_publication', 'to_photo')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
