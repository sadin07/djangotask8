from django.contrib import admin
from .models import Book, Author, Review

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')
    search_fields = ('title', 'author')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating')
    search_fields = ('book__title',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Review, ReviewAdmin)
