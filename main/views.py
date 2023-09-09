from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Muhammad Farrel Altaf',
        'app_name': 'CarRel',
        'class': "PBP C"
    }

    return render(request, "main.html", context)