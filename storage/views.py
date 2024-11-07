from django.db.models import Min
from django.shortcuts import render
from .models import Storehouse, StorehouseImage, Box
from django.http import JsonResponse

def view_products(request):
    storehouses = Storehouse.objects.all()
    images_store = StorehouseImage.objects.all()
    boxes_store = Box.objects.all()
    store_serialized = []

    for storehouse in storehouses:
        images = images_store.filter(storehouse=storehouse)
        boxes = boxes_store.filter(storehouse=storehouse, price__isnull=False)
        min_price_box = boxes.order_by('price').first().price
        store_serialized.append(
            {
                "id": storehouse.id,
                "city": storehouse.city,
                "address": storehouse.address,
                "description": storehouse.description,
                "amount_box": boxes.count(),
                "min_price": min_price_box,
                "images": [image.img.url for image in images]
            }
        )


    #return render(request, template_name="boxes.html", context={'boxes': boxes})
    return render(request, template_name="boxes.html", context={'storehouses': store_serialized})



def avaliable_boxes(request, storehous_id):
    storehouse = Storehouse.objects.get(id=storehous_id)
    avaliable_boxes = storehouse.boxes.all()
    boxes_serialized = [
        {
            "code": box.box_number,
            "floor": box.floor,
        }
        for box in avaliable_boxes
    ]

    return JsonResponse({"boxes": boxes_serialized})
