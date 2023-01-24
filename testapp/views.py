from django.shortcuts import render,redirect
from django.contrib import messages
from random import randint
from django.core.mail import send_mail
# Create your views here.
def contact_us(request):
    if request.method=='GET':
        template_name='testapp/contact_form.html'
        return render(request,template_name)
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone_no=request.POST.get('phone_no')
        message=request.POST.get('message')
        print(f'name {name} email {email} phone_no {phone_no} message {message}')
        otp=randint(100000,999999)
        print('your otp is ',otp)
        request.session['OTP']=str(otp)
        request.session['name']=str(name)
        request.session['email']=str(email)
        request.session['phone_no']=str(phone_no)
        request.session['message']=str(message)
        subject="Email Verification"
        message=f"""
                Hey {name} !
                
                This is Your Otp - {otp} ,for Verification
                """
        mail_from='bharathbrnads@gmail.com'
        email_to=email
        send_mail(
            subject,
            message,
            mail_from,
            [email_to],
            fail_silently=False
        )
        messages.info(request,'Check Your Mail , You Received OTP For Verification')
        return redirect('verification')
def verification(request):
    if request.method == 'GET':
        is_verification=True
        context={
            'is_verification':is_verification,
        }
        template_name='testapp/verification_form.html'
        return render(request,template_name,context)
    if request.method == 'POST':
        user_otp=request.POST.get('user_otp')
        system_otp= request.session['OTP']
        if system_otp == user_otp:
            name=request.session['name']
            email=request.session['email']
            phone_no=request.session['phone_no']
            message=request.session['message']
            subject=f"{name} is contacting you"
            message=f"""
                    Name : {name} , 
                    Email  : {email} , 
                    Phone NO : {phone_no} , 
                    Messages : {message} , 
                    """
            mail_from='bharathbrnads@gmail.com'
            email_to='ram659504@gmail.com'
            send_mail(
                subject,
                message,
                mail_from,
                [email_to],
                fail_silently=False
            )
            messages.success(request,'Successfully your details has been submitted..!!')
            return redirect('success')
        else:
            is_invalid_otp=True
            context={
                'is_invalid_otp':is_invalid_otp
            }
            template_name='testapp/verification_form.html'
            return render(request,template_name,context)
def success(request):
    template_name='testapp/success.html'
    return render(request,template_name)