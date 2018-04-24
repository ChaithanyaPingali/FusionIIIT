from django.conf.urls import url

from . import views 

app_name = 'office'

urlpatterns = [

    url(r'^officeOfDeanStudents/', views.officeOfDeanStudents, name='officeOfDeanStudents'),
    url(r'^officeOfPurchaseOfficer/',views.officeOfPurchaseOfficer, name ='officeOfPurchaseOfficer'),
    url(r'^apply_purchase/', views.apply_purchase, name='apply_purchase'),
    url(r'^after_purchase/', views.after_purchase, name='after_purchase'),
    url(r'^officeOfRegistrar/', views.officeOfRegistrar, name='officeOfRegistrar'),
    url(r'^officeOfDeanRSPC/', views.officeOfDeanRSPC, name='officeOfDeanRSPC'),
    url(r'^officeOfDeanPnD/', views.officeOfDeanPnD, name='officeOfDeanPnD'),
    url(r'^officeOfHOD/', views.officeOfHOD, name='officeOfHOD'),
    url(r'^genericModule/', views.genericModule, name='genericModule'),
    url(r'^deleteitem/(?P<id>[0-9]+)',views.delete_item, name='delete_item'),
    url(r'^deletevendor/(?P<id>[0-9]+)',views.delete_vendor, name='delete_vendor'),
    url(r'^editvendor/(?P<id>[0-9]+)',views.edit_vendor, name='edit_vendor'),
    url(r'^editvendor/office/officeOfPurchaseOfficer/edit/',views.edit,name='edit'),
    url(r'^edititem/(?P<id>[0-9]+)',views.edit_item, name='edit_item'),
    url(r'^edititem/office/officeOfPurchaseOfficer/edit1/',views.edit1,name='edit'),
]