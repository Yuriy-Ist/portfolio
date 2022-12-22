from django.shortcuts import render

from .models import PhotoCategory



def home(request):
    categorys = PhotoCategory.objects.all()
    context =  {
        'categorys':categorys,
        }

    return render(request, 'portfolio_app/index.html', context=context)


def portfolio(request):
    categorys = PhotoCategory.objects.all()
    return render(request, 'portfolio_app/portfolio.html', context={'categorys':categorys})


def contact(request):
    categorys = PhotoCategory.objects.all()
    return render(request, 'portfolio_app/contact.html', context={'categorys':categorys})


def portfolio_detail(request, pk):
    categorys = PhotoCategory.objects.all()
    category = PhotoCategory.objects.get(id=pk)
    photos = category.photosets_set.all()
    context = {
        'photos':photos, 
        'category':category,
        'categorys':categorys
        }
    return render(request, 'portfolio_app/portfolio_detail.html', context=context)