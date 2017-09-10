from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
from .models import Package


def softmax(L):
    values = []
    for n in L:
        s = np.exp(n) / sum(map(lambda x: np.exp(x), L))
        values.append(s)
    return values


# Views
def index(request):
    if request.method == 'GET':
        ninguno = request.GET.get('ninguno', '0')
        vacaciones = request.GET.get('vacaciones', '0')
        negocios = request.GET.get('negocios', '0')
        aventura = request.GET.get('aventura', '0')
        festivales = request.GET.get('festivales', '0')
        vector = [int(x) for x in [ninguno, vacaciones, negocios, aventura, festivales]]
        vector_max = softmax(vector)
        index = vector_max.index(max(vector_max))

        packages = Package.objects.filter(segment=index).values()

        response = list(packages)
    else:
        response = {'403': 'bad request'}
    return JsonResponse(response, safe=True)
