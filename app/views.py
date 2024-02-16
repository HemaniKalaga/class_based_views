from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import View,TemplateView
# Create your views here.

#using HttpResponse
def fbv_string(request):
    return HttpResponse('this is function based view using HttpResponse')

class Cbv_string(View):
    def get(self,request):
        return HttpResponse('this is a class based function view using HttpResponse')
    

#
def fbvhtml(request):
    return render(request,'fbvhtml.html')

class CbvHtml(View):
    def get(self,request):
        return render(request,'CbvHtml.html')



#using templates
#insertion of data using template(View)
def insert_book_by_fbvt(request):
    BFO=BookForm()
    d={'BFO':BFO}

    if request.method=='POST':
        BFDO=BookForm(request.POST)
        if BFDO.is_valid():
            BFDO.save()
            return HttpResponse('The Data is inserted')
    return render(request,'insert_book_by_fbvt.html',d)


class insert_book_by_cbvt(View):
    def get(self,request):
        BFO=BookForm()
        d={'BFO':BFO}
        return render(request,'insert_book_by_cbvt.html',d)
    
    def post(self,request):
        SFDO=BookForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Insertion is done')
        
#insertion of data using template(TemplateView)
class Cbv_Template(TemplateView):
    template_name='Cbv_Template.html'
        

        

        


    
        
'''#--------------------------------------------------------------------------

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *


# Returning string as response by using FBV
def fbv_string(request):
    return HttpResponse('<h1>This is the string from fbv_string')

# Returning string as response by using Class Based View

class CbvString(View):
    def get(self,request):
        return HttpResponse('String of CbvString')


# rendering html by FBV

def fbvhtml(request):
    return render(request,'fbvhtml.html')

# rendering html by Class Based Views 

class CbvHtml(View):
    def get(self,request):
        return render(request,'CbvHtml.html')

# Insert Data by FBV through Model Forms


def insert_school_by_fbv(request):
    SFO=SchoolForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_fbv is done')
    return render(request,'insert_school_by_fbv.html',d)

# Insert Data By using Class Based View

class InsertSchoolByCbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'InsertSchoolByCbv.html',d)
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertSchoolByCbv is done')



class Cbv_Template(TemplateView):
    template_name='Cbv_Template.html'
    '''