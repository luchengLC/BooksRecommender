from urllib import parse
import copy
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import math
from Recommender.handlers.util import dbOptions, package


#  啊啊啊啊啊，用什么 算法
@require_http_methods(["GET"])
def handle_hot_query(request):
    pass
