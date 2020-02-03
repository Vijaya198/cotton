from django.db import models
import datetime

def increment_vendor_number():
    last_vendor_information = vendor_information.objects.all().order_by('id').last()
    if not last_vendor_information:
        return 'VN-' + str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) +'-'+ '000'
    vendor_id = last_vendor_information.vendor_id
    vendor_int = int(vendor_id[10:13])
    new_vendor_int = vendor_int + 1
    new_vendor_id = 'VN-' + str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(2) + '-' + str(new_vendor_int).zfill(3)
    return new_vendor_id

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

'''
def save(self, **kwargs):
    if not self.vendor_id:
        tmzdat= "VN-"+timezone.now().strftime("%Y%m")+"-"
        max = vendor_information.objects.aggregate(vendor_id_max=Max ('vendor_id'))['vendor_id_max']
        self.id = "{}{:02d}".format(tmzdat, max if max is not None else 1)
        super.save(*kwargs)
'''
# Create your models here.







