from django.conf.urls import include, url
from django.contrib import admin
from products.views import products_view, search_product_view

urlpatterns = [
    # Examples:
    url(r'^search_product', search_product_view),
    url(r'^$', products_view, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
