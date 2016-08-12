from django.contrib import admin

# Register your models here.
from .models import Publisher, Auther, Book

class AutherAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publishers', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    #fields = ('title', 'authors', 'publishers', 'publication_date')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publishers',)

admin.site.register(Publisher)
admin.site.register(Auther, AutherAdmin)
admin.site.register(Book, BookAdmin)
