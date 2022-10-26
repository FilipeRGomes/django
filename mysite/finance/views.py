from dataclasses import fields
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import AccountForm
from .models import Account, Transaction


class AccountIndexView(generic.ListView):
    model = Account
    template_name = 'account/account_list.html'
    context_object_name = 'list' #Returned by queryset

    def get_queryset(self):
        """Return the last five published questions."""
        return Account.objects.all()


class AccountDetailView(generic.DetailView):
    model = Account
    form_class = AccountForm
    template_name = 'account/detail.html'
    context_object_name = 'content' # name of object used in context
    

class AccountCreateView(generic.CreateView):
    model = Account
    form_class: AccountForm 
    template_name = 'account/create.html'
    #fields = ['name', 'account_description', 'balance']




class AccountUpdateView(generic.UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'account/account_update.html'
    #fields = ['name', 'account_description', 'balance']

    # Estudar mais os metodos especiais do django
    def dispatch(self, *args, **kwargs):
        self.account_id = kwargs['pk']
        return super(AccountUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        account = Account.objects.get(id=self.account_id)
        return HttpResponse(render_to_string('account/account_success_update.html', {'account': account}))    


class AccountDeleteView(generic.DeleteView):
    model = Account
    success_url = reverse_lazy('finance:index')
    template_name = 'account/confirm_delete.html'




class ResultsView(generic.DetailView):
    model = Account
    template_name = 'result.html'



