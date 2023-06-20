from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Product,Order
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import status
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
 
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'desc', 'price', 'amount']   
           
        def create(self, validated_data):
            user = self.context['user']
            validated_data['user'] = user
            return Order.objects.create(**validated_data,user=user)

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields =  ['amount', 'desc', 'price']
    def create(self, validated_data):
        # return Order.objects.create(**validated_data)
        user = self.context['user']
        return Order.objects.create(**validated_data,user=user)
    
class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        cart_items = request.data
        print(cart_items)
        serializer = CartItemSerializer(data=request.data,  context={'user': request.user},many=True)
        if serializer.is_valid():
            cart_items = serializer.save()
        #     # Process the cart items as needed
        #     # ...
            return Response("Cart items received and processed successfully.")
        else:
            return Response(serializer.errors, status=400)


# @api_view(['post'])
# @permission_classes([IsAuthenticated])
# def checkout(request): # actual order (buy)
#     cart_items = request.data
#     print(cart_items)
#     print(request.user)
#     serializer = OrderSerializer(data=request.data, many=True, context={'user': request.user})
#     if serializer.is_valid():
#         cart_items = serializer.save()
#     #     # Process the cart items as needed
#     #     # ...
#         return Response("Cart items received and processed successfully.")
#     else:
#         return Response(serializer.errors, status=400)
    
    # serializer = OrderSerializer(data=request.data, context={'user': request.user},many=True)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




class ProductViewSet(APIView):
    def get(self, request):
        my_model = Product.objects.all()
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

@api_view(['GET','post'])
def orders(request):
    all_orders=OrderSerializer(Order.objects.all(),many=True).data
    return Response ( all_orders)


def index(req):
    return HttpResponse('<h1>hello')


def about(req):
    return JsonResponse(f'about', safe=False)

def contact(req):
    return JsonResponse(f'contact', safe=False)