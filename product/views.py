from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSelializer
from rest_framework.views import APIView

#This is demonstration of Function based/decorators view(using @api_view)
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def product(request):
    # To get the data/view the data from database to the client
    if request.method == 'GET':
        objs = Product.objects.all()
        serializer = ProductSelializer(objs, many= True)
        return Response(serializer.data)
    
    # To send the data/add the data to database
    elif request.method == 'POST':
        data =request.data  
        serializer = ProductSelializer(data=data)  
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        return Response(serializer.error)
    
    # we can update all the data 
    # and we need to pass all data /fields value
    # whether we want to update or not
    elif request.method == 'PUT':
        data =request.data  
        obj = Product.objects.get(id=data['id'])
        serializer = ProductSelializer(obj,data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        return Response(serializer.error)
    
    #support partial update when we want to update any 
    # particular field data  
    elif request.method == 'PATCH':
        data =request.data  
        obj = Product.objects.get(id=data['id'])
        serializer = ProductSelializer(obj,data=data, partial= True)  
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        return Response(serializer.error)
    
    # To delete the data for the particular id
    elif request.method == 'DELETE':
        data =request.data 
        tmpId=data['id']
        obj = Product.objects.get(id=data['id'])
        obj.delete()
        return Response({'productid':tmpId,'status':'succesfully delete' })
    
#This is demonstration of class based view(using APIview)
class ProductApi(APIView):
    
    # To get the data/view the data from database to the client
    def get(self, request):
         objs = Product.objects.all()
         serializer = ProductSelializer(objs, many= True)
         return Response(serializer.data)
     
    # To send the data/add the data to database
    def post(self, request):
        data =request.data  
        serializer = ProductSelializer(data=data)  
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        return Response(serializer.error)
    
    # we can update all the data 
    # and we need to pass all data /fields value
    # whether we want to update or not
    def put(self, request):
        data =request.data  
        obj = Product.objects.get(id=data['id'])
        serializer = ProductSelializer(obj,data=data) 
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        return Response(serializer.error)
    
    #support partial update when we want to update any 
    # particular field data  
    def patch(self, request):
        data =request.data  
        obj = Product.objects.get(id=data['id'])
        serializer = ProductSelializer(obj,data=data, partial= True)  
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data)
        return Response(serializer.error)
    # To delete the data for the particular id
    def delete(self, request):
        data =request.data 
        tmpId=data['id']
        obj = Product.objects.get(id=data['id'])
        obj.delete()
        return Response({'productid':tmpId,'status':'succesfully delete' })



