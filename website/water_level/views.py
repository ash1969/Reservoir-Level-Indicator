from django.shortcuts import render

# Create your views here.


def karnataka_map(request):

    args = {}
    return render(request, 'water_level/karnataka.html', args)