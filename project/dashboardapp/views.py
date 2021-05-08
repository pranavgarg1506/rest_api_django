from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def UserDashboard(request):

    print("method in UserDashboard", request.method)
    if request.method == 'GET':
        response = requests.get('http://127.0.0.1:8000/user/api/')
        print(type(response))
        print(response)
        print(response.status_code)
        if response.status_code != 200:
            raise ApiError('GET /tasks/ {}'.format(response.status_code))
        total = []
        for record in response.json():
            print(record)
            temp = []
            temp.append(record['id'])
            temp.append(record['name'])
            print(record['id'], record['name'])
            total.append(temp)

        return HttpResponse(total)