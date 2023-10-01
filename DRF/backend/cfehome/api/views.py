from django.http import JsonResponse
import json

# Django Models

def api_home(request, *args, **kwargs):
    # requests -> HttpRequest -> Django
    # print(dir(request))
    # requests.body
    print(request.GET) # url query params
    print(request.POST)
    body = request.body  # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)  # string og JSON data -> Python Dict
    except:
        pass
    print(data)
    # data['headers'] = request.headers  # request.META ->
    data['params'] = dict(request.GET)
    print(request.headers)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
