from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package

'''用于 保持登录状态'''
@require_http_methods(["GET"])
def handle_home(request):
    pass