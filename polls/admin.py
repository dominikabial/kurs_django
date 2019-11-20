from django.contrib import admin
from .models import Question, Choice


# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    fields = ['id', 'choice_text']
    suit_classes = 'suit-tab suit-tab-questions'


class AdminQuestion(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']
    search_fields = ['question_text']
    list_filter = ['is_active']

    fieldsets = [
        ("Główne", {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['id', 'question_text', 'is_active']}),
        ("Daty", {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['pub_date']}),
        ("Image", {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['question_image']}),
        # ("Poziom trudnosci", {'fields': ['level']})
    ]

    suit_form_tabs = (('general', 'General'), ('Daty', 'Daty'),
                      ('Image', 'Image'), ('other', 'Other'),
                      ('questions', 'Questions')
                      )

    inlines = [ChoiceInline]
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(Question, AdminQuestion)

admin.site.register(Choice)
