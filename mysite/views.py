from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
#from steps_count.models import Top_List
#from steps_count.forms import Top_List_Form

import datetime

from mysite.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def hello(request):
    return HttpResponse("Hello World!")
def current_datetime(request):
    now = datetime.datetime.now()
    ##t = Template("It is now {{ current_date }}.")
    ###t = get_template('current_datetime.html')
    #html = "<html><body> It is now %s.</body></html>" % now
    ###html = t.render(Context({'current_date': now}))
    ###return HttpResponse(html)
    return render(request, 'current_datetime.html', {'current_date': now})
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body> In %s hour(s), it will be %s.</body></html>" %(offset, dt)
    return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                'noreply@example.com',
                #cd.get('email', 'sdcdrive@example.com'),
                #['suneel.m@axiomio.com'],
                [cd['email']]
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial = {'subject': 'I love your site!'}
            )
    return render(request, 'contact_form.html', {'form': form})

def thanks(request):
    return HttpResponse('thanks')
