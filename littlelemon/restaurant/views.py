from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

#def index(request):
 #   return render(request, 'index.html', {})

# Create your views here.
#class bookingview(APIView):

 #   def get(self, request):
  #      items = Booking.objects.all()
   #     serializer = BookingSerializer(items, many=True)
    #    return Response(serializer.data)
    
   # def post(self, request):
    #    serializer = BookingSerializer(data=request.data)

     #   if serializer.is_valid():
      #      serializer.save()
       #     return Response({'status': 'success', 'data': serializer.data})

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
