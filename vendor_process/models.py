from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime, date

from django.db.models import ForeignKey


def increment_vendor_number():
    last_vendor_information = vendor_information.objects.all().order_by('id').last()
    if not last_vendor_information:
        return 'VN-' + str(date.today().year) + str(date.today().month).zfill(2) +'-'+ '001'
    vendor_id = last_vendor_information.vendor_id
    vendor_int = int(vendor_id[10:13])
    new_vendor_int = vendor_int + 1
    new_vendor_id = 'VN-' + str(str(date.today().year)) + str(date.today().month).zfill(2) + '-' + str(new_vendor_int).zfill(3)
    return new_vendor_id

# Create your models here.
class vendor_information(models.Model):
    vendor_id = models.CharField(max_length=20, default=increment_vendor_number, editable=False)
    account_id = models.ForeignKey(User, db_constraint=False, db_column='account_id',on_delete=models.CASCADE)#account_id = models.IntegerField(default=0, null=True)

    company_nick_name = models.CharField(max_length=254)
    company_name_reg = models.CharField(max_length=254)
    door_street = models.CharField(max_length=254)
    locality = models.CharField(null=True, max_length=254)
    state = models.CharField( null=True,max_length=254)
    pincode = models.IntegerField()

    primary_email = models.EmailField()
    primary_contact_name = models.CharField(null=True, max_length=100)
    primary_contact_no = models.BigIntegerField(default=0, null=True)
    secondary_email = models.EmailField(null=True)
    secondary_contact_no = models.BigIntegerField(default=0, null=True)
    secondary_contact_name = models.CharField(null=True, max_length=254)
    gstin = models.CharField(null=True,max_length=15)
    uin = models.CharField(blank=True, null=True,max_length=15)

    insurance_no = models.CharField( blank=True, null=True, max_length=50)
    insurance_company = models.CharField(blank=True, null=True, max_length=254)
    expiry_date = models.DateField(blank=True, default=None, null=True)
    status = models.CharField(max_length=9,default=None, null=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(blank=True, default=None, null=True)

def increment_account_number():
    last_user_info = user_info.objects.all().order_by('id').last()
    if not user_info:
        new_account_id= str(date.today().year) + str(date.today().month).zfill(2) +str(date.today().day).zfill(2)+ '000'
        new_acc_id = int(new_account_id)

        return new_acc_id

    account_id = last_user_info.account_id
    account_int = int(account_id[8:11])
    new_account_int = account_int + 1
    new_account_id =  str(date.today().year) + str(date.today().month).zfill(2) + str(date.today().day).zfill(2)+str(new_account_int).zfill(3)
    new_acc_id= int(new_account_id)

    return new_acc_id

class user_info(models.Model):
    account_id = models.ForeignKey(User, db_constraint=False, db_column='account_id', on_delete=models.CASCADE)
    acc_holder_name=models.CharField(max_length=100)
    acc_holder_contact_no=models.IntegerField()
    status=models.CharField(default=None, max_length=9, null=True)
    created_date=models.DateTimeField()
    update_date=models.DateTimeField(default=None, blank=True, null=True)

class user_address(models.Model):
    account_id = models.ForeignKey(User, db_constraint=False, db_column='account_id', on_delete=models.CASCADE)
    entity_name = models.CharField(default=None, blank=True, null=True, max_length=100)
    email = models.EmailField()
    door_street = models.CharField(default=None, blank=True, null=True, max_length=50)
    locality = models.CharField(default=None, blank=True, null=True, max_length=50)
    state = models.CharField(default=None, blank=True, null=True, max_length=50)
    pincode = models.IntegerField(default=None, blank=True, null=True)
    contact_no = models.IntegerField(default=None, blank=True, null=True)
    gstin = models.CharField(default=None, blank=True, null=True, max_length=100)
    uin = models.CharField(default=None, blank=True, null=True, max_length=100)
    insurance_no = models.CharField(default=None, blank=True, null=True, max_length=100)
    insurance_name = models.CharField(default=None, blank=True, null=True, max_length=100)
    expiry_date = models.DateField(default=None, blank=True, null=True)
    addr_identity = models.CharField(max_length=15)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField (default=None, blank=True, null=True)

class state(models.Model):
    state = models.CharField(max_length = 254)

    class Meta:
        db_table="state"


'''
class vendor_information(models.Model):
    #vendor_id = models.CharField(primary_key = True, default=genMethod, editable = False, max_length=15)
    #vendor_id = models.CharField(primary_key=True, editable=False, max_length=12)
    vendor_id = models.CharField(max_length=20, default=increment_vendor_number, editable=False)
    account_id =models.IntegerField(default=None, blank=True, null=True)
    company_name=models.CharField(max_length=100)
    vendor_type=models.CharField(max_length=25)
    company_door_street=models.CharField(max_length=100)
    company_locality=models.CharField(max_length=50)
    company_state=models.CharField(max_length=50)
    company_pincode=models.IntegerField()
    company_email=models.EmailField()
    proprietorDirectorName=models.CharField(max_length=100)
    proprietorDirectorContact=models.BigIntegerField()
    local_contact_name = models.CharField(max_length=100)
    local_contact_no=models.BigIntegerField(default=None, blank=True, null =True)
    gstin=models.CharField(max_length=10)
    uin=models.CharField(max_length=10)
    pan=models.CharField(max_length=10)
    account_no=models.BigIntegerField()
    account_name=models.CharField(max_length=30)
    account_type=models.CharField(max_length=10)
    bank_name=models.CharField(max_length=15)
    branch=models.CharField(max_length=50)
    ifsc_code=models.CharField(max_length=11)
    insurance_no=models.CharField(max_length=30)
    insurance_name=models.CharField(max_length=30)
    expiry_date =models.DateField()
    status=models.CharField(max_length=9, null=True)
    created_date=models.DateTimeField()
    updated_date=models.DateTimeField(default=None, blank=True, null=True)


def save(self, **kwargs):
    if not self.vendor_id:
        tmzdat= "VN-"+timezone.now().strftime("%Y%m")+"-"
        max = vendor_information.objects.aggregate(vendor_id_max=Max ('vendor_id'))['vendor_id_max']
        self.id = "{}{:02d}".format(tmzdat, max if max is not None else 1)
        super.save(*kwargs)
        


class user_address(models.Model):
    account_id = models.IntegerField(default=None, blank=True, null=True)
    entity_name =models.CharField(default=None, blank=True, null=True, max_length=100)
    email =models.EmailField()
    door_street =models.CharField(default=None, blank=True, null=True, max_length=50)
    locality =models.CharField(default=None, blank=True, null=True, max_length=50)
    state =models.CharField(default=None, blank=True, null=True, max_length=50)
    pincode=models.IntegerField(default=None, blank=True, null=True)
    contact_no=models.IntegerField(default=None, blank=True, null=True)
    gstin = models.CharField(default=None, blank=True, null=True, max_length=100)
    uin = models.CharField(default=None, blank=True, null=True, max_length=100)
    pan = models.CharField(default=None, blank=True, null=True, max_length=100)

    insurance_no = models.CharField(default=None, blank=True, null=True, max_length=100)
    insurance_name = models.CharField(default=None, blank=True, null=True, max_length=100)
    expiry_date = models.DateField()
    addr_identity = models.CharField(max_length=15)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(default=None, blank=True, null=True)

'''




