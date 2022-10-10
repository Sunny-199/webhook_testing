from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import EmailForm
from .mixins import EmailMixin
from django.core.mail import send_mail
from django.core.mail import EmailMessage


class Index(EmailMixin, TemplateView):
    template_name = 'index.html'
    email_template_name = 'email.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        form = EmailForm()
        data = dict()
        data['email_to'] = self.request.POST.get('email_to')
        data['title'] = self.request.POST.get('title')
        data['message'] = self.request.POST.get('message')

        context['form'] = form
        context['data'] = data
        return context

#     def post(self, request, *args, **kwargs):
#         self.send_mail(
#     'Subject here',
#     'Here is the message.',
#     'sunny@zestgeek.com',
#     ['sunny@zestgeek.com'],
#     fail_silently=False,
# )
#         return HttpResponseRedirect(reverse_lazy('core:index'))


    def post(self, request, *args, **kwargs):
        subject = "test email"
        message = "hello sunny"
        reply_to_list = ['sunny@zestgeek.com', 'sunny@zestgeek.com']

        email = EmailMessage(subject, message, 'sunny@zestgeek.com', reply_to_list)
        email.send(fail_silently=True)
        return HttpResponseRedirect(reverse_lazy('core:index'))

