from django.contrib import admin
from blog.models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author','published_date', 'counted_views', 'status', 'created_date', 'updated_date')
    list_filter = ('status',)
    #ordering = ['-created_date']
    search_fields = ['title', 'content']

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
