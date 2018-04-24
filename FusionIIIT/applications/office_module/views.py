from django.shortcuts import render 
from django.http import HttpResponse,HttpResponseRedirect
from .models import vendor,stock,apply_for_purchase,purchase_commitee
from cgi import escape
from io import BytesIO
from applications.globals.models import ExtraInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template
from xhtml2pdf import pisa

@login_required
def apply_purchase(request):

    # 
    # name=ExtraInfo.objects.get(user=user)  
    
    # user = request.user
    # user = User.objects.get(id=1).extrainfo
    user=request.user.extrainfo
    # user=ExtraInfo.objects.get(id=user)
    
    if request.method == 'POST':
        '''if "submit" in request.POST:'''
        item_name=request.POST.get('item_name')
        quantity=request.POST.get('quantity')
        expected_cost=int(request.POST.get('expected_cost'))
        
        if  expected_cost >=25000 and expected_cost <= 250000 :
            local_comm_mem1_id=request.POST.get('local_comm_mem1_id')
            local_comm_mem2_id=request.POST.get('local_comm_mem2_id')
            local_comm_mem3_id=request.POST.get('local_comm_mem3_id')

        nature_of_item1= 1 if request.POST.get('nature_of_item1') == 'on' else 0
        nature_of_item2= 1 if request.POST.get('nature_of_item2') == 'on' else 0
        
        # extra = ExtraInfo.objects.all()
        # extraInfo = ExtraInfo.objects.get(id=inspecting_authority_id)
        
        purpose=request.POST.get('purpose')
        # budgetary_head_id=request.POST.get('budgetary_head_id')       
        # inspecting_authority_id=request.POST.get('inspecting_authority_id')
        expected_purchase_date=request.POST.get('expected_purchase_date')
        # print(expected_purchase_date+"...........................")
        
    # xyz=apply_for_purchase(indentor_name=name,)
    # xyz.save()


        
        a = apply_for_purchase.objects.create(
                item_name=item_name,
                quantity=int(quantity),
                expected_cost=expected_cost,    
                nature_of_item1=nature_of_item1,
                nature_of_item2=nature_of_item2,
                purpose=purpose,
                # budgetary_head_id = budgetary_head_id,
                # inspecting_authority_id=inspecting_authority_id,
                expected_purchase_date= expected_purchase_date,        
                indentor_name=user,
                
        )
        a.save()
        if  expected_cost >=25000 and expected_cost <= 250000 :
            b = purchase_commitee.objects.create(
        
            local_comm_mem1_id=local_comm_mem1_id,
            local_comm_mem2_id=local_comm_mem2_id,
            local_comm_mem3_id=local_comm_mem3_id,                
            )
            b.save()

        
           

        return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html",{})
    else:
        return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html",{})

@login_required
def after_purchase(request):
    if request.method == 'POST':
        '''if "submit" in request.POST:'''
        file_no=request.POST.get('file_no')
        amount=request.POST.get('amount')
        invoice=request.POST.get('invoice')
        apply_for_purchase.objects.filter(id=file_no).update(amount=amount, invoice=invoice)  

        return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html",{})
    else:
        return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html",{})


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
        elif "purchase_search" in request.POST:
            pr = request.POST['file']
            phmatch = apply_for_purchase.objects.filter(Q(id=pr))
            return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html",{'phmatch':phmatch})    
        '''elif "delete_item" in request.POST:
            a = request.POST.getlist('box')
            for i in range(len(a)):
                k = stock.objects.get(id = a[i])
                k.delete()
            return HttpResponse("successflly deleted item")'''

    else:
        p=vendor.objects.all()
        q=stock.objects.all()
        ph=apply_for_purchase.objects.all()
    return render(request, "officeModule/officeOfPurchaseOfficer/officeOfPurchaseOfficer.html",{'p':p,'q':q,'ph':ph})

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
