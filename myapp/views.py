from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from .forms import URLform
from .models import URL
# Create your views here.
def home(request):
	form = URLform(request.POST or None)
	context = {
	     "form": form,
	}



	if form.is_valid():
		instance = form.save(commit=False)
		myurl = form.cleaned_data.get("myurl")
		if not myurl:
			myurl = "New myurl"	
		instance.myurl = myurl
		instance.save()
		context = {
		    "title": "Thank You"
		}



	# if request.user.is_authenticated() and request.user.is_staff:
	# 	# for instance in SignUp.objects.all():
	# 	# 	print (instance.full_name)

	# 	queryset = SignUp.objects.all().order_by('-timestamp')
	# 	context = {
	# 	"queryset" : queryset
	# 	}
	return render(request, "home.html", context)


def contact(request):
	title = 'Contact Us'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key in form.cleaned_data:
		# 	print (key)
		# 	print (form.cleaned_data.get(key))
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		full_name = form.cleaned_data.get("full_name")
		subject = "Site contact form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'yourotheremail@gmail.com']
		contact_message = "%s: %s via %s"%(form_full_name, form_message, form_email)
		send_mail(subject, 
			contact_message,
			 from_email, 
			 [to_email], 
			 fail_silently=False)


	context ={
        "form": form,
        "title": title,
	}
	return render(request, "forms.html", context)