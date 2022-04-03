from .models import Book, User, Bookrecord
from datetime import datetime
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Book)
class BookAdmin(ImportExportActionModelAdmin):
    search_fields = ('title', 'author')
    list_display = ('title', 'author', 'count')
    list_filter = ('author',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('role', 'first_name', 'last_name')
    list_display = ('first_name', 'role')
    list_filter = ('role', )

def mark_book_record_as_returned(modeladmin, request, queryset):
    queryset.filter(returned_on__isnull=True).update(returned_on=datetime.today())


@admin.register(Bookrecord)
class Bookrecord(admin.ModelAdmin):
    list_display = ('book', 'user', 'took_on', 'returned_on', 'is_returned',)
    autocomplete_fields = ('book', 'user',)
    list_select_related = ('book', 'user',)
    actions = (mark_book_record_as_returned, )

    def is_returned(self, book_record):
        return "yes" if book_record.is_returned else "no"

    
