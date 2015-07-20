from rest_framework import generics

from rest_framework import permissions

from api.serializers import *
from permissions import IsOwnerOrReadOnly


class RetrieveAllUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class CreateOrRetrieveAllProducts(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(sales_person=self.request.user)


permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
class RetrieveOrUpdateOrDeleteProduct(generics.RetrieveUpdateDestroyAPIView, permissions.IsAuthenticated):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
class CreateOrRetrieveAllCustomers(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        serializer.save(sales_person=self.request.user)


permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class RetrieveOrUpdateOrDeleteCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class CreateOrRetrieveAllTransactions(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        serializer.save(sales_person=self.request.user)


permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class RetrieveTransaction(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
