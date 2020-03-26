from django.db import models
from annoying.fields import AutoOneToOneField
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class trade_information(models.Model):
    #vendor_id = models.CharField(primary_key = True, default=genMethod, editable = False, max_length=15)
    bussiness_mode = models.CharField(max_length=30)
    conf_no = models.AutoField(primary_key=True, default=1)
    conf_date=models.DateTimeField()
    buyer_name=models.CharField(max_length=25)
    gstin_buyer = models.CharField(max_length=10)
    buyer_door_street=models.CharField(max_length=100)



    #buyer_locality=models.CharField(max_length=50)

    buyer_state=models.CharField(max_length=50)

    buyer_pincode=models.IntegerField()
    seller_name = models.CharField(max_length=25)
    gstin_seller = models.CharField(max_length=10)
    trader_name = models.CharField(max_length=50)
    trader_type = models.CharField(max_length=15)
    broker_name = models.CharField(max_length=50)

    broker_contact_no = models.BigIntegerField(default=None, blank=True, null=True)
    broker_email=models.EmailField()
    broker_commission_percent = models.BigIntegerField(default=None, blank=True, null=True)
    broker_commission_rupees = models.BigIntegerField(default=None, blank=True, null=True)
    station = models.CharField(max_length=25)
    state = models.CharField(max_length=50)
    hsn_code =models.IntegerField()
    variety=models.CharField(max_length=15)
    staple_buyer=models.IntegerField()
    staple_seller = models.IntegerField()
    mic_buyer=models.IntegerField()
    mic_seller = models.IntegerField()
    grade=models.CharField(max_length=15)
    gtex_buyer = models.IntegerField(default=None, blank=True)
    gtex_seller = models.IntegerField(default=None, blank=True)
    gpt = models.IntegerField(blank=True)
    moist_buyer = models.IntegerField()
    moist_seller = models.IntegerField()
    trash_buyer = models.IntegerField()
    trash_seller = models.IntegerField()
    bales_nos=models.IntegerField()
    truck_nos=models.IntegerField()
    price=models.IntegerField()
    delivery_terms=models.CharField(max_length=10)
    gst=models.IntegerField()

    dispatch_terms=models.CharField(max_length=30)
    payment_terms=models.CharField(max_length=50)
    first_payment=models.IntegerField(blank=True)
    first_payment_days = models.IntegerField(blank=True)
    second_payment = models.IntegerField(blank=True)
    second_payment_days = models.IntegerField(blank=True)
    dhara=models.CharField(max_length=50, blank=True)
    gst_payment=models.CharField(max_length=50)
    interest_late_payment=models.IntegerField()
    weighment_terms=models.CharField(max_length=30)
    passing_terms = models.CharField(max_length=30)
    transit_insurance_details=models.CharField(max_length=100)
    unloading_contact_no = models.BigIntegerField(default=None, blank=True, null=True)
    weighbridge_contact_no = models.BigIntegerField(default=None, blank=True, null=True)
    notes=models.CharField(max_length=500)

class VendorProcessVendorInformation(models.Model):
    vendor_id = models.CharField(max_length=20)
    account_id = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=100)
    vendor_type = models.CharField(max_length=25)
    company_door_street = models.CharField(max_length=100)
    company_locality = models.CharField(max_length=50)
    company_state = models.CharField(max_length=50)
    company_pincode = models.IntegerField()
    company_email = models.CharField(max_length=254)
    proprietordirectorname = models.CharField(db_column='proprietorDirectorName', max_length=100)  # Field name made lowercase.
    proprietordirectorcontact = models.BigIntegerField(db_column='proprietorDirectorContact')  # Field name made lowercase.
    local_contact_name = models.CharField(max_length=100)
    local_contact_no = models.BigIntegerField(blank=True, null=True)
    gstin = models.CharField(max_length=10)
    uin = models.CharField(max_length=10)
    pan = models.CharField(max_length=10)
    account_no = models.BigIntegerField()
    account_name = models.CharField(max_length=30)
    account_type = models.CharField(max_length=10)
    bank_name = models.CharField(max_length=15)
    branch = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=11)
    insurance_no = models.CharField(max_length=30)
    insurance_name = models.CharField(max_length=30)
    expiry_date = models.DateField()
    status = models.CharField(max_length=9, blank=True, null=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_process_vendor_information'



