from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseRedirect
from .models import vendor, stock
from cgi import escape
from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template
from xhtml2pdf import pisa


@login_required
def officeOfPurchaseOfficer(request):
    context={}
    if request.method == 'POST':
        if "submit" in request.POST:
            vendor_name=request.POST['vendor_name']
            vendor_item=request.POST['vendor_item']
            vendor_address=request.POST['vendor_address']
    
            vendor.objects.create(
                vendor_name=vendor_name,
                vendor_item=vendor_item,
                vendor_address=vendor_address,
            )
            return HttpResponse("successflly added vendor")

        elif "store" in request.POST:
            item_type=request.POST.get('item_type')
            item_name=request.POST.get('item_name')
            quantity=request.POST.get('qunatity')

            stock.objects.create(
                item_type=item_type,
                item_name=item_name,
                quantity=quantity,
            )
            return HttpResponse("successflly added item")
        elif "item_search" in request.POST:
            srch = request.POST['item_name']
            match = stock.objects.filter(Q(item_name__icontains=srch))
            return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html",{'match':match})
        elif "vendor_search" in request.POST:
            sr = request.POST['item']
            matchv = vendor.objects.filter(Q(vendor_item__icontains=sr))
            return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html",{'matchv':matchv})
        '''elif "delete_item" in request.POST:
            a = request.POST.getlist('box')
            for i in range(len(a)):
                k = stock.objects.get(id = a[i])
                k.delete()
            return HttpResponse("successflly deleted item")'''

    else:
        p=vendor.objects.all()
        q=stock.objects.all()
    return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html",{'p':p,'q':q})

def delete_item(request,id):
    #template = 'officemodule/officeOfPurchaseOfficer/manageStore_content1.html'
    print(">>>>>>>")
    print(id)
    item = get_object_or_404(stock,id=id)
    item.delete()
    return HttpResponse("Deleted successfully")

def delete_vendor(request,id):
    #template = 'officemodule/officeOfPurchaseOfficerr/manageStore_content1.html'
    print(">>>>>>>")
    print(id)
    ven = get_object_or_404(vendor,id=id)
    ven.delete()
    return HttpResponse("Deleted successfully")    

def edit_vendor(request,id):


    p= get_object_or_404(vendor,id=id)
    context={
        'p' : p
    }
    return render(request,"officeModule/officeOfPurchaseOfficer/edit.html",context)
    return HttpResponseRedirect('/office/officeOfPurchaseOfficer')

def edit(request):

    ID=request.POST.get('vendor_id')
    name=request.POST.get('vendor_name')
    item=request.POST.get('vendor_item')
    add=request.POST.get('vendor_address')
    d=vendor(id=ID,vendor_name=name,vendor_item=item,vendor_address=add)
    d.save()
    return HttpResponseRedirect('/office/officeOfPurchaseOfficer')

def edit_item(request,id):


    p= get_object_or_404(stock,id=id)
    context={
        'p' : p
    }
    return render(request,"officeModule/officeOfPurchaseOfficer/edit1.html",context)
    return HttpResponseRedirect('/office/officeOfPurchaseOfficer')

def edit1(request):

    ID=request.POST.get('item_id')
    name=request.POST.get('item_name')
    add=request.POST.get('quantity')
    d=stock(id=ID,item_name=name,quantity=add)
    d.save()
    return HttpResponseRedirect('/office/officeOfPurchaseOfficer')

'''def delete(request):
    if request.method == 'POST' :
        a = request.POST.getlist('box') 
        for i in range(len(a)) :
            if "delete_item" in request.POST :
                k = stock.objects.get(id = a[i])
                k.delete()
    
        return HttpRespons("officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html")'''
'''def create_vendor(request):
    if request.method == 'POST':
        vendor_name = request.POST['vendor_name']
        vendor_item = request.POST['vendor_item']
        vendor_address = request.POST['vendor_address']

        vendor.objects.create(
            vendor_name = vendor_name,
            vendor_item = vendor_item,
            vendor_address = vendor_address
        )

        return HttpResponse('')'''
    


def officeOfRegistrar(request):
    context = {}

    return render(request, "officeModule/officeOfRegistrar/officeOfRegistrar.html", context)


def officeOfDeanStudents(request):
    context = {}

    return render(request, "officeModule/officeOfRegistrar/officeOfDeanStudents.html", context)


def officeOfDeanRSPC(request):
    context = {}

    return render(request, "officeModule/officeOfDeanRSPC/officeOfDeanRSPC.html", context)


def officeOfDeanPnD(request):
    context = {}

    return render(request, "officeModule/officeOfDeanPnD/officeOfDeanPnD.html", context)

def officeOfHOD(request):
    context = {}

    return render(request, "officeModule/officeOfHOD/officeOfHOD.html", context)


def genericModule(request):
    context = {}

    return render(request, "officeModule/genericModule/genericModule.html", context)
