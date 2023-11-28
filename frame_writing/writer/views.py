from django.shortcuts import render

def index(request):
    message = {
        'title':'FRAME WRITER',
        'text':'test text',
    }
    return render(request, 'writer/index.html', message)
