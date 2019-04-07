import json
from django.http import HttpResponse
from classes.RedisClass import *


def get(request):

    status = {}
    if request.method != 'GET':
        status['status'] = 'error'
        status['response'] = 'wrong method, use GET'
        return HttpResponse(json.dumps(status))

    try:
        key = request.path.split('/')[-1]
    except Exception as e:
        status['status'] = 'error'
        status['response'] = str(e)
        return HttpResponse(json.dumps(status))

    redis_obj = RedisClass()

    value = redis_obj.get_key(key)

    return HttpResponse(json.dumps(value))


def put(request):

    status = {}
    if request.method != 'POST':
        status['status'] = 'error'
        status['response'] = 'wrong method, use POST'
        return HttpResponse(json.dumps(status))

    try:
        data = json.loads(request.body)
    except Exception as e:
        status['status'] = 'error'
        status['response'] = str(e)
        return HttpResponse(json.dumps(status))

    try:
        key = data['key']
        value = data['value']
    except:
        status['status'] = 'error'
        status['response'] = 'wrong usage, send {\'key\':\'<key>\',\'value\':\'<value>\'} as json in data'
        return HttpResponse(json.dumps(status))

    redis_obj = RedisClass()

    value = redis_obj.set_key(key, value)

    return HttpResponse(json.dumps(value))

def home_error(request):

    status = {}
    status['status'] = 'error'
    status['response'] = 'wrong endpoint provided, use /get or /put'
    return HttpResponse(json.dumps(status))