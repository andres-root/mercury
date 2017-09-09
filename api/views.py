from django.shortcuts import render
from django.http import JsonResponse
import numpy as np


def softmax(L):
    values = []
    for n in L:
        s = np.exp(n) / sum(map(lambda x: np.exp(x), L))
        values.append(s)
    return values


# Views
def index(request):
    response = {'200': 'ok'}
    return JsonResponse(response)
