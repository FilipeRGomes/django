from django.urls import path
from django.views.generic import TemplateView
from . import views
#https://www.abidibo.net/blog/2014/05/26/how-implement-modal-popup-django-forms-bootstrap/
#https://www.abidibo.net/blog/2015/11/18/modal-django-forms-bootstrap-4/
app_name = 'finance'
urlpatterns = [
    path('account', views.AccountIndexView.as_view(), name='index'),
    path('account/detail/<int:pk>/', views.AccountDetailView.as_view(), name='detail'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('account/create/', views.AccountCreateView.as_view(), name='create'),
    path('account/update/<int:pk>/', views.AccountUpdateView.as_view(), name='update'),
    path('account/delete/<int:pk>/', views.AccountDeleteView.as_view(), name='delete'),
    
]

"""
Without Generic Viws
from django.urls import path

from . import views
app_name = 'polls' #Used to specify what app the url belongs in template
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/detail/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
]
"""