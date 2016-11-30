from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('pingherapp/iq/index.html')
    context = {
        'latest_question_list': 'testMohit',
    }
    return HttpResponse(template.render(context, request))