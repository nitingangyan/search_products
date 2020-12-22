from threading import Thread
import requests

from django.conf import settings
from products.models import Products


def search_product_on_url(url, k):
    r = requests.get(url)
    data = r.json()
    data_list = []
    if k == "paytm":
            data_list = [{"product_id": x["product_id"], "name": x["name"], "image": x["image_url"], "price": x["actual_price"], "url": x["url"], "c_name": k} for x in data["grid_layout"]]
    if k == "shopclues":
        data_list = [{"product_id": x["product_id"],"name": x["product"], "image": x["image_url"], "price": x["price"], "url": x["product_url"], "c_name": k} for x in data["products"]]
    save_data(data_list)
    return data_list


def search_product(s_text, c_name, store=None):
    if store is None:
        store = []
    store += search_product_on_url(s_text, c_name)
    return store


def search_product_on_multiple_url(search_text, page_no):
    store = []
    threads = []
    for s in settings.SEARCH_URLS:
        s_text = s["url"].format(search_text, page_no)
        t = Thread(target=search_product, args=(s_text, s["c_name"], store))
        threads.append(t)

    [ t.start() for t in threads ]
    [ t.join() for t in threads ]
    return store


def save_data(data_list):
    for item in data_list:
        try:
            prod = Products.objects.get(product_id=item["product_id"])
            prod.name = item["name"]
            prod.image = item["image"]
            prod.url = item["url"]
            prod.price = item["price"]
        except Exception as ex:
            Products(
                product_id=item["product_id"],
                name=item["name"],
                image=item["image"],
                url=item["url"],
                price=item["price"]
            ).save()