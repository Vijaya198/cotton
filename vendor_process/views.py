
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from .models import vendor_information, user_info, user_address, state
from django.utils import timezone
from django.db import IntegrityError, InterfaceError
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.exceptions import ValidationError
import logging
from datetime import datetime, date
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
from django.db.utils import OperationalError
from django.contrib.auth.models import User

from django.http import JsonResponse

# Create your views here.



def home(request):
    try:
        vendor_infos = vendor_information.objects.filter(~Q(status="Deleted"))


        context = {

            "vendors_infos": vendor_infos
        }
        return render(request, "vendor.html", context)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError,TypeError, KeyError,IndexError, ValueError,AttributeError, OverflowError, ValidationError, IntegrityError, InterfaceError) as e:
        print("Exception: ", e)
        return HttpResponse(e)

def edit_account1(request, newContext={}):

    try:
        print("edit_account1", request.session.get("id"))
        all_states = state.objects.all()
        usr_id = request.session.get("id")
        user_informations = user_info.objects.filter(account_id=usr_id)
        user_addr_p  =  user_address.objects.filter(account_id  = usr_id, addr_identity = "primary")
        user_addr_s1 = user_address.objects.filter(account_id = usr_id, addr_identity =  "secondary1")
        user_addr_s2 = user_address.objects.filter(account_id = usr_id, addr_identity = "secondary2")
        user_p_mail = user_address.objects.filter(account_id=usr_id, addr_identity="primary").values('email')
        user_s1_mail = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1").values('email')
        user_s2_mail = user_address.objects.filter(account_id=usr_id, addr_identity="secondary2").values('email')
        if (user_p_mail):
            user_mail1 = user_p_mail[0]["email"]
        else:
            user_mail1 = ""
        if (user_s1_mail):
            user_mail2 = user_s1_mail[0]["email"]
        else:
            user_mail2 = ""
        if (user_s2_mail):
            user_mail3=user_s2_mail[0]["email"]
        else:
            user_mail3 = ""
        if (not user_informations):
            user_informations="0"
        if (not user_addr_p):
            user_addr_p ="0"
            print("primary",user_addr_p)
        if (not user_addr_s1):
            user_addr_s1 ="0"
        if (not user_addr_s2):
            user_addr_s2 ="0"

        context = {

            "user_informations": user_informations,
            "user_addr_ps": user_addr_p,
            "user_addr_s1s": user_addr_s1,
            "user_addr_s2s": user_addr_s2,
            "user_p_mail": user_mail1,
            "user_s1_mail": user_mail2,
            "user_s2_mail": user_mail3,
            "all_states":all_states


        }
        context.update(newContext)
        return render(request, "editaccount_company.html", context)
    except (ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, TypeError,KeyError,IndexError,AttributeError, ValueError, OverflowError, ValidationError, IntegrityError, InterfaceError) as e:
        print("except")
        return HttpResponse(e)


def edit_account2(request, newContext={}):
    try:
        print("edit_account2", request.session.get("id"))
        all_states = state.objects.all()
        usr_id = request.session.get("id")
        user_informations = user_info.objects.filter(account_id=usr_id)
        user_addr_p = user_address.objects.filter(account_id=usr_id, addr_identity="primary")
        user_addr_s1 = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1")
        user_addr_s2 = user_address.objects.filter(account_id=usr_id, addr_identity="secondary2")
        user_p_mail = user_address.objects.filter(account_id=usr_id, addr_identity="primary").values('email')
        user_s1_mail = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1").values('email')
        user_s2_mail = user_address.objects.filter(account_id=usr_id, addr_identity="secondary2").values('email')

        if (user_p_mail):
            user_mail1 = user_p_mail[0]["email"]
        else:
            user_mail1 = ""
        if (user_s1_mail):
            user_mail2 = user_s1_mail[0]["email"]
        else:
            user_mail2 = ""
        if (user_s2_mail):
            user_mail3=user_s2_mail[0]["email"]
        else:
            user_mail3 = ""

        if (not user_informations):
            user_informations="0"
        if (not user_addr_p):
            user_addr_p ="0"
            print("primary",user_addr_p)
        if (not user_addr_s1):
            user_addr_s1 ="0"
        if (not user_addr_s2):
            user_addr_s2 ="0"

        context = {

            "user_informations": user_informations,
            "user_addr_ps":user_addr_p,
            "user_addr_s1s": user_addr_s1,
            "user_addr_s2s": user_addr_s2,
            "user_p_mail": user_mail1,
            "user_s1_mail": user_mail2,
            "user_s2_mail": user_mail3,
            "all_states":all_states
        }
        context.update(newContext)
        return render(request, "editaccount_company2.html", context)
    except (OperationalError,ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, TypeError, KeyError,
            IndexError,AttributeError,ValueError, OverflowError, ValidationError, IntegrityError, InterfaceError) as e:
        print("except")

def edit_account3(request, newContext={}):
    try:
        print("edit_account3", request.session.get("id"))
        all_states = state.objects.all()
        usr_id = request.session.get("id")
        user_informations = user_info.objects.filter(account_id=usr_id)
        user_addr_p=user_address.objects.filter(account_id=usr_id, addr_identity="primary")
        user_addr_s1 = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1")
        user_addr_s2 = user_address.objects.filter(account_id=usr_id, addr_identity="secondary2")

        user_p_mail = user_address.objects.filter(account_id=usr_id, addr_identity="primary").values('email')
        user_s1_mail = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1").values('email')
        user_s2_mail = user_address.objects.filter(account_id=usr_id, addr_identity="secondary2").values('email')

        if (user_p_mail):
            user_mail1 = user_p_mail[0]["email"]
        else:
            user_mail1 = ""
        if (user_s1_mail):
            user_mail2 = user_s1_mail[0]["email"]
        else:
            user_mail2 = ""
        if (user_s2_mail):
            user_mail3=user_s2_mail[0]["email"]
        else:
            user_mail3 = ""

        print(user_p_mail)

        if (not user_informations):
            user_informations="0"
        if (not user_addr_p):
            user_addr_p ="0"
            print("primary",user_addr_p)
        if (not user_addr_s1):
            user_addr_s1 ="0"
        if (not user_addr_s2):
            user_addr_s2 ="0"
        context = {

            "user_informations": user_informations,
            "user_addr_ps":user_addr_p,
            "user_addr_s1s": user_addr_s1,
            "user_addr_s2s": user_addr_s2,
            "user_p_mail": user_mail1,
            "user_s1_mail": user_mail2,
            "user_s2_mail": user_mail3,
            "all_states" : all_states

        }
        context.update(newContext)
        return render(request, "editaccount_company3.html", context)
    except (OperationalError,ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError,
            TypeError,KeyError,IndexError, AttributeError,ValueError, OverflowError,
            ValidationError, IntegrityError, InterfaceError) as e:
        print("except")
        return HttpResponse(e)

def edit_account_contact(request, newContext={}):
    try:
        print("edit_account_contact", request.session.get("id"))

        usr_id = request.session.get("id")
        user_informations = user_info.objects.filter(account_id=usr_id)
        user_addr_p = user_address.objects.filter(account_id=usr_id, addr_identity="primary")
        user_addr_s1 = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1")
        user_addr_s2 = user_address.objects.filter(account_id=usr_id, addr_identity="secondary2")
        user_p_mail = user_address.objects.filter(account_id=usr_id, addr_identity="primary").values('email')
        user_s1_mail = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1").values('email')
        user_s2_mail = user_address.objects.filter(account_id=usr_id, addr_identity="secondary2").values('email')

        if (user_p_mail):
            user_mail1 = user_p_mail[0]["email"]
        else:
            user_mail1 = ""
        if (user_s1_mail):
            user_mail2 = user_s1_mail[0]["email"]
        else:
            user_mail2 = ""
        if (user_s2_mail):
            user_mail3=user_s2_mail[0]["email"]
        else:
            user_mail3 = ""

        if (not user_informations):
            user_informations="0"
        if (not user_addr_p):
            user_addr_p ="0"
            print("primary",user_addr_p)
        if (not user_addr_s1):
            user_addr_s1 ="0"
        if (not user_addr_s2):
            user_addr_s2 ="0"

        context = {

            "user_informations": user_informations,
            "user_addr_ps": user_addr_p,
            "user_addr_s1s": user_addr_s1,
            "user_addr_s2s": user_addr_s2,
            "user_p_mail": user_mail1,
            "user_s1_mail": user_mail2,
            "user_s2_mail": user_mail3

        }
        context.update(newContext)
        return render(request, "editaccount_contact.html", context)
    except (OperationalError,ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError,TypeError,KeyError,
            IndexError, AttributeError, ValueError, OverflowError, ValidationError, IntegrityError, InterfaceError) as e:
        print("exception: ", e)
        return HttpResponse(e)

def account_mail(request):
    try:
        print("account_mail", request.session.get("id"))
        usr_id = request.session.get("id")
        user_informations= user_info.objects.filter(account_id=usr_id)
        user_addr_p = user_address.objects.filter(account_id=usr_id, addr_identity="primary")
        user_addr_s1 = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1")
        user_addr_s2 = user_address.objects.filter(account_id=usr_id, addr_identity="secondary2")

        user_p_mail = user_address.objects.filter(account_id=usr_id, addr_identity="primary").values('email')
        user_s1_mail = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1").values('email')
        user_s2_mail = user_address.objects.filter(account_id=usr_id, addr_identity="secondary2").values('email')

        if (user_p_mail):
            user_mail1 = user_p_mail[0]["email"]
        else:
            user_mail1 = ""
        if (user_s1_mail):
            user_mail2 = user_s1_mail[0]["email"]
        else:
            user_mail2 = ""
        if (user_s2_mail):
            user_mail3=user_s2_mail[0]["email"]
        else:
            user_mail3 = ""

        if (not user_informations):
            user_informations="0"
        if (not user_addr_p):
            user_addr_p ="0"
            print("primary",user_addr_p)
        if (not user_addr_s1):
            user_addr_s1 ="0"
        if (not user_addr_s2):
            user_addr_s2 ="0"

        context = {

            "user_informations": user_informations,
            "user_addr_ps": user_addr_p,
            "user_addr_s1s": user_addr_s1,
            "user_addr_s2s": user_addr_s2,
            "user_p_mail": user_mail1,
            "user_s1_mail": user_mail2,
            "user_s2_mail": user_mail3

        }
        return render(request, "account_mail.html", context)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError,TypeError,
            KeyError,IndexError, AttributeError, ValueError, OverflowError, ValidationError, IntegrityError, InterfaceError) as e:
        print("except")
        return HttpResponse(e)

def accountinfo(request):
    try:
        print("accountinfo", request.session.get("id"))

        usr_id = request.session.get("id")
        user_informations= user_info.objects.filter(account_id=usr_id)
        user_addr_p = user_address.objects.filter(account_id=usr_id, addr_identity="primary")
        user_addr_s1 = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1")
        user_addr_s2 = user_address.objects.filter(account_id=usr_id, addr_identity="secondary2")

        user_p_mail = user_address.objects.filter(account_id=usr_id, addr_identity="primary").values('email')
        user_s1_mail = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1").values('email')
        user_s2_mail = user_address.objects.filter(account_id=usr_id, addr_identity="secondary2").values('email')

        if (user_p_mail):
            user_mail1 = user_p_mail[0]["email"]
        else:
            user_mail1 = ""
        if (user_s1_mail):
            user_mail2 = user_s1_mail[0]["email"]
        else:
            user_mail2 = ""
        if (user_s2_mail):
            user_mail3=user_s2_mail[0]["email"]
        else:
            user_mail3 = ""

        if (not user_informations):
            user_informations="0"
        if (not user_addr_p):
            user_addr_p ="0"
            print("primary",user_addr_p)
        if (not user_addr_s1):
            user_addr_s1 ="0"
        if (not user_addr_s2):
            user_addr_s2 ="0"
        context = {

            "user_informations": user_informations,
            "user_addr_ps": user_addr_p,
            "user_addr_s1s": user_addr_s1,
            "user_addr_s2s": user_addr_s2,
            "user_p_mail": user_mail1,
            "user_s1_mail": user_mail2,
            "user_s2_mail": user_mail3

        }
        return render(request, "accountinfo.html", context)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError,TypeError,
            KeyError,IndexError, AttributeError, ValueError, OverflowError, ValidationError, IntegrityError, InterfaceError) as e:
        print("except")
        return HttpResponse(e)


def vendors(request):

    try:
        print("Id in Vendors ", request.session.get("id"))

        usr_id = request.session.get("id")
        data = vendor_information.objects.filter(account_id=usr_id).filter(~Q(status="Deleted"))

        context ={
            "vendors_infos": data,

        }
        return render(request, "vendor.html", context)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError,TypeError, KeyError,
            IndexError,AttributeError,ValueError, OverflowError, ValidationError, IntegrityError, InterfaceError) as e:
        print("except")
        return HttpResponse(e)

def add_vendor(request):
    try:
        print("SESSION_ID", request.session.get("id"))
        print("session_key:Vendor", request.session.session_key)
        all_states = state.objects.all()
        #we have to change
        #vendor_infos = vendor_information.objects.filter(vendor_id="VN-202001-005")
        #user_account_id = request.session.user.account_id
        #user_id = request.session.user.id
        #request.session.user=User.objects.filter(account_id=user_account_id).first()
        #print("user_account_id",user_account_id, user_id)
        context={
            "all_states":all_states
        }
        return render(request, "vendoradd5.html", context)
    except (OperationalError,ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError,TypeError,KeyError,IndexError,
            AttributeError,ValueError, OverflowError, ValidationError, IntegrityError, InterfaceError) as e:
        print("Exception", e)
        return HttpResponse(e)

def valid_entity_locality(request):
    try:
        print("edit_account_contact", request.session.get("id"))
        usr_id = request.session.get("id")
        entity_name1 = request.GET.get('entity_name', None)
        locality = request.GET.get('locality', None)
        print("vendor_id", locality)
        entity_names= user_address.objects.annotate(
                entity_name_lower=Lower("entity_name")).filter(account_id=usr_id)
        locations = user_address.objects.annotate(
            locality_lower=Lower("locality")).filter(account_id=usr_id)
        print("hello")
        duplicate_entity_flag = False
        duplicate_locality_flag = False
        for entity_name in entity_names:
            if (entity_name.entity_name_lower == entity_name1.lower()):
                duplicate_entity_flag = True
        for location in locations:
            if (location.locality_lower == locality.lower()):
                duplicate_locality_flag = True
        if (duplicate_entity_flag):
            if (duplicate_locality_flag):
                duplicate_flag = True
            else:
                duplicate_flag = False
        data = {
            "duplicate_flag": duplicate_flag
        }
        return JsonResponse(data)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError,TypeError,KeyError,IndexError,
            AttributeError, ValueError, OverflowError, ValidationError, IntegrityError, InterfaceError) as e:
        print("Exception:" , e)
        return HttpResponse(e)

def valid_company_nick_name(request):
    try:
        company_nick_name = request.GET.get('company_nick_name', None)
        vendor_id=request.GET.get('vendor_id', None)
        print("vendor_id", vendor_id)
        if(vendor_id == ""):
            company_nicks = vendor_information.objects.annotate(
                    company_nick_name_lower=Lower("company_nick_name")).filter(~Q(status="Deleted"))
        else:
            print("hello:", vendor_id)
            company_nicks = vendor_information.objects.annotate(
                company_nick_name_lower=Lower("company_nick_name")).filter(~Q(status="Deleted"), ~Q(vendor_id=vendor_id))

        print("hello")
        duplicate_flag = False
        for company_nick in company_nicks:
            if (company_nick.company_nick_name_lower == company_nick_name.lower()):
                print(company_nick.company_nick_name_lower , "   ",company_nick_name.lower() )
                duplicate_flag = True
        print("local variable:", company_nick_name.lower())

        data = {
            "duplicate_flag": duplicate_flag
        }
        return JsonResponse(data)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError,TypeError,KeyError,IndexError,
            AttributeError, ValueError, OverflowError, ValidationError, IntegrityError, InterfaceError) as e:
        print("Exception:" , e)
        return HttpResponse(e)


def vendor_register(request):
    try:
        print("vendor_register",request.session.get("id"))
        all_states = state.objects.all()
        usr_id = request.session.get("id")
        acc_usr = User.objects.filter(id=usr_id).first()
        if (request.method=="POST"):
            print("request Method:", request.method)
            company_nick_name = request.POST["company_nick_name"]
            company_name_reg = request.POST["company_name_reg"]
            print("vendor_register", company_nick_name)
            door_street = request.POST["adddoor"]
            locality = request.POST["locality"]
            state1 = request.POST["state"]
            pincode = request.POST["pincode"]
            primary_contact_no = request.POST["primary_contact_no"]
            if (primary_contact_no == ""):
                primary_contact_no =None
            primary_contact_name = request.POST["primary_contact_name"]
            primary_email = request.POST["primary_email"]
            secondary_contact_name = request.POST["contact_name2"]
            secondary_contact_no = request.POST["secondary_contact_no"]
            if (secondary_contact_no == ""):
                secondary_contact_no =None
            secondary_email = request.POST["secondary_email"]
            gstin = request.POST["gstin"]
            uin = request.POST["uin"]
            insurno = request.POST["insurno"]
            insurcompany = request.POST["insurcompany"]

            expiry_temp_date = request.POST["expirydate"]
            if (expiry_temp_date == ""):
                expiry_date=None
            else:
                print(expiry_temp_date)
                #if (expiry_temp_date.split('/')[0]):
                    #if ()
                temp_date=datetime.strptime(expiry_temp_date, '%m/%d/%Y')
                print(temp_date)
                expiry_date =temp_date.strftime('%Y-%m-%d')
            #temp_date=timezone.now()
            created_date=str(datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M"))
            print("Secondary_name: ", secondary_contact_name, secondary_email)
            print(locality)

            #avoid duplication of company_nick_name in submission
            duplicate_flag = False
            company_nicks = vendor_information.objects.annotate(
                company_nick_name_lower=Lower("company_nick_name")).filter(~Q(status="Deleted"))
            for company_nick in company_nicks:
                if (company_nick.company_nick_name_lower == company_nick_name.lower()):
                    #print(company_nick.company_nick_name_lower, "   ", company_nick_name.lower())
                    duplicate_flag = True
            print("local variable:", company_nick_name.lower(), duplicate_flag)

            if (duplicate_flag):
                vendors_infos = {
                    'company_nick_name': company_nick_name, 'company_name_reg': company_name_reg,
                    'door_street': door_street,
                    'locality': locality, 'state': state, 'pincode': pincode,
                    'primary_contact_name': primary_contact_name,
                    'primary_contact_no': primary_contact_no, 'primary_email': primary_email,
                    'secondary_contact_name': secondary_contact_name, 'secondary_contact_no': secondary_contact_no,
                    'secondary_email': secondary_email, 'gstin': gstin, 'uin': uin, 'insurance_no': insurno,
                    'insurance_company': insurcompany, 'expiry_date': expiry_date
                }
                context = {
                    'vendors_infos': vendors_infos,
                    'display_messages': "Company Nick Name is already available. Pls give unique one",
                    'all_states':all_states
                }
                return render(request, 'duplicatevendoradd.html', context)
            else:
                vendor_info = vendor_information.objects.create(account_id=acc_usr, company_nick_name=company_nick_name,
                                                                company_name_reg=company_name_reg,
                                                                door_street=door_street,
                                                                locality=locality, state=state1,
                                                                pincode=pincode,
                                                                primary_contact_name=primary_contact_name,
                                                                primary_contact_no=primary_contact_no,
                                                                primary_email=primary_email,
                                                                secondary_contact_name=secondary_contact_name,
                                                                secondary_contact_no=secondary_contact_no,
                                                                secondary_email=secondary_email, gstin=gstin, uin=uin,
                                                                insurance_no=insurno,
                                                                insurance_company=insurcompany, expiry_date=expiry_date,
                                                                status="",
                                                                created_date=created_date)
                vendor_info.save()
                print("success")
                display_messages = "Your Information is created Successfully"
                context = {
                    "vendor_id": "CS Vendor ID: " + vendor_info.vendor_id,
                    "created_updated_date": "created at " + created_date,
                    "display_messages": display_messages
                }
                return render(request, "successform.html", context)

    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError,TypeError, KeyError,IndexError,
            AttributeError, ValueError, OverflowError, ValidationError, IntegrityError, InterfaceError) as e:
        print("Got this Exception:-  ", e)
        return HttpResponse(e)

def edit_vendor_details(request):
    try:
        all_states = state.objects.all()
        if (request.method=="POST"):
            vendor_id= request.POST["Edit"]
            print("vendor_id:", vendor_id)
            data=vendor_information.objects.filter(vendor_id=vendor_id)

            context={

                "vendors_infos": data,
                "all_states":all_states
            }
            return render(request, "editvendorinfo.html",context)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, TypeError,KeyError,IndexError, AttributeError, ValueError, OverflowError, User.DoesNotExist, ValidationError, IntegrityError, InterfaceError) as e:
        print("Exception:", e)
        return HttpResponse(e)

#rough use
def edit_contactaccount(request):
    try:
        print("edit_contactaccount", request.session.get("id"))

        usr_id=request.session.get("id")
        acc_usr = User.objects.filter(id=usr_id).first()
        print("user:", acc_usr)
        if (request.method == "POST"):
            account_holder_name = request.POST["account_holder_name"]
            account_contact_no= request.POST["account_contact_no"]
            if(account_contact_no == ""):
                account_contact_no = None
            created_date = str(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M"))
            user_informo =user_info.objects.filter(account_id=usr_id)
            '''
            if (account_holder_name ==  ""):
                context = {
                    'acc_holder_empty_flag': True
                }
                response = edit_account_contact(request, context)
                return response
            '''
            if (not user_informo):
                print("not user_informo")
                user_information = user_info.objects.create(account_id=acc_usr, acc_holder_name=account_holder_name,
                                                            acc_holder_contact_no=account_contact_no, status="",
                                                            created_date=created_date)
                user_information.save()
                print("success")
                display_messages = "Your Information is created Successfully."
                context = {

                    "display_messages": display_messages,

                }
            else:
                user_information= user_info.objects.filter(account_id=usr_id).update(acc_holder_name=account_holder_name, acc_holder_contact_no = account_contact_no, status="", update_date=created_date)

                print("Updated success")
                #updated_infos = vendor_information.objects.filter(vendor_id=vendor_id)
                display_messages = "Your Information is updated Successfully."
                context = {

                "display_messages": display_messages,

                }
        return render(request, "accountsuccessform.html", context)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, TypeError, KeyError,IndexError, AttributeError, ValueError, OverflowError, User.DoesNotExist, ValidationError, IntegrityError, InterfaceError) as e:
        print("Except", e)

def edit_account1info(request):
    try:
        print("edit_account1info", request.session.get("id"))
        usr_id = request.session.get("id")

        acc_usr = User.objects.filter(id=usr_id).first()
        if (request.method == "POST"):
            entity_name1 = request.POST["entity_name1"]
            entity_mail1 = request.POST["entity_mail1"]
            entity_contact_no1 = request.POST["entity_contact_no1"]
            if (entity_contact_no1 == ""):
               entity_contact_no1 =None
            entity_adddoor1 = request.POST["entity_adddoor1"]
            entity_locality1 = request.POST["entity_locality1"]
            entity_state1 = request.POST["entity_state1"]
            if (entity_state1==""):
                entity_state1 = None
            entity_pincode1= request.POST["entity_pincode1"]
            if (entity_pincode1 == ""):
               entity_pincode1 =None
            entity_gstin1 = request.POST["entity_gstin1"]
            entity_uin1= request.POST["entity_uin1"]
            entity_insur_company1 = request.POST["entity_insur_company1"]
            entity_insur_no1 = request.POST["entity_insur_no1"]
            #if (entity_insur_no1 == ""):
                #entity_insur_no1 = None
            temp_expiry_date1 = request.POST["entity_expiry_date1"]
            if (temp_expiry_date1 == ""):
                entity_expiry_date1 = None
            else:
                print(temp_expiry_date1)
                if (len(temp_expiry_date1.split('/')[0]) > 2):
                    temp_date = datetime.strptime(temp_expiry_date1, '%Y-%m-%d')
                else:
                    temp_date = datetime.strptime(temp_expiry_date1, '%m/%d/%Y')
                print(temp_date)
                entity_expiry_date1 = temp_date.strftime('%Y-%m-%d')
            created_date = str(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M"))
            '''           
            if (entity_name1 == ""):
                if(entity_locality1 != ""):
                    context = {
                        'Empty_flag': True
                    }
                    response = edit_account1(request, context)
                    return response
            elif(entity_locality1 == ""):
                context = {
                    'empty_flag': True
                }
                response = edit_account1(request, context)
                return response

            # validiy check for e
            # ntity_name and locality
            entity_names = user_address.objects.annotate(
                entity_name_lower=Lower("entity_name")).filter(account_id=usr_id).filter(~Q(addr_identity ="primary"))
            locations = user_address.objects.annotate(
                locality_lower=Lower("locality")).filter(account_id=usr_id).filter(~Q(addr_identity = "primary"))
            print("hello")
            duplicate_entity_flag = duplicate_locality_flag = duplicate_flag = False

            for entity_name in entity_names:
                print(entity_name.entity_name_lower, "    ", entity_name1.lower())
                if (entity_name.entity_name_lower == entity_name1.lower()):

                    duplicate_entity_flag = True
            for location in locations:
                print(location.locality_lower, "    ", entity_locality1.lower())
                if (location.locality_lower == entity_locality1.lower()):
                    duplicate_locality_flag = True
            if ((duplicate_entity_flag== True) and (duplicate_locality_flag == True)):
                    duplicate_flag = True


            if (duplicate_flag):
                #messages.error(request, "duplicate name")
                #return HttpResponseRedirect("editaccountone")
                context = {
                    'duplicate_flag': duplicate_flag
                }
                response = edit_account1(request, context)
                return response
            '''


            account_user_addres = user_address.objects.filter(account_id=usr_id).filter(addr_identity="primary")
            print("E_N",entity_name1)

            if (not account_user_addres):
                print("primary create")
                account_user_address = user_address.objects.create(account_id=acc_usr, entity_name=entity_name1, email= entity_mail1, contact_no=entity_contact_no1,
                                    door_street=entity_adddoor1, locality=entity_locality1, state= entity_state1, pincode=entity_pincode1,
                                    gstin=entity_gstin1, uin=entity_uin1, insurance_name=entity_insur_company1, insurance_no=entity_insur_no1,
                                    expiry_date=entity_expiry_date1,addr_identity="primary", created_date=created_date)
                account_user_address.save()
                print("successpc")
                display_messages = "Your Information is created Successfully."
                context = {

                    "display_messages": display_messages,

                }
            else:
                print("primary update")
                account_user_address = user_address.objects.filter(account_id=usr_id) .filter(addr_identity ="primary").update(entity_name=entity_name1, email=entity_mail1,
                                                                   contact_no=entity_contact_no1,
                                                                   door_street=entity_adddoor1,
                                                                   locality=entity_locality1, state=entity_state1,
                                                                   pincode=entity_pincode1,
                                                                   gstin=entity_gstin1, uin=entity_uin1,
                                                                   insurance_name=entity_insur_company1,
                                                                   insurance_no=entity_insur_no1,
                                                                   expiry_date=entity_expiry_date1,
                                                                   addr_identity="primary", updated_date=created_date)

                print("successpu")
                display_messages = "Your Information is updated Successfully."
                context = {

                    "display_messages": display_messages,

                }
            return render(request, "accountsuccessform.html", context)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, TypeError, KeyError,
            IndexError, AttributeError, ValueError, OverflowError, User.DoesNotExist, ValidationError,
            IntegrityError, InterfaceError) as e:
        print("Except", e)
        return HttpResponse (e)

def edit_account2info(request):
    try:
        print("edit_account2info", request.session.get("id"))
        usr_id = request.session.get("id")
        ac_id = request.session.get("account_id")
        acc_usr = User.objects.filter(id=usr_id).first()
        if (request.method == "POST"):
            entity_name2 = request.POST["entity_name2"]
            entity_mail = request.POST["entity_mail2"]
            entity_contact_no = request.POST["entity_contact_no2"]
            if (entity_contact_no == ""):
                entity_contact_no = None
            entity_adddoor = request.POST["entity_adddoor2"]
            entity_locality = request.POST["entity_locality2"]
            entity_state = request.POST["entity_state2"]
            if (entity_state==""):
                entity_state = None
            entity_pincode= request.POST["entity_pincode2"]
            if (entity_pincode == ""):
               entity_pincode =None
            entity_gstin = request.POST["entity_gstin2"]
            entity_uin= request.POST["entity_uin2"]
            entity_insur_company = request.POST["entity_insur_company2"]
            entity_insur_no = request.POST["entity_insur_no2"]
            #if (entity_insur_no == ""):
             #   entity_insur_no=None
            temp_expiry_date = request.POST["entity_expiry_date2"]
            if (temp_expiry_date == ""):
                entity_expiry_date =None
            else:
                print(temp_expiry_date)
                if (len(temp_expiry_date.split('/')[0]) > 2):
                    temp_date = datetime.strptime(temp_expiry_date, '%Y-%m-%d')
                else:
                    temp_date = datetime.strptime(temp_expiry_date, '%m/%d/%Y')
                print(temp_date)
                entity_expiry_date = temp_date.strftime('%Y-%m-%d')
            created_date = str(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M"))

            # validiy check for entity_name and locality
            '''
            entity_names = user_address.objects.annotate(
                entity_name_lower=Lower("entity_name")).filter(account_id=usr_id).filter(~Q(addr_identity="secondary1"))
            locations = user_address.objects.annotate(
                locality_lower=Lower("locality")).filter(account_id=usr_id).filter(~Q(addr_identity="secondary1"))
            print("hello")
            duplicate_entity_flag = duplicate_locality_flag = duplicate_flag = False

            for entity_name in entity_names:
                print(entity_name.entity_name_lower, "    ", entity_name2.lower())
                if (entity_name.entity_name_lower == entity_name2.lower()):

                    duplicate_entity_flag = True
            for location in locations:
                print(location.locality_lower, "    ", entity_locality.lower())
                if (location.locality_lower == entity_locality.lower()):
                    duplicate_locality_flag = True
            if ((duplicate_entity_flag== True) and (duplicate_locality_flag == True)):
                    duplicate_flag = True
            if (duplicate_flag):
                #messages.error(request, "duplicate name")
                #return HttpResponseRedirect("editaccounttwo")
                context = {
                    'duplicate_flag': duplicate_flag
                }
                response = edit_account1(request, context)
                return response
            '''
            account_user_addres = user_address.objects.filter(account_id=usr_id).filter(addr_identity="secondary1")
            if (not account_user_addres):
                print("not secondary1")
                account_user_address = user_address.objects.create(account_id=acc_usr, entity_name=entity_name2, email= entity_mail, contact_no=entity_contact_no,
                                    door_street=entity_adddoor, locality=entity_locality, state= entity_state, pincode=entity_pincode,
                                    gstin=entity_gstin, uin=entity_uin, insurance_name=entity_insur_company, insurance_no=entity_insur_no,
                                    expiry_date=entity_expiry_date,addr_identity="secondary1", created_date=created_date)
                account_user_address.save()
                print("successs1")
                display_messages = "Your Information is created Successfully."
                context = {

                "display_messages": display_messages,

                }
            else:
                print("not secondary update")
                account_user_address = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1").update(
                                                                   entity_name=entity_name2, email=entity_mail,
                                                                   contact_no=entity_contact_no,
                                                                   door_street=entity_adddoor, locality=entity_locality,
                                                                   state=entity_state, pincode=entity_pincode,
                                                                   gstin=entity_gstin, uin=entity_uin,
                                                                   insurance_name=entity_insur_company,
                                                                   insurance_no=entity_insur_no,
                                                                   expiry_date=entity_expiry_date,
                                                                   addr_identity="secondary1",
                                                                   updated_date=created_date)
                print("successs1u")
                display_messages = "Your Information is updated Successfully."
                context = {

                    "display_messages": display_messages,

                }
            return render(request, "accountsuccessform.html", context)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, TypeError, KeyError,
            IndexError, AttributeError, ValueError, OverflowError, User.DoesNotExist, ValidationError,
            IntegrityError, InterfaceError) as e:
        print("Except", e)
        return HttpResponse(e)

def edit_account3info(request):
    try:
        print("edit_account3info", request.session.get("id"))
        usr_id = request.session.get("id")
        acc_usr = User.objects.filter(id=usr_id).first()
        if (request.method == "POST"):
            entity_name3 = request.POST["entity_name3"]
            entity_mail = request.POST["entity_mail3"]
            entity_contact_no = request.POST["entity_contact_no3"]
            if (entity_contact_no == ""):
                entity_contact_no = None
            entity_adddoor = request.POST["entity_adddoor3"]
            entity_locality = request.POST["entity_locality3"]
            entity_state = request.POST["entity_state3"]
            if (entity_state==""):
                entity_state = None
            entity_pincode= request.POST["entity_pincode3"]
            if (entity_pincode == ""):
               entity_pincode =None
            entity_gstin = request.POST["entity_gstin3"]
            entity_uin= request.POST["entity_uin3"]
            entity_insur_company = request.POST["entity_insur_company3"]
            entity_insur_no = request.POST["entity_insur_no3"]
            #if (entity_insur_no == ""):
                #entity_insur_no=None
            temp_expiry_date = request.POST["entity_expiry_date3"]
            if (temp_expiry_date == ""):
                entity_expiry_date =None
            else:
                print(temp_expiry_date)
                if (len(temp_expiry_date.split('/')[0]) > 2):
                    temp_date = datetime.strptime(temp_expiry_date, '%Y-%m-%d')
                else:
                    temp_date = datetime.strptime(temp_expiry_date, '%m/%d/%Y')
                print(temp_date)
                entity_expiry_date = temp_date.strftime('%Y-%m-%d')
            created_date = str(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M"))

            # validiy check for entity_name and locality
            '''
            entity_names = user_address.objects.annotate(
                entity_name_lower=Lower("entity_name")).filter(account_id=usr_id).filter(~Q(addr_identity="secondary2"))
            locations = user_address.objects.annotate(
                locality_lower=Lower("locality")).filter(account_id=usr_id).filter(~Q(addr_identity="Secondary2"))
            print("hello")
            duplicate_entity_flag = duplicate_locality_flag = duplicate_flag = False

            for entity_name in entity_names:
                print(entity_name.entity_name_lower, "    ", entity_name3.lower())
                if (entity_name.entity_name_lower == entity_name3.lower()):
                    duplicate_entity_flag = True
            for location in locations:
                print(location.locality_lower, "    ", entity_locality.lower())
                if (location.locality_lower == entity_locality.lower()):
                    duplicate_locality_flag = True
            if ((duplicate_entity_flag == True) and (duplicate_locality_flag == True)):
                duplicate_flag = True
            if (duplicate_flag):
                #messages.error(request, "duplicate name")
                #return HttpResponseRedirect("editaccountthree")
                context = {
                    'duplicate_flag': duplicate_flag
                }
                response = edit_account1(request, context)
                return response
            '''
            account_user_addres = user_address.objects.filter(account_id=usr_id).filter(addr_identity="secondary2")
            if (not account_user_addres):
                account_user_address = user_address.objects.create(account_id=acc_usr, entity_name=entity_name3, email= entity_mail, contact_no=entity_contact_no,
                                    door_street=entity_adddoor, locality=entity_locality, state= entity_state, pincode=entity_pincode,
                                    gstin=entity_gstin, uin=entity_uin, insurance_name=entity_insur_company, insurance_no=entity_insur_no,
                                    expiry_date=entity_expiry_date,addr_identity="secondary2", created_date=created_date)
                account_user_address.save()
                print("success")
                display_messages = "Your Information is updated Successfully." + "\n" + "Your account Id:" + "\n" + " \n" + "\n" + "\n"
                context = {

                    "display_messages": display_messages,

                }
            else:
                account_user_address = user_address.objects.filter(account_id=usr_id,
                                                                   addr_identity="secondary2").update(
                            entity_name=entity_name3, email=entity_mail,
                            contact_no=entity_contact_no,
                            door_street=entity_adddoor, locality=entity_locality,
                            state=entity_state, pincode=entity_pincode,
                            gstin=entity_gstin, uin=entity_uin,
                            insurance_name=entity_insur_company,
                            insurance_no=entity_insur_no,
                            expiry_date=entity_expiry_date,
                            updated_date=created_date)
                print("success")
                display_messages = "Your Information is updated Successfully."
                context = {

                    "display_messages": display_messages,

                }

            return render(request, "accountsuccessform.html", context)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, TypeError, KeyError,
            IndexError, AttributeError, ValueError, OverflowError, User.DoesNotExist, ValidationError,
            IntegrityError, InterfaceError) as e:
        print("Except", e)
        return HttpResponse(e)

def edit_account_mail(request):
    try:
        print("edit_account_mail", request.session.get("id"))
        usr_id = request.session.get("id")
        acc_usr = User.objects.filter(id=usr_id).first()
        if (request.method == "POST"):
            entity_mail1 = request.POST["entity_email1"]
            entity_mail2 = request.POST["entity_email2"]
            entity_mail3 = request.POST["entity_email3"]

            created_date = str(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M"))
            account_user_addres = user_address.objects.filter(account_id=usr_id , addr_identity="primary")
            if (not account_user_addres):
                account_user_address = user_address.objects.create(account_id=acc_usr,
                                                                   entity_name="", email=entity_mail1,
                                                                   contact_no=None,
                                                                   door_street="", locality="",
                                                                   state="", pincode=None,
                                                                   gstin="", uin="",
                                                                   insurance_name="",
                                                                   insurance_no="",
                                                                   expiry_date=None,
                                                                   addr_identity="primary",
                                                                   created_date=created_date)
                account_user_address.save()
                print("successpc")

            else:
                print("hi")
                account_user_address = user_address.objects.filter(account_id=usr_id,
                                                                   addr_identity="primary").update(email=entity_mail1,updated_date=created_date)
                print("successpu")

            account_user_addres = user_address.objects.filter(account_id=usr_id, addr_identity="secondary1")
            if (not account_user_addres):
                account_user_address = user_address.objects.create(account_id=acc_usr,
                                                                   entity_name="", email=entity_mail2,
                                                                   contact_no=None,
                                                                   door_street="", locality="",
                                                                   state="", pincode=None,
                                                                   gstin="", uin="",
                                                                   insurance_name="",
                                                                   insurance_no="",
                                                                   expiry_date=None,
                                                                   addr_identity="secondary1",
                                                                   created_date=created_date)
                account_user_address.save()
                print("successs1c")

            else:
                account_user_address = user_address.objects.filter(account_id=usr_id,
                                                                   addr_identity="secondary1").update(email=entity_mail2,updated_date=created_date)
                print("successs1u")

                account_user_addres = user_address.objects.filter(account_id=usr_id, addr_identity="secondary2")
            if (not account_user_addres):
                    account_user_address = user_address.objects.create(account_id=acc_usr,
                                                                       entity_name="", email=entity_mail3,
                                                                       contact_no=None,
                                                                       door_street="", locality="",
                                                                       state="", pincode=None,
                                                                       gstin="", uin="",
                                                                       insurance_name="",
                                                                       insurance_no="",
                                                                       expiry_date=None,
                                                                       addr_identity="secondary2",
                                                                       created_date=created_date)
                    account_user_address.save()
                    print("successs2c")
            else:
                    account_user_address = user_address.objects.filter(account_id=usr_id,
                                                                       addr_identity="secondary2").update(
                        email=entity_mail3, updated_date=created_date)
                    print("successs2u")
            display_messages = "Your Information is stored Successfully."
            context = {

                        "display_messages": display_messages,

                    }
            return render(request, "accountsuccessform.html", context)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, TypeError, KeyError,
            IndexError, AttributeError, ValueError, OverflowError, User.DoesNotExist, ValidationError,
            IntegrityError, InterfaceError) as e:
        print("Except", e)
        return HttpResponse(e)

def updateVendor(request):
    try:

        if (request.method=="POST"):

            vendor_id = request.POST["submit"]
            print("vendor_id:", vendor_id)
            print("request Method:", request.method)

            company_nick_name = request.POST["company_nick_name"]
            company_name_reg = request.POST["company_name_reg"]
            door_street = request.POST["adddoor"]
            locality = request.POST["locality"]
            state = request.POST["state"]
            print("state:", state)
            pincode = request.POST["pincode"]
            primary_contact_no = request.POST["primary_contact_no"]
            if (primary_contact_no == ""):
                primary_contact_no =None
            primary_contact_name = request.POST["primary_contact_name"]
            primary_email = request.POST["primary_email"]
            secondary_contact_no = request.POST["secondary_contact_no"]
            if (secondary_contact_no == ""):
                secondary_contact_no = None
            secondary_contact_name = request.POST["contact_name2"]
            secondary_email = request.POST["secondary_email"]
            gstin = request.POST["gstin"]
            uin = request.POST["uin"]
            insurance_no = request.POST["insurno"]
            insurance_company = request.POST["insurcompany"]
            expiry_temp_date = request.POST["expirydate"]
            if (expiry_temp_date == ""):
                print("hi")
                expiry_date= None
            else:
                print(expiry_temp_date)
                if (len(expiry_temp_date.split('/')[0])>2):
                    temp_date = datetime.strptime(expiry_temp_date, '%Y-%m-%d')
                else:
                    temp_date = datetime.strptime(expiry_temp_date, '%m/%d/%Y')
                print(temp_date)
                expiry_date = temp_date.strftime('%Y-%m-%d')
            created_date = request.POST["created_date"]
            updated_date=str(datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M"))

            company_nicks = vendor_information.objects.annotate(
                company_nick_name_lower=Lower("company_nick_name")).filter(~Q(status="Deleted"), ~Q(vendor_id=vendor_id))
            print("hello")
            duplicate_flag = False
            for company_nick in company_nicks:
                if (company_nick.company_nick_name_lower == company_nick_name.lower()):
                    print(company_nick.company_nick_name_lower, "   ", company_nick_name.lower())
                    duplicate_flag = True
            print("local variable:", company_nick_name.lower())

            if (duplicate_flag):
                vendors_infos = {
                    'vendor_id':vendor_id,'company_nick_name': company_nick_name, 'company_name_reg': company_name_reg,
                    'door_street': door_street,'locality': locality, 'state': state, 'pincode': pincode,
                    'primary_contact_name': primary_contact_name,'primary_contact_no': primary_contact_no, 'primary_email': primary_email,
                    'secondary_contact_name': secondary_contact_name, 'secondary_contact_no': secondary_contact_no,
                    'secondary_email': secondary_email, 'gstin': gstin, 'uin': uin, 'insurance_no': insurance_no,
                    'insurance_company': insurance_company, 'expiry_date': expiry_date, 'created_date':created_date
                }
                context = {
                    'vendors_info': vendors_infos,
                    'display_messages': "Company Nick Name is already available. Pls give unique one"
                }
                return render(request, 'duplicateeditvendorinfo.html', context)
            else:
                vendor_info = vendor_information.objects.filter(vendor_id=vendor_id).update(company_nick_name=company_nick_name,
                                                         company_name_reg = company_name_reg, door_street=door_street,
                                                         locality=locality, state = state,
                                                        pincode = pincode, primary_contact_name= primary_contact_name, primary_contact_no =primary_contact_no,
                                                        primary_email=primary_email, secondary_contact_name =secondary_contact_name, secondary_contact_no=secondary_contact_no,
                                                        secondary_email=secondary_email, gstin=gstin, uin=uin,  insurance_no=insurance_no,
                                                        insurance_company=insurance_company,expiry_date = expiry_date,status="",
                                                        updated_date=updated_date
                                                        )

                print("Updated")

                updated_infos=vendor_information.objects.filter(vendor_id=vendor_id)
                display_messages= "Your Information is updated Successfully."
                context= {
                    "vendor_id": "CS Vendor ID: " + vendor_id,
                    "created_updated_date": "Updated at " + updated_date,
                    "display_messages": display_messages,


                }
                return render(request, "successform.html", context)

    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, TypeError,KeyError,IndexError, AttributeError, ValueError, OverflowError, User.DoesNotExist, ValidationError, IntegrityError, InterfaceError) as e:
        print("Exception:", e)
        return HttpResponse(e)


def traders(request):
    return render(request, "traders.html")

def confirm(request):
    return render(request, "successform.html")

def viewmore(request, id):
    try:
        vendors_infos= vendor_information.objects.filter(vendor_id=id)
        print("id:vendor_id",  id)
        vendors_infos = vendor_information.objects.filter(vendor_id=id)
        context = {

            "vendors_infos": vendors_infos,

        }
        return render(request, "Reportvendor.html", context)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, TypeError,KeyError,IndexError,  AttributeError,ValueError, OverflowError, User.DoesNotExist, ValidationError, IntegrityError, InterfaceError) as e:
        print("Exception:", e)
        return HttpResponse(e)

def table_info(request):
    try:
        print("hi")
        data = {}

        vendor_id=request.GET.get('id', None)
        vendor_id = vendor_id.split("r-")[1]
        obj= vendor_information.objects.get(vendor_id = vendor_id)

        user_info = {'vendor_id': obj.vendor_id, 'company_nick_name': obj.company_nick_name,"company_name_reg":obj.company_name_reg,
                     'door_street':obj.door_street,'locality': obj.locality, 'state': obj.state,
                     'pincode': obj.pincode,'primary_contact_name': obj.primary_contact_name,
                     'primary_contact_no': obj.primary_contact_no, 'primary_email': obj.primary_email,
                     'secondary_contact_name': obj.secondary_contact_name,
                     'seconday_contact_no': obj.secondary_contact_no, 'secondary_email': obj.primary_email,
                     'gstin': obj.gstin, 'uin': obj.uin,'insurance_no': obj.insurance_no,
                     'insurance_company': obj.insurance_company, 'expiry_date': obj.expiry_date, 'updated_date': obj.updated_date,
                     'created_date': obj.created_date
                     }
        data ={
            "user_info": user_info
        }
        print("Vendor_id", vendor_id)
        return JsonResponse(data)
    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, TypeError,KeyError,IndexError, AttributeError, ValueError, OverflowError, User.DoesNotExist, ValidationError, IntegrityError, InterfaceError) as e:
        print( "exception: ", e)

def delete_vendor_details(request):
    try:
        #vendor_id=request.POST["hidVendorId"]
        usr_id =request.session.get("id")
        vendor_id=request.GET.get('id', None)
        print("DELETE1 Vendor_id", vendor_id)
        delete_vendor = vendor_information.objects.filter(vendor_id=vendor_id).filter(account_id =usr_id).update(status="Deleted")
        vendor_info = vendor_information.objects.filter(~Q(status="Deleted")).filter(account_id =usr_id)
        print("deleted")
        data ={
            "deleted":True
        }
        print("DELETE2 Vendor_id", vendor_id)
        #return render(request, 'vendor5.html')
        return JsonResponse(data)

    except (OperationalError, ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError, TypeError, KeyError,IndexError, AttributeError, ValueError, OverflowError, User.DoesNotExist, ValidationError, IntegrityError, InterfaceError) as e:
        print("Exception: ", e)
        return HttpResponse(e)
