from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from .models import  *
from rest_framework import status
from .models import *
import requests
from django.http import HttpResponse,Http404,HttpResponseRedirect
from jamboAdmin.forms import SignUpForm
from .email import *
from .forms import *


def signup(request):
    if request.method == 'POST':
        form = merchantUSers(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)

            name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            recipient = NewsLetterRecipientss(name=name, email=email)
            recipient.save()
            send_message(name, email)
            return redirect('indexone')
    else:
        form = merchantUSers()

    return render(request, 'registration/registration_form.html', {'form': form})

def indexone(request):
    return render(request, 'indexone.html')

@login_required(login_url='/accounts/login/')
def merchants(request):
<<<<<<< HEAD
    url = ('http://127.0.0.1:8000/api/GetMerchants')
    headers = {'Authorization': 'Token 6841dd7a3c767c125ca2fdaddf05ee5f127ab6f8'}
    response = requests.get(url,headers=headers)
=======
    url = ('https://jpaye.herokuapp.com/api/GetMerchants')
    headers = {'Authorization': 'Token 4d7607cc35bc893b6f80eac430d4371fb46dc0c8'}
    response = requests.get(url, headers=headers)
>>>>>>> 9ec2200006d4c28fa6e31e37299b0c1648ca27f3
    details = response.json()
    for detail in details:
        Business_name = detail.get('Business_name')
        Email = detail.get('Email')
        Phone_number = detail.get('Phone_number')
        Address = detail.get('Physical_address')
        Code = detail.get('Post_code')
        Town = detail.get('Town')
        Pay_bill = detail.get('JP_paybill')
        Industry = detail.get('Industry')
        
    return render(request, 'merchants.html', {'details': details})

<<<<<<< HEAD

def sign(request):
    current_user = request.user
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            merchant = form.save(commit=False)
            merchant.save()

            name = form.cleaned_data.get('Business_owner')
            email = form.cleaned_data.get('email')
        
            recipient = Merchant(name=Business_owner, email=email)
            recipient.save()
            send_message(name, email)
            
=======
@login_required(login_url='/accounts/login/')
def revenueStreams(request):
    url = ('https://jpaye.herokuapp.com/api/GetRevenueStreams')
    headers = {'Authorization': 'Token 4d7607cc35bc893b6f80eac430d4371fb46dc0c8'}
    response = requests.get(url, headers=headers)
    details = response.json()
    for detail in details:
        id= detail.get('id')
        name = detail.get('name')
    return render(request, 'revenueStreams.html', {'details': details})


def payments(request):
    url = ('https://jpaye.herokuapp.com/api/GetPayments/')
    headers = {'Authorization': 'Token 4d7607cc35bc893b6f80eac430d4371fb46dc0c8'}
    response = requests.get(url,headers=headers)
    details = response.json()
    for detail in details:
        id = detail.get('id')
        bill_number = detail.get('bill_number')
        payers_name = detail.get('payers_name')
        payers_phone = detail.get('payers_phone')
        narration = detail.get('narration')
        amount = detail.get('amount')
        pay_date = detail.get('pay_date')
    return render(request, 'payments.html', {'details': details})



def merchantBills(request):
    url = ('https://jpaye.herokuapp.com/api/BillsDetails/')
    headers = {'Authorization': 'Token 4d7607cc35bc893b6f80eac430d4371fb46dc0c8'}
    response = requests.get(url,headers=headers)
    details = response.json()
    for detail in details:
        id = detail.get('id')
        customer_name = detail.get('customer_name')
        customer_phone = detail.get('customer_phone')
        customer_email = detail.get('customer_email')
        narration = detail.get('narration')
        quantity = detail.get('quantity')
        amount = detail.get('amount')
        post_date = detail.get('post_date')
        due_date = detail.get('due_date')
        generated_by = detail.get('generated_by')
        status = detail.get('status')
    return render(request, 'merchant_bills.html', {'details': details})
>>>>>>> 9ec2200006d4c28fa6e31e37299b0c1648ca27f3
