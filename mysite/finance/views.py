from dataclasses import fields
from unicodedata import category
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import AccountForm, CategoryForm
from .models import Account, Category, Transaction

################################################################################################
# Account Views
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
    template_name = 'account/account_create.html'
    fields = ['name', 'account_description', 'balance']
    
    def dispatch(self, *args, **kwargs):
        #self.account_id = kwargs['pk']
        return super(AccountCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.save()
        return HttpResponse(render_to_string('account/account_success_update.html'))    


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
    success_url = reverse_lazy('finance:account_index')
    template_name = 'account/account_confirm_delete.html'

    def dispatch(self, *args, **kwargs):
        self.account_id = kwargs['pk']
        return super(AccountDeleteView, self).dispatch(*args, **kwargs)
    
    
    def form_valid(self, form):
        account = Account.objects.get(id=self.account_id)
        account.delete()
        return HttpResponse(render_to_string('account/account_success_update.html'))    

    # Estudar mais os metodos especiais do django
    #def dispatch(self, *args, **kwargs):
        #self.account_id = kwargs['pk']
    #    return super(AccountDeleteView, self).dispatch(*args, **kwargs)


class ResultsView(generic.DetailView):
    model = Account
    template_name = 'result.html'


################################################################################################
# Category Views

"""
class CategoryIndexView(generic.ListView):
    model = Category
    template_name = 'account/account_list.html'
    context_object_name = 'list' #Returned by queryset

    def get_queryset(self):
        "Return the last five published questions."
        return Category.objects.all()


class CategoryDetailView(generic.DetailView):
    model = Category
    form_class = CategoryForm
    template_name = 'account/detail.html'
    context_object_name = 'content' # name of object used in context
   

class CategoryCreateView(generic.CreateView):
    model = Category
    form_class: CategoryForm 
    template_name = 'account/account_create.html'
    fields = ['name',]
    
    def dispatch(self, *args, **kwargs):
        #self.account_id = kwargs['pk']
        return super(CategoryCreateView, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.save()
        return HttpResponse(render_to_string('account/account_success_update.html'))    


class CategoryUpdateView(generic.UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'account/account_update.html'
    #fields = ['name', 'account_description', 'balance']

    # Estudar mais os metodos especiais do django
    def dispatch(self, *args, **kwargs):
        self.category_id = kwargs['pk']
        return super(CategoryUpdateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.save()
        category = Category.objects.get(id=self.category_id)
        return HttpResponse(render_to_string('account/account_success_update.html', {'account': category}))    


class CategoryDeleteView(generic.DeleteView):
    model = Category
    success_url = reverse_lazy('finance:account_index')
    template_name = 'account/account_confirm_delete.html'

    # Estudar mais os metodos especiais do django
    def dispatch(self, *args, **kwargs):
        #self.account_id = kwargs['pk']
        return super(CategoryDeleteView, self).dispatch(*args, **kwargs)

"""