
from app.models import Product
import json


def getRecommendation(profile):
    products = Product.objects.filter(tags__in=profile)
    if products.count() != 0:
        return json.dumps(products[0].to_json())
    else:
        return "{}"
