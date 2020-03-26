
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import View
from django.contrib.sessions.models import Session
from .forms import SignupForm, EmailValidationOnForgotPassword
from .tokens import account_activation_token, password_reset_token
from vendor_process.views import *
from datetime import datetime, date


# from django.contrib.auth import get_user_model
# User = get_user_model()


# Create your views here.
def home(request):
        if (request.user):
            print("hi")
            return render(request, "result.html")
        else:
            print("hi")
            return render(request, "login.html")


def user_login(request):

    context = {}

    if (request.method=="POST"):
        email = request.POST.get('email')

        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user:
            #login(request, user)
            acc_user = User.objects.filter(email=email).first()
            request.session["id"] = acc_user.id
            request.session["account_id"] = acc_user.account_id
            request.session['email']=acc_user.email
            print("session_id:login", request.session.session_key)
            print("session_id:login",acc_user.id)
            #request.session.id = acc_user.id

            #print(request.session['_auth_user_id'])
            #print(request.session['_auth_user_backend'])
            #request.session.account_id = accid.account_id
            #request.session.id=accid=id

            #context = {'account_id': accid.account_id}


            #if request.GET.get('next', None):
               # return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect("vendors")
        else:
            if User.objects.filter(email=email).exists():
                u = User.objects.get(email=email)
                if u.is_active:
                    #context["error"] = "Incorrect Password, please click Forgot Password to reset your password"
                    messages.info(request, "Incorrect Password")
                    logout(request)
                    return HttpResponseRedirect(reverse('user_login'))

                    #return render(request, "login.html", context)
                else:
                    return render(request, "confirmation_link_invalid.html")
            else:

                return render(request, "login.html", context)
    else:
        return render(request, "login.html", context)


def user_success(request):
    context = {}
    if (request.user.is_authenticated):
        print("user success")
        request.session.user =request.user
        return render(request, "result.html", context)
    else:

        messages.info(request, "Pls sign in....")
        return HttpResponseRedirect(reverse("user_login"))

def user_details(request):

    context = {}
    #if (request.user.is_authenticated):
    request.session.user=request.user

    return render(request, "user_details.html")
    #else:

        #messages.info(request, "Pls sign in.")
        #return HttpResponseRedirect(reverse("user_login"))

def user_register(request):
    #sys_messages = messages.get_messages(request)

    #for msg in sys_messages._queued_messages:
        #del msg

    if (request.method=="POST"):
        print("User_register HI")

        username = request.POST.get('username')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")




        first_name = request.POST.get('first_name')

        last_name = request.POST.get('last_name')


        if (username):
            print("first if loop")
            if(password1):
                if (password1==password2):
                    print("second if loop")
                    if (User.objects.filter(username=username).exists()):
                        print("Username already exists")
                        messages.info(request, "Username already exists")
                        return render(request, "index.html")
                    elif (User.objects.filter(email=email).exists()):
                        print("email already taken")
                        messages.info(request, "email already taken")
                        return render(request, "signup.html")
                    else:
                        user=User.objects.create_user(username=username,
                                      first_name=first_name,
                                      last_name=last_name,
                                      password=password1,
                                      email=email
                                      )
                        user.save()
                        print("Register Successfully")

                        try:
                            del request.session.user

                        except:
                            pass
                        logout(request)

                        messages.info(request, "Register successfully.... Please Sign in  with resgister details")
                        return render(request, "login.html")

                else:
                    print("password is mismatch")


                    messages.info(request, "Password mismatch")
                    return render(request, "signup.html")
            else:

                messages.info(request, "pls enter username")
                return HttpResponseRedirect(reverse("user_register"))
        else:

            return HttpResponseRedirect(reverse("user_register"))

    else:
        return render(request, "signup.html")


def user_signup(request):
    print("signup")
    #return render(request, "register.html")
    #return HttpResponseRedirect(reverse("user_register"))
    #username = request.POST.get('username')
    if (request.method == "POST"):
        email = request.POST.get('email')
        print(email)
        password1 = request.POST.get('password1')
        print(password1)
        password2 = request.POST.get('password2')


        if(email):
            print("first if loop")
            if (password1):
                print(password1)
                if (password1 == password2):
                    print("second if loop")
                    if (User.objects.filter(email=email).exists()):
                        print("email already taken")
                        messages.info(request, "email already taken")
                        return render(request, "signup.html")
                    elif(password1 != password2):
                        print("password is mismatch")

                        messages.info(request, "Password mismatch")
                        return render(request, "signup.html")

                    else:
                        user = User(username=email, email='email')
                        user.set_password(password1)
                        user.is_active = False
                        user.save()
                        current_site = get_current_site(request)
                        mail_subject = 'Activate your account.'
                        message = render_to_string('acc_active_email.html', {
                            'email': email,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': account_activation_token.make_token(email),
                        })
                        to_email = email
                        email1 = EmailMessage(mail_subject, message, to=[to_email])
                        email1.send()
                        print("Register Successfully")
                        return HttpResponse('Please confirm your email address to complete the registration')


                        #try:
                        #    del request.session.user

                        #except:
                         #   pass
                        #logout(request)

                        #messages.info(request, "Register successfully.... Please Sign in  with resgister details")
                        #print(request)
                        #return HttpResponseRedirect(reverse("user_login"))
                else:
                    print("password is mismatch")

                    messages.info(request, "Password mismatch")
                    return render(request, "signup.html")
            else:

                messages.info(request, "pls enter password")
                return HttpResponseRedirect(reverse("user_signup"))
        else:

            messages.info(request, "pls enter valid email id")
            return HttpResponseRedirect(reverse("user_signup"))




    else:
        return render(request, "signup.html")




def user_profile(request):

    return render(request, "profile.html")

def user_logout(request):

    try:
        print("logout",request.session.session_key)
        request.session.flush()

    except:

        pass

    messages.info(request, " ")
    #logout(request)
    return HttpResponseRedirect(reverse('user_login'))
    #return render(request, "login.html")

class SignUpView(View):

    form_class = SignupForm
    template_name ='signup.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        context = {}
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            #account_id = increment_account_number()
            if (password1 == password2):

                if ((User.objects.filter(email=email).exists()) and  (User.is_active)):

                    print("email already taken")
                    messages.info(request, "email already taken")
                    #return render(request, "signup.html")
                else:
                    user = form.save(commit=False)
                    user.is_active = False
                    user.save()
                    current_site = get_current_site(request)
                    print(current_site)
                    subject = 'Activate Your account'
                    message = render_to_string('acc_active_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                    })
                    user.email_user(subject, message)
                    #class Meta:
                        #model = EmailAddress
                        #fields = ('email', 'verified', 'user_id')
                    #EmailAddress.save(self, update_fields='email')
                    #context['message'] = "Please confirm your email to complete registration"
                    return render(request, "confirmation_link_invalid.html", context)
                    #messages.success(request, ('Please confirm your email to complete registration'))
            else:
                return render(request, "password_incorrect.html")
                #return redirect('login')
        return render(request,self.template_name, {'form': form})
        #return render(request, 'password_incorrect.html', {'form': form})


        #return render(request, "password_incorrect.html")

class ActivateAccount(View):


    def get(self, request, uidb64, token, *args, **kwargs):
        #form = self.form_class(request.POST)
        try:
            print("try")
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
            print(user)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            print("except")
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            print("user is not none")
            user.is_active = True
            #user.email_confirmed = True
            #EmailAddress.verified = True
            print("email confirmed")
            print("authentification", user.is_authenticated)
            user.save()

            #login(request, user, backend='django.contib.auth.backends.ModelBackend')
            #messages.success(request, ('Your account have been confirmed.'))
            #return redirect('user_login')
            #return redirect('login.html')
            #return redirect("account_activated.html")
            print(request)

            return render(request, "account_activated.html")
        else:
            #user.email_confirmed = False
            #messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return render(request, "confirmation_link_invalid.html")

class PasswordResetView(View):
#class PassResView(RatelimitMixin, PasswordResetView):
    form_class = EmailValidationOnForgotPassword
    template_name ='register/password_reset_form'


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, *args, **kwargs):
        context = {}
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if not User.objects.filter(email__iexact=email, is_active=True).exists():
                user = form.save(commit=False)
                msg = "There is no user with this email."
                current_site = get_current_site(request)
                print(current_site)
                subject = 'Password Change'
                message = render_to_string('registration/password_reset_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': password_reset_token.make_token(user),
                })
                user.email_user(subject, message)
                return render(request, "password_reset_complete.html", context)
            else:
                    return render(request, "password_incorrect.html")
                    #return redirect('login')
        return render(request, self.template_name, {'form': form})

def increment_account_number():
    last_user = User.objects.all().order_by('id').last()
    if not last_user:
        new_account_id = str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) +str(datetime.date.today().day).zfill(2)+ '001'
        new_acc_id = int(new_account_id)

        return new_acc_id

    account_id = last_user.account_id
    acc_id = str(account_id)
    account_int = int(acc_id[8:11])
    new_account_int = account_int + 1
    new_account_id =  str(date.today().year) + str(date.today().month).zfill(2) + str(date.today().day).zfill(2)+str(new_account_int).zfill(3)
    new_acc_id= int(new_account_id)

    return new_acc_id






