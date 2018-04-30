from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package

'''注册'''
@require_http_methods(["POST"])
def handle_register(request):
    pass