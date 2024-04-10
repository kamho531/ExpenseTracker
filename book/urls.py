from django.urls import path
from . import views


urlpatterns = [
    path('listcategory/',views.listcategory, name='listcategory'),
    path('updatecategory/<int:pk>', views.updatecategory, name='updatecategory'),
    path('addcategory/', views.addcategory, name='addcategory'),
    path('deletecategory/<int:pk>', views.deletecategory, name='deletecategory'),
    path('addbook/', views.addbook, name="addbook"),
    path('updatebook/<str:pk>', views.updatebook, name="updatebook"),
    path('deletebook/<str:pk>', views.deletebook, name='deletebook'),    
    path('searchbook/', views.searchbook, name="searchbook"),
    path('searchbycategory/', views.searchbycategory, name='searchbycategory'),
    path('showexpense/', views.showexpenseView, name='showexpense'),
]