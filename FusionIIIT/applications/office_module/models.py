
from django.db import models
import datetime

from applications.globals.models import ExtraInfo, Designation, DepartmentInfo, Staff, Faculty
# Create your models here.h



PURCHASE_STATUS = (

    ('0', "Pending"),
    ('1', "Approve"),
    ('2', "Items Ordered"),
    ('3', "Items Puchased"),
    ('4', "Items Delivered"),

)

APPROVE_TAG = (

    ('0', "Pending"),
    ('1', "Approve"),
)


PURCHASE_TYPE = (

    ('0', "Amount < 25000"),
    ('1', "25000<Amount<250000"),

    ('2', "250000<Amount < 2500000"),
    ('3', "Amount>2500000"),

)

NATURE_OF_ITEM1 = (
    ('0', "Non-consumable"),
    ('1', "Consumable"),

)
NATURE_OF_ITEM2 = (
    ('0', "Equipment"),
    ('1', "Machinery"),
    ('2', "Furniture"),
    ('3', "Fixture"),

)

ITEM_TYPE = (
    ('0', "Non-consumable"),
    ('1', "Consumable"),

)
class vendor(models.Model):
    vendor_name = models.CharField(max_length=100)
    vendor_address = models.CharField(max_length=200)
    vendor_item = models.CharField(max_length=200)

    class Meta:
        db_table = 'vendor'



class apply_for_purchase(models.Model):
    indentor_name = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE,related_name='indentor_name')
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    inspecting_authority = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE,related_name='inspecting_authority')
    expected_purchase_date = models.DateField()
    order_date = models.DateField(default=datetime.date.today)
    purchase_status = models.IntegerField(choices=PURCHASE_STATUS, default='0')
    purchase_officer = models.ForeignKey(Staff, on_delete=models.CASCADE)
    amount = models.IntegerField(default='0')
    purchase_date = models.DateField()

    registrar_approve_tag = models.IntegerField(choices=APPROVE_TAG, default='0')
    accounts_approve_tag = models.IntegerField(choices=APPROVE_TAG, default='0')

    purchase_type = models.IntegerField(choices=PURCHASE_TYPE, default='0')
    purpose = models.CharField(max_length=200)

    budgetary_head = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE,related_name='bud_head')
    invoice = models.FileField()
    nature_of_item1 = models.IntegerField(choices=NATURE_OF_ITEM1, default='0')
    nature_of_item2 = models.IntegerField(choices=NATURE_OF_ITEM2, default='0')

    item_name = models.CharField(max_length=100)
    expected_cost = models.IntegerField(default='0')
    quantity = models.IntegerField(default='0')

    class Meta:
        db_table = 'apply_for_purchase'

class stock(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default='0')

    item_type = models.IntegerField(choices=ITEM_TYPE, default='0')

    class Meta:
        db_table = 'stock'


class purchase_commitee(models.Model) :
    local_comm_mem1 = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE,related_name='local_comm_mem1')
    local_comm_mem2 = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE,related_name='local_comm_mem2')
    local_comm_mem3 = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE,related_name='local_comm_mem3')
    approve_mem1 = models.IntegerField(choices=APPROVE_TAG, default ='0')
    approve_mem2 = models.IntegerField(choices=APPROVE_TAG, default ='0')
    approve_mem3 = models.IntegerField(choices=APPROVE_TAG, default ='0')

    class Meta:
        db_table = 'purchase_commitee'


class quotations(models.Model) :
    quotation1 = models.FileField()
    quotation2 = models.FileField()
    quotation3 = models.FileField()

    class Meta:
        db_table = 'quotations'
