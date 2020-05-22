from django.shortcuts import render

# Create your views here.
def jumbotron(request):
    return render(request,'myapp/jumbotron.html')

def carousel(request):
	return render(request, 'myapp/carousel.html')

def album(request):
	return render(request, 'myapp/album.html')

def signin(request):
	return render(request, 'myapp/sign-in.html')

def registro(request):
	return render(request, 'myapp/registro.html')