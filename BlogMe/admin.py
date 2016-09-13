from django.contrib import admin
from BlogMe.models import posts

class PostAdmin(admin.ModelAdmin):
    list_display = ["title","timestamp","update"]
    #list_display_links = ["update"]
    search_fields = ["title","content"]
    class Meta:
        model = posts
# Register your models here.
admin.site.register(posts,PostAdmin)