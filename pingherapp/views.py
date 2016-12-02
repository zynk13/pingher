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
    temp1=witaihandler.converse("Who won the 2016 elections")
    
    return HttpResponse(temp1[0])