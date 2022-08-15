from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Details
from rest_framework import generics
from .serializers import DetailsSerializer

# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        gender=request.POST['gender']
        dob=request.POST['dob']
        qualification=request.POST['qualification']
        contact=request.POST['contact']
        address=request.POST['address']
        image=request.POST['image']
        save_in_db=Details.objects.create(name=name,gender=gender,dob=dob,qualification=qualification,contact=contact,address=address,image=image)
        save_in_db.save()
        messages.success(request, ("Details added successfully!"))
        return render(request,'home.html')
    else:
        return render(request,'home.html')

class DetailsListCreateAPI(generics.ListCreateAPIView):
    queryset=Details.objects.all()
    serializer_class=DetailsSerializer

class DetailsListViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Details.objects.all()
    serializer_class=DetailsSerializer






