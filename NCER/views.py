from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")

#二级python
def python_66(request):
    return HttpResponse("Hello python ! ")

#四级嵌入式
def embeded_45(request):
    pass


#三级嵌入式
def embeded_39(request):
    pass

#二级C
def c_24(request):
    pass