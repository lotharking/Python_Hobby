""" Views file platzigram"""
from django.http import HttpResponse

def hello_word(request):
    """ Hello word """
    return HttpResponse('hello-word')