from django.contrib import admin

# Register your models here.
from .models import Post, Category, Media


class MediaInline(admin.TabularInline):
    model = Media
    extra = 1


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['title',"category","user","post_type","viewed_number","draft","publish"],
        })
    ]
    list_display = ["title", "category", "user", "post_type", "viewed_number", "draft", "created_date", "updated_date"]
    list_display_links = ["title"]
    list_editable = ["draft"]
    list_filter = ["category", "user", "post_type", "draft"]
    search_fields = ["title"]
    inlines = [MediaInline]


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "enabled"]
    list_display_links = ["name"]
    list_editable = ["enabled"]
    list_filter = ["enabled"]

    search_fields = ["name"]


admin.site.register(Category, CategoryAdmin)
