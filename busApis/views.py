from django.shortcuts import render

# Create your views here.
import requests


def home(request):
    my_headers = {'x-api-key': '?'}

    url = 'https://gtfsr.transportforireland.ie/v1/?format=json'

    response = requests.get(url, headers=my_headers)

    search_was_successful = (response.status_code == 200)  # 200 = SUCCESS

    data = response.json()

    data['success'] = search_was_successful

    return render(request, 'main.html', {'data': data})

# ['entity'][1]['trip_update']['trip']['trip_id']
