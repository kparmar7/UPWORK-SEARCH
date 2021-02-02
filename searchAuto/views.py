from django.shortcuts import render
from searchAuto.models import Product
from django.http import JsonResponse
def autoComplete(request):
    print(request.GET.get('term'))
    if 'term' in request.GET:
        qu = Product.objects.filter(title__istartswith = request.GET.get('term'))
        titles = list()
        print(qu,'-----------')
        for product in qu:
            titles.append(product.title)
        return JsonResponse(titles, safe=False)
    return render(request, 'home.html')

