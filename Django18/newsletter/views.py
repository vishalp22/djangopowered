from django.core.mail import send_mail
from django.shortcuts import render
# Create your views here.
from Django18 import settings
from .forms import SignUpForm, ContactForm


def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.fullname:
            instance.fullname == "Vishal"
        instance.save()
        context = {
            "title": "Thank You"
        }
    return render(request, 'home.html', context)


def contact(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        fullname = form.cleaned_data.get("fullname")

        subject = 'Site Contact Form'
        from_email = settings.Email_HOST_USER
        to_email = [from_email, 'otheremail@gmail.com']

        contact_message = "{}: {} via {}".format(
            fullname,
            message,
            email,
        )
        some_html_message = """ <h1> Hello </h1> """

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  html_message=some_html_message,
                  fail_silently=True
                  )

    context = {
        "form": form,
        "title": title,
    }
    return render(request, 'forms.html', context)
