from django.shortcuts import render

# Create your views here.
def level0(request):
    return render(request, 'levels/level0.html')

def level1(request):
    return render(request, 'levels/level1.html')
