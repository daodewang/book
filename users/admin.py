from django.contrib import admin

from .models import UserProfile, Book, Type

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Book)
#admin.site.register(Type)

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_type', 'code')
    search_fields = ['category_type']


admin.site.register(Type, TypeAdmin)


