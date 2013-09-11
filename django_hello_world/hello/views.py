from annoying.decorators import render_to
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django_hello_world.hello.models import Requests, Contact
from django_hello_world.hello.forms import ContactForm, CustomRequestsForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.conf import settings
from django.forms.models import modelformset_factory


@render_to('hello/home.html')
def home(request):
    users = User.objects.filter()

    record = Contact.objects.get(pk=1)
    return {'users': users,
            'request': request,
            'record': record
            }


@render_to('hello/requests.html')
def requests(request):
    requests = Requests.objects.all()
    return {'request': request,
            'requests': requests}
    # RequestsFormSet = modelformset_factory(Requests, max_num=10)
    # if request.method == 'POST':
    #     formset = RequestsFormSet(request.POST, request.FILES)
    #     if formset.is_valid():
    #         for form in formset:
    #             form.save()
    # else:
    #     formset = RequestsFormSet()
    #     # for form in formset:
    #     #     print (form.as_table())
    # print formset
    # return {'formset': formset}
    #request_list = [req.req for req in Requests.objects.reverse()[:10]]
    #return {'request_list': request_list}


@login_required
#@render_to('hello/form.html')
def form(request):
    if request.is_ajax():
        template = 'hello/form.html'
    else:
        template = 'hello/edit.html'
    item = get_object_or_404(Contact, id=1)
    form = ContactForm(request.POST or None, request.FILES or None,  instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            if request.is_ajax():
                if getattr(settings, 'DEBUG', False):  # only if DEBUG=True
                    import time
                    time.sleep(2)  # delay AJAX response for x seconds
                return HttpResponseRedirect('/success/')

            else:
                return HttpResponseRedirect('/success/')

    return render(request, template, {
        'form': form, 'photo': Contact.objects.get(pk=1).photo
    })


def login(request):
    return render_to_response('login.html')
