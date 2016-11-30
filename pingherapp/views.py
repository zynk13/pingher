from django.http import HttpResponse
from django.template import loader
import Converse

def index(request):
    template = loader.get_template('pingherapp/iq/index.html')
    context = {
        'latest_question_list': 'testMohit',
    }
    temp1=Converse.converse("Who won the 2016 elections")
	temp2=Converse.converse("who won the elections")
	print temp1
	print temp2
    return HttpResponse(template.render(context, request))