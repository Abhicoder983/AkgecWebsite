from django.shortcuts import render


# Create your views here.
def home(request):
    return render( request,'index.html')
def about(request):
    return render( request, 'about.html')
def careers(request):
    return render(request, 'Career.html')
