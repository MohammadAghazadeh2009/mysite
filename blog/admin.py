from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author','published_date', 'counted_views', 'status', 'created_date','login_require', 'updated_date')
    list_filter = ('status',)
    #ordering = ['-created_date']
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_filter = ('approved',)
    list_display = ('name','approved', 'created_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
