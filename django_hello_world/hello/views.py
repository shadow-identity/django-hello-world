from annoying.decorators import render_to
from django.contrib.auth.models import User
from hello.models import Requests, ContactForm, Contact

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


@render_to('hello/home.html')
def home(request):
    users = User.objects.filter()

    #TODO: remove it
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

#@render_to('hello/form.html')
def form(request):

    item = get_object_or_404(Contact, id=1)
    form = ContactForm(request.POST or None, instance=item)

    if request.method == 'POST': # If the form has been submitted...
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            form.save()
            return HttpResponseRedirect('/') # Redirect after POST

    return render(request, 'hello/form.html', {
        'form': form,
    })

    #form = get_object_or_404(Requests)
    """try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))"""
