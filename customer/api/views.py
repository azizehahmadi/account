from customer.models import Customer
from customer.api.serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

class CustomerListAV(APIView):
    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetailAV(APIView):

    def get(self, request, slug):
        try:
            customer = Customer.objects.get(pk=slug)
        except customer.DoesNotExist:
            return Response({'error': 'customer not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, slug):
        customer = Customer.objects.get(pk=slug)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, slug):
        customer= Customer.objects.get(pk=slug)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



