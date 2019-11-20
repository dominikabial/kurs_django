from django.contrib import admin
from .models import Autor, Book, Publisher, Comment, ImportComment

# Register your models here.
#admin.site.register(Autor)

admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Comment)
#admin.site.register(ImportComment)
@admin.register(Autor)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
#    pass
    #def ger_author(self, obj):


#@admin.register(Book)
#class BookAdmin(admin.ModelAdmin):
#    list_display = ['title', 'author']
@admin.register(ImportComment)
class AdminInfo(admin.ModelAdmin):
    pass
