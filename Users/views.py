from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.conf import settings
from django.core.mail import send_mail

from Users.forms import SignUpForm
from Users.tokens import account_activation_token


@login_required
def home(request):
    return render(request, 'users/home.html')

def login_view(request):
	context = {}
	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
		if user:
			login(request, user)
			return redirect('home')
	else:
		form = AccountAuthenticationForm()
		context['login_form'] = form
	return render(request, "users/login.html", context)

    
def signup(request):
    if request.method == 'POST':
        f = SignUpForm(request.POST)
        if f.is_valid():
            user = f.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('users/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_to = user.email
            print(send_to)
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, [send_to], fail_silently=False)

            return redirect('account_activation_sent')
    else:
            f = SignUpForm()
    return render(request, 'users/signup.html', {'form': f})


def account_activation_sent(request):
    return render(request, 'users/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')
    return render(request, 'users/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'users/account_activation_sent.html')


#from django.shortcuts import render
#, redirect
#from django.views import View
#from django.http import JsonResponse
#from django.contrib.auth.models import User

#import json


#class UsenameValidationView(View):
#    def post(self, request):
#        data = json.loads(requst.body)
#        username = data['username']

#        if User.objects.filter(username=username).exists():
#            return JsonResponse({'username_error': 'username already exists'}, status=400)
#        
#        return JsonResponse({'username_valid': True})
        
        

#class RegistrationView(View):
#    def get(self, request):
#        return render(request, 'users/register.html')

