from django.http import HttpResponse
from django.template import loader
import witaihandler

def index(request):
    template = loader.get_template('pingherapp/iq/index.html') 
    context = {
        'latest_question_list': 'testMohit',
    }
    return HttpResponse(template.render(context, request))
    
def askQuestion(request):
    question=request.GET.get('question', '')
    temp1=witaihandler.converse(question)
    return HttpResponse(temp1)