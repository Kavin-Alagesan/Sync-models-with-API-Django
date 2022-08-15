from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.home),
    path('generics/',views.DetailsListCreateAPI.as_view()),
    path('generics_edit/<int:pk>/',views.DetailsListViewUpdateDelete.as_view()),
]
