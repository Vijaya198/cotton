from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import vendor_information
from django.utils import timezone
from django.db.models import Q
import time
from datetime import datetime
import pytz

# Create your views here.



def home(request):
    try:
        vendor_infos = vendor_information.objects.filter(~Q(status="Deleted"))

        #vendor_infos = vendor_information.objects.filter(status="")
        #for data in datas:
            #print("State:",data.company_state )
        context = {
            "vendors_infos": vendor_infos
        }
        return render(request, "vendor.html", context)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        print("except")

def vendors(request):
    try:
        data=vendor_information.objects.filter(status="")
        context ={
            "vendors_infos": data
        }
        return render(request, "vendor.html", context)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        print("except")

def add_vendor(request):
    try:
        return render(request, "vendoradd.html")
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        print("except")

def vendor_register(request):
    try:
        if (request.method=="POST"):
            print("request Method:", request.method)
            vendor_type =request.POST["vendortype"]
            company_name = request.POST["company_name"]
            company_door_street = request.POST["adddoor"]
            company_locality = request.POST["locality"]
            company_state = request.POST["state"]
            company_pincode = request.POST["pincode"]
            company_email = request.POST["company_email"]
            proprietorDirectorName = request.POST["proprietorDirectorName"]
            proprietorDirectorContact = request.POST["proprietorDirectorContact"]
            local_contact_name = request.POST["local_contact_name"]
            local_contact_no = request.POST["local_contact_no"]
            gstin = request.POST["gstin"]
            uin = request.POST["uin"]
            pan = request.POST["pan"]
            account_no = request.POST["accountno"]
            account_name = request.POST["accountname"]
            account_type = request.POST["accounttype"]
            bank_name = request.POST["bankname"]
            branch = request.POST["branch"]
            ifsc_code =request.POST["ifsc"]
            insurno = request.POST["insurno"]
            insurname = request.POST["insurname"]
            expiry_date = request.POST["expirdate1"]
            temp_date=timezone.now()
            created_date=str(datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S"))

            vendor_info = vendor_information.objects.create(account_id ="10011",company_name=company_name, vendor_type=vendor_type,
                                                         company_door_street=company_door_street,
                                                        company_locality=company_locality, company_state=company_state,
                                                        company_pincode = company_pincode,company_email=company_email,
                                                        proprietorDirectorName=proprietorDirectorName,
                                                        proprietorDirectorContact=proprietorDirectorContact, local_contact_name=local_contact_name,
                                                        local_contact_no=local_contact_no, gstin=gstin, uin=uin, pan=pan,
                                                        account_no=account_no, account_name=account_name, account_type=account_type,
                                                        bank_name=bank_name, branch=branch, ifsc_code=ifsc_code, insurance_no=insurno,
                                                        insurance_name=insurname,expiry_date = expiry_date,status="",
                                                        created_date=created_date
                                                        )
            vendor_info.save()
            print("success")
            print("Vendor_type", vendor_type)

            context = {
                "updated_infos": vendor_info
            }

            return render(request, "confirmform.html", context)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        print("except")

def edit_vendor_details(request):
    try:
        if (request.method=="POST"):
            vendor_id= request.POST["Edit"]
            print("vendor_id:", vendor_id)
            data=vendor_information.objects.filter(vendor_id=vendor_id)

            context={
                "vendors_infos": data
            }
            return render(request, "editVendorDetails.html",context)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        print("except")

def updateVendor(request):
    try:
        if (request.method=="POST"):

            vendor_id = request.POST["Submit"]
            print("vendor_id:", vendor_id)
            print("request Method:", request.method)

            vendor_type =request.POST["vendortype"]
            company_name = request.POST["company_name"]
            company_door_street = request.POST["adddoor"]
            company_locality = request.POST["locality"]
            company_state = request.POST["state"]
            company_pincode = request.POST["pincode"]
            company_email = request.POST["company_email"]
            proprietorDirectorName = request.POST["proprietorDirectorName"]
            proprietorDirectorContact = request.POST["proprietorDirectorContact"]
            local_contact_name = request.POST["local_contact_name"]
            local_contact_no = request.POST["local_contact_no"]
            gstin = request.POST["gstin"]
            uin = request.POST["uin"]
            pan = request.POST["pan"]
            account_no = request.POST["accountno"]
            account_name = request.POST["accountname"]
            account_type = request.POST["accounttype"]
            bank_name = request.POST["bankname"]
            branch = request.POST["branch"]
            ifsc_code =request.POST["ifsc"]
            insurno = request.POST["insurno"]
            insurname = request.POST["insurname"]
            expiry_date = request.POST["expirdate1"]
            updated_date=timezone.now()

            vendor_info = vendor_information.objects.filter(vendor_id=vendor_id).update(company_name=company_name, vendor_type=vendor_type,
                                                         company_door_street=company_door_street,
                                                        company_locality=company_locality, company_state=company_state,
                                                        company_pincode = company_pincode,company_email=company_email,
                                                        proprietorDirectorName=proprietorDirectorName,
                                                        proprietorDirectorContact=proprietorDirectorContact, local_contact_name=local_contact_name,
                                                        local_contact_no=local_contact_no, gstin=gstin, uin=uin, pan=pan,
                                                        account_no=account_no, account_name=account_name, account_type=account_type,
                                                        bank_name=bank_name, branch=branch, ifsc_code=ifsc_code, insurance_no=insurno,
                                                        insurance_name=insurname,expiry_date = expiry_date,status="",
                                                        updated_date=updated_date
                                                        )
            #vendor_info.save()
            print("Updated")
            print("Vendor_type", vendor_type)
            updated_info=vendor_information.objects.filter(vendor_id=vendor_id)
            context= {
                "updated_infos": updated_info
            }
            return render(request, "confirmform.html", context)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        print("except")


def traders(request):
    return render(request, "traders.html")

def confirm(request):
    return render(request, "confirmform.html")



def delete_vendor_details(request):
    try:
        print("hi")
        if (request.method=="POST"):
            vendor_id=request.POST["hidVendorId"]
            print("DELETE Vendor_id", vendor_id)
            #delete_vendor = vendor_information.objects.filter(vendor_id=vendor_id).update(status="Deleted")
            vendor_info = vendor_information.objects.filter(~Q(status="Deleted"))
            context ={
                "vendors_infos":vendor_info
            }
            return render(request, "vendor.html", context)
        '''
        else:
            vendor_info = vendor_information.objects.all
            context = {
                "vendors_infos": vendor_info
            }
            return render(request, "vendor.html")
        '''
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        print("except")
