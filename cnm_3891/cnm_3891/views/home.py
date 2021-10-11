from django.http import HttpResponse
import os

def index(request):
    folderName = os.getcwd()
    htmlFile = open(folderName + '/cnm_3891/views/home.html', 'r')
    html = htmlFile.read()
    return HttpResponse(html)