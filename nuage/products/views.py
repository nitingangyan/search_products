import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status

from products.helper import search_product_on_multiple_url

# Create your views here.

def products_view(request):
    return render(request, "index.html")


@api_view(http_method_names=['GET'])
def search_product_view(request):
    search_text = request.GET.get("search_text", None)
    page_no = request.GET.get("page_no", None)
    try:
        response = search_product_on_multiple_url(search_text, page_no)
        return HttpResponse(json.dumps(response), status=status.HTTP_200_OK, content_type="application/json")
    except Exception as e:
        logger.exception('search_text: Exception {0}'.format(str(e)))
        return HttpResponse({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type="application/json")
