""" Views file platzigram"""
# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json

# Debugger
import pdb;

def hello_word(request):
    """ Hello word """
    now = datetime.now().strftime('%dth / %b / %Y - %H:%M hrs')
    return HttpResponse('Current server time is {now}'.format(now=str(now)))

def sorted(request):
    """ return number sortered in json format """
    # pdb.set_trace() # debugger the view
    if request.GET['numbers']:
        numbers = [int (i) for i in request.GET['numbers'].split(',')]
        numbers.sort()
        data = {
            'status': 'OK',
            'numbers': numbers,
            'message': 'Integers sorted successfully'
        }
        # pdb.set_trace()
        return HttpResponse(
            json.dumps(data, indent= 4), 
            content_type='application/json'
        )
    else:
        return HttpResponse('Nothing number')

def say_hi(request, name, age):
    """ return validation age of the user """
    if age<12:
        message = 'sorry, {} you are so young for this page'.format(name)
    else:
        message = 'hi {}, you are welcome'.format(name)
    return HttpResponse(message)