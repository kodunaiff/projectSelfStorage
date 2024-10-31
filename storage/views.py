from django.shortcuts import render

def view_products(request):
    boxes = [
        {
            'name': 'тест_Новосибирск',
            'address': 'ул. Лермонтова д.15_тест',
        },
        {
            'name': 'тест_Иркутск',
            'address': 'ул. Пушкина д.17_тест',
        },
    ]
    # logic
    return render(request, template_name="boxes.html", context={'boxes': boxes})
    #return render(request, template_name="boxes.html")


# Create your views here.
