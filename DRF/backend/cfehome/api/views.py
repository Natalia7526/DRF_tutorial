from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product


# Django Models

# def api_home(request, *args, **kwargs):
#     # requests -> HttpRequest -> Django
#     # print(dir(request))
#     # requests.body
#     print(request.GET) # url query params
#     print(request.POST)
#     body = request.body  # byte string of JSON data
#     data = {}
#     try:
#         data = json.loads(body)  # string og JSON data -> Python Dict
#     except:
#         pass
#     print(data)
#     # data['headers'] = request.headers  # request.META ->
#     data['params'] = dict(request.GET)
#     print(request.headers)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
        print(data)
    return JsonResponse(data)
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # model instance (model data)
        # turn a Python dict
        # return JSON to my client -> serialization
    #     data = dict(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})
