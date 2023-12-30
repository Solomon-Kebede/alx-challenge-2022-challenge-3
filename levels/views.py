from django.shortcuts import render

# Create your views here.
def level0(request):
    return render(request, 'levels/level0.html')

def level1(request):
    return render(request, 'levels/level1.html')

def custom_404_view_1(request, url):
    return render(request, '404/404.html', status=404)
