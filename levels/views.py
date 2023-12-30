from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def level0(request):
    return render(request, 'levels/level0.html')

def level1(request):
    return render(request, 'levels/level01.html')

def level2(request):
    return render(request, 'levels/level02.html')

def level3(request):
    return render(request, 'levels/level03.html')

def level4(request):
    return render(request, 'levels/level04.html')

def level5(request):
    return render(request, 'levels/level05.html')

def level6(request):
    return render(request, 'levels/level06.html')

def level7(request):
    return render(request, 'levels/level07.html')

def level8(request):
    return render(request, 'levels/level08.html')

def level9(request):
    return render(request, 'levels/level09.html')

def level10(request):
    return render(request, 'levels/level10.html')

def level11(request):
    team = request.GET.get('t')
    print(team)
    if team != 'emacs':
        return redirect('level0')
    return render(request, 'levels/level11.html')

def level12(request):
    return render(request, 'levels/level12.html')

def level13(request):
    return render(request, 'levels/level13.html')

def level14(request):
    return render(request, 'levels/level14.html')

def level15(request):
    return render(request, 'levels/level15.html')

def level16(request):
    return render(request, 'levels/level16.html')

def level17(request):
    return render(request, 'levels/level17.html')

def level18(request):
    return render(request, 'levels/level18.html')

def level19(request):
    return render(request, 'levels/level19.html')

def level20(request):
    return render(request, 'levels/level20.html')

def level21(request):
    return render(request, 'levels/level21.html')

def level22(request):
    return render(request, 'levels/level22.html')

def level23(request):
    return render(request, 'levels/level23.html')

def level24(request):
    return render(request, 'levels/level24.html')

def level25_part1(request):
    return render(request, 'levels/level25_part1.html')

def level25_part2_and_level_26(request):
    referer = request.META.get('HTTP_REFERER')
    if (referer != 'nasa.com'):
        return render(request, 'levels/level25_part2.html')
    else:
        return render(request, 'levels/level26.html')

def level27(request):
    return render(request, 'levels/level27.html')

def custom_404_view_1(request, url):
    return render(request, '404/404.html', status=404)
