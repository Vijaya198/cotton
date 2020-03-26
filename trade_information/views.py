from django.core.serializers import json
from django.db import models
from annoying.fields import AutoOneToOneField
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import trade_information, VendorProcessVendorInformation
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.db import models
#from django.db.models import vendor_process_vendor_information

# Create your views here.
def traderadd(request):
    print("traders")

    print("request Method:", request.method)
    #vendor_data = VendorProcessVendorInformation.objects.filter(vendor_type="Buyer")
    vendor_data = VendorProcessVendorInformation.objects.all()
    #trader_detail= VendorProcessVendorInformation.objects.filter(vendor_type="Trader")

    return render(request, "traderadd.html", {"vendor_data": vendor_data, })


def vendoradd(request):
   # print("traders")
    return render(request, "vendoradd.html")

def traders(request):

    return render(request, "traders.html")

def vendor(request):
   # print("traders")
    return render(request, "vendor.html")



def trader_details(request):
    if (request.method == "POST"):
        print("request Method:", request.method)
        #data = vendor_process_vendor_information.objects.all()
        bussiness_mode = request.POST["bussinesstype"]
        conf_no = request.POST["retconfirmno"]
        conf_date = request.POST["tconfirmdate"]
        buyer_name = request.POST["tbuyername"]
        gstin_buyer = request.POST["tgstin_b"]
        buyer_door_street = request.POST["tdoor_add"]

        buyer_state = request.POST["tstate"]

        buyer_pincode = request.POST["tpincode"]
        seller_name = request.POST["sellername"]
        gstin_seller = request.POST["tgstin_s"]
        trader_name = request.POST["tradername"]
        trader_type = request.POST["tradertype"]
        broker_name = request.POST["tbrokername"]

        broker_contact_no = request.POST["tbroker_cno"]

        broker_email = request.POST["tbrokeremail"]
        broker_commission_percent = request.POST["tcommiss_per"]
        broker_commission_rupees = request.POST["tcommiss_rs"]
        station = request.POST["tstation"]
        state = request.POST["tstate_qual"]
        hsn_code = request.POST["thsn"]
        variety = request.POST["tvariety"]
        staple_buyer = request.POST["tstaple_b"]
        staple_seller = request.POST["tstaple_s"]
        mic_buyer = request.POST["tmicfrom_b"]
        mic_seller = request.POST["tmicfrom_s"]
        grade = request.POST["tgrade"]
        gtex_buyer = request.POST["tgtex_b"]
        gtex_seller = request.POST["tgtex_s"]
        gpt = request.POST["tgpt"]
        moist_buyer = request.POST["tmoisture_b"]
        moist_seller = request.POST["tmoisture_s"]
        trash_buyer = request.POST["ttrash_b"]
        trash_seller = request.POST["ttrash_s"]
        bales_nos = request.POST["tbales"]
        truck_nos = request.POST["ttruck"]
        price = request.POST["tprice"]
        delivery_terms = request.POST["termdel"]
        gst = request.POST["tgst"]
        dispatch_terms = request.POST["tdispatch"]
        payment_terms = request.POST["termpay"]
        first_payment = request.POST["tfirstpa"]
        first_payment_days = request.POST["tfirstpayday"]
        second_payment = request.POST["tsecondpayper"]
        second_payment_days = request.POST["tsecondpayday"]
        dhara = request.POST["tdhara"]
        gst_payment = request.POST["tgstpay"]
        interest_late_payment = request.POST["tinterestlate"]
        weighment_terms = request.POST["tweighment"]
        passing_terms = request.POST["tpassing"]
        transit_insurance_details = request.POST["transit_insur"]
        unloading_contact_no = request.POST["tmillgateno"]
        weighbridge_contact_no = request.POST["weighbridgeno"]
        notes = request.POST["tnotes"]




        trade_info = trade_information.objects.create(bussiness_mode = bussinesstype,
                                                        conf_no = 1,
                                                        conf_date=tconfirmdate,
                                                        buyer_name=tbuyername,
                                                        gstin_buyer = tgstin_b,
                                                        buyer_door_street=tdoor_add,

                                                        buyer_state=tstate,

                                                        buyer_pincode=tpincode,
                                                        seller_name = sellername,
                                                        gstin_seller = tgstin_s,
                                                        trader_name=tradername,
                                                        trader_type=tradertype,
                                                        broker_name = tbrokername,

                                                        broker_contact_no = tbroker_cno,

                                                        broker_email=tbrokeremail,
                                                        broker_commission_percent = tcommiss_per,
                                                        broker_commission_rupees = tcommiss_rs,
                                                        station = tstation,
                                                        state = tstate_qual,
                                                        hsn_code =thsn,
                                                        variety=tvariety,
                                                        staple_buyer=tstaple_b,
                                                        staple_seller = tstaple_s,
                                                        mic_buyer=tmicfrom_b,
                                                        mic_seller = tmicfrom_s,
                                                        grade=tgrade,
                                                        gtex_buyer = tgtex_b,
                                                        gtex_seller = tgtex_s,
                                                        gpt = tgpt,
                                                        moist_buyer = tmoisture_b,
                                                        moist_seller = tmoisture_s,
                                                        trash_buyer = ttrash_b,
                                                        trash_seller = ttrash_s,
                                                        bales_nos=tbales,
                                                        truck_nos=ttruck,
                                                        price=tprice,
                                                        delivery_terms=termdel,
                                                        gst=tgst,
                                                        dispatch_terms=tdispatch,
                                                        payment_terms=termpay,
                                                        first_payment=tfirstpa,
                                                        first_payment_days = tfirstpayday,
                                                        second_payment = tsecondpayper,
                                                        second_payment_days = tsecondpayday,
                                                        dhara=tdhara,
                                                        gst_payment=tgstpay,
                                                        interest_late_payment=tinterestlate,
                                                        weighment_terms=tweighment,
                                                        passing_terms = tpassing,
                                                        transit_insurance_details=transit_insur,
                                                        unloading_contact_no = tmillgateno,
                                                        weighbridge_contact_no = weighbridgeno,
                                                        notes=tnotes
                                                                                        )
        trade_info.save()
        return render(request, "confirmform.html")
    else:
        return render(request, "traders.html")


def buyer_populate(request):
    print("buyerpopulate")
    buyer_name = request.POST.get('buyer_name')
    print(buyer_name)
    try:
        buyer_data = VendorProcessVendorInformation.objects.get(company_name=buyer_name)
    except VendorProcessVendorInformation.MultipleObjectsReturned:
        buyer_data = VendorProcessVendorInformation.objects.filter(company_name=buyer_name).first()


    print(buyer_data)

    buyer_info = [{'gstin': buyer_data.gstin, 'company_door_street': buyer_data.company_door_street, 'company_state': buyer_data.company_state, 'company_pincode': buyer_data.company_pincode}]
    response_data = {"buyer_info": buyer_info}
    print(buyer_info)
    response_data = {}
    try:
        response_data['buyer_info'] = buyer_info
        print("try")




        print("except")
    except:
        response_data['result'] = 'No details found'
        response_data['message'] = 'There is currently no data'

    print("returning response")

    return JsonResponse(buyer_info, safe=False)


def seller_populate(request):
    print("sellerpopulate")
    seller_name = request.POST.get('seller_name')
    print(seller_name)
    try:
        seller_data = VendorProcessVendorInformation.objects.get(company_name=seller_name)
    except VendorProcessVendorInformation.MultipleObjectsReturned:
        seller_data = VendorProcessVendorInformation.objects.filter(company_name=seller_name).first()



    print(seller_data)

    seller_info = [{'gstin': seller_data.gstin, 'company_door_street': seller_data.company_door_street,
                   'company_state': seller_data.company_state, 'company_pincode': seller_data.company_pincode}]
    response_data = {"seller_info": seller_info}
    print(seller_info)
    response_data = {}
    try:
        response_data['buyer_info'] = seller_info
        print("try")


    except:
        print("except")
        response_data['result'] = 'No details found'
        response_data['message'] = 'There is currently no data'

    print("returning response")

    return JsonResponse(seller_info, safe=False)

def trader_populate(request):
    print("traderpopulate")
    trader_name = request.POST.get('trader_name')
    print(trader_name)
    try:
        trader_data = VendorProcessVendorInformation.objects.get(company_name=trader_name)
    except VendorProcessVendorInformation.MultipleObjectsReturned:
        trader_data = VendorProcessVendorInformation.objects.filter(company_name=trader_name).first()



    print(trader_data)

    trader_info = [{'gstin': trader_data.gstin, 'company_door_street': trader_data.company_door_street,
                   'company_state': trader_data.company_state, 'company_pincode': trader_data.company_pincode}]
    response_data = {"trader_info": trader_info}
    print(trader_info)
    response_data = {}
    try:
        response_data['buyer_info'] = trader_info
        print("try")


    except:
        print("except")
        response_data['result'] = 'No details found'
        response_data['message'] = 'There is currently no data'

    print("returning response")

    return JsonResponse(trader_info, safe=False)

