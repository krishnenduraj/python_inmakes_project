from django.conf.urls.static import static
from django.urls import path

from todoproject import settings
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    #path('details',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdate.as_view(),name='cbvupdate')

]




