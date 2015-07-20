from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt

from api import views

urlpatterns = [
    url(r'^GetAllUsers/$', csrf_exempt(views.RetrieveAllUsers.as_view())),
    url(r'^RetrieveUserById/(?P<pk>[0-9]+)/$', csrf_exempt(views.RetrieveUser.as_view())),
    url(r'^GetAllProducts/$', csrf_exempt(views.CreateOrRetrieveAllProducts.as_view())),
    url(r'^PostNewProduct/$', csrf_exempt(views.CreateOrRetrieveAllProducts.as_view())),
    url(r'^RetrieveProductById/(?P<pk>[0-9]+)/$', csrf_exempt(views.RetrieveOrUpdateOrDeleteProduct.as_view())),
    url(r'^UpdateProductById/(?P<pk>[0-9]+)/$', csrf_exempt(views.RetrieveOrUpdateOrDeleteProduct.as_view())),
    url(r'^DeleteProductById/(?P<pk>[0-9]+)/$', csrf_exempt(views.RetrieveOrUpdateOrDeleteProduct.as_view())),
    url(r'^GetAllCustomers/$', csrf_exempt(views.CreateOrRetrieveAllCustomers.as_view())),
    url(r'^PostNewCustomer/$', csrf_exempt(views.CreateOrRetrieveAllCustomers.as_view())),
    url(r'^RetrieveCustomerById/(?P<pk>[0-9]+)/$', csrf_exempt(views.RetrieveOrUpdateOrDeleteCustomer.as_view())),
    url(r'^UpdateCustomerById/(?P<pk>[0-9]+)/$', csrf_exempt(views.RetrieveOrUpdateOrDeleteCustomer.as_view())),
    url(r'^DeleteCustomerById/(?P<pk>[0-9]+)/$', csrf_exempt(views.RetrieveOrUpdateOrDeleteCustomer.as_view())),
    url(r'^GetAllTransactions/$', csrf_exempt(views.CreateOrRetrieveAllTransactions.as_view())),
    url(r'^PostNewTransaction/$', csrf_exempt(views.CreateOrRetrieveAllTransactions.as_view())),
    url(r'^RetrieveTransactionById/(?P<pk>[0-9]+)/$', csrf_exempt(views.RetrieveTransaction.as_view()))
]

urlpatterns = format_suffix_patterns(urlpatterns)
