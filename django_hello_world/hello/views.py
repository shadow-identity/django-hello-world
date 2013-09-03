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
            #todo: fix paths
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
            item.name = form.cleaned_data['name']
            item.surname = form.cleaned_data['surname']
            item.email = form.cleaned_data['email']
            item.skype = form.cleaned_data['skype']
            item.jabber = form.cleaned_data['jabber']
            item.date_of_birth = form.cleaned_data['date_of_birth']
            item.bio = form.cleaned_data['bio']
            item.other_contacts = form.cleaned_data['other_contacts']

            item.save()
            if request.is_ajax():
                #if getattr(settings, 'DEBUG', False): # only if DEBUG=True
                #todo: remove freeze
                import time
                time.sleep(2)  # delay AJAX response for 5 seconds
                return HttpResponseRedirect('/success/')

            else:
                return HttpResponseRedirect('/success/')

    return render(request, 'hello/form.html', {
        'form': form, 'photo': Contact.objects.get(pk=1).photo
    })


def login(request):
    return render_to_response('login.html')