from annoying.decorators import render_to
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django_hello_world.hello.models import Requests, ContactForm, Contact
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


@render_to('hello/home.html')
def home(request):
    users = User.objects.filter()

    record = Contact.objects.get(pk=1)
    return {'users': users,
            'name': record.name,
            'surname': record.surname,
            'bio': record.bio,
            'skype': record.skype,
            'email': record.email,
            'jabber': record.jabber,
            'other_contacts': record.other_contacts,
            'date_of_birth': record.date_of_birth,
            'photo': record.photo
            }


@render_to('hello/requests.html')
def requests(request):
    request_list = [req.req for req in Requests.objects.reverse()[:10]]
    return {'request_list': request_list}

@login_required
#@render_to('hello/form.html')
def form(request):

    item = get_object_or_404(Contact, id=1)
    form = ContactForm(request.POST or None, request.FILES or None,  instance=item)

    if request.method == 'POST':
        if form.is_valid():
            #todo: Process the data in form.cleaned_data
            form.save()
            if request.is_ajax():
                #if getattr(settings, 'DEBUG', False): # only if DEBUG=True
                #todo: remove freeze
                import time
                time.sleep(2)  # delay AJAX response for 5 seconds
                #todo: redirect fix
                return render(request, '/success/')

            else:
                return HttpResponseRedirect('/success/')

    return render(request, 'hello/form.html', {
        'form': form, 'photo': Contact.objects.get(pk=1).photo
    })


def login(request):
    return render_to_response('login.html')