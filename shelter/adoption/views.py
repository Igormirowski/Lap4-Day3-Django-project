from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# Create your views here.
from .models import Dog

doggos = [
    { 'id': 1, 'name': 'Cody', 'breed': 'Cockapoo', 'owner': 'Yvonne'},
    { 'id': 2, 'name': 'Luffy', 'breed': 'Shiba', 'owner': 'Kieran'},
    { 'id': 3, 'name': 'Yami', 'breed': 'Shiba', 'owner': 'Trevor'}
]

def home(request):
    # return HttpResponse("<h1>Starts here</h1>")
    return render (request, 'adoption/home.html')


def about(request):
    return render(request, 'adoption/about.html')



def dogs(request):
    data = {'doggos': Dog.objects.all()}
    return render(request, 'adoption/dogs.html', data)
        # 'doggos': doggos 
    # return HttpResponse(
        # "<h1>There are all our dogs</h1>"
        # f"<p>We have {len(doggos)} dogs in out shelter</p>"
        # )


def show(request, id):
    # dog = list(filter(lambda doggo: doggo['id'] == id, doggos))
    dog = get_object_or_404(Dog, pk=id)
    data = {'dog': dog}
    return render (request, 'adoption/show.html', data)
    # return HttpResponse(
    #     f"<h1>This page is for dog number {id}!</h1>"
    #     f"<p>His name is {dog[0]['name']}.</p>"
    # )
