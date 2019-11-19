from django.contrib import admin
from .models import Question, Choice
# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    fields = ['id','choice_text']

class AdminQuestion(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']
    search_fields = ['question_text']
    list_filter = ['is_active']

    fieldsets = [
        ("Główne", {'fields': ['id','question_text', 'is_active']}),
        ("Daty", {'fields':['pub_date']}),
        ("Image", {'fields': ['question_image']}),
        #("Poziom trudnosci", {'fields': ['level']})
    ]

    inlines = [ChoiceInline]
    readonly_fields = ['id', 'created', 'modified']

admin.site.register(Question, AdminQuestion)


admin.site.register(Choice)
