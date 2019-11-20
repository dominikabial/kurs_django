from books.models import ImportComment

def books_context_processor(request):
    return {'important_message':'to jest wazna wiadomosc'}

def info_admin_panel(reqest):
    last_info = ImportComment.objects.latest('id')
    return {'message_admins_panel': f'{last_info}'}