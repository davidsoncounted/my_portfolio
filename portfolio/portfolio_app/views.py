from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact, Portfolio, Resume, Rate, Resume_details, About, Skills, Resume_responsibility, Portfoliocategory
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from .form import ref_form, post_form
from django.db.models import Q
from django.conf import settings
import os

 

def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # choose = Portfolio.objects.filter(Q(category__name__icontains=q)).order_by('-created')

    cate = Portfolio.objects.all()
    portfolio = Portfolio.objects.all() 
    resume = Resume.objects.all()  
    resume_details = Resume_details.objects.all()
    categories = Portfoliocategory.objects.all()
    about = About.objects.all()
    skills = Skills.objects.all()
    # web_choice = Portfolio.objects.filter(web_development = True)
    reference = Rate.objects.filter(approve=False)
    approved_ref = Rate.objects.filter(approve=True)
    context = {'portfolio': portfolio, 'about':about, 'skills':skills, 'reference': reference, 'categories': categories, 'resume_details': resume_details, 'cate': cate,'resume': resume, 'ref': approved_ref}
    return render(request, 'index.html',context)
   

def portfolio_page(request):
    portfolio = Portfolio.objects.all()
    categories = Portfoliocategory.objects.all()
    context = {'portfolio': portfolio, 'categories': categories}
    return render(request, 'portfolio.html', context ) 

def portfolio(request, pk):

    portfolio_details = Portfolio.objects.get(id=pk)
    context = {'portfolio_details': portfolio_details}
    return render(request, 'portfolio-details.html', context)  

login_required(login_url= 'index')
def create_post(request):
    port_form = post_form() 
    if request.method == 'POST':
        port_form = post_form(request.POST, request.FILES)
        if port_form.is_valid():
            port_form.save()
            messages.success(request, 'Post successful')
            return redirect('portfolio')
        else:
            messages.error(request, 'post not successful')
            return redirect('create-post')
    context = {'port_form': port_form}
    return render(request, 'post.html', context)


def category (request):
    category = request.GET.get('category')
    if category == None:
        portfolio = Portfolio.objects.all()

    else: 
        portfolio = Portfolio.objects.filter(category__projectCategory= category)


    categories = Portfoliocategory.objects.all()
    context = {'portfolio': portfolio, 'categories': categories}
    # Your other view logic here
    return render(request, 'portfolio.html', context)  
   

def contact(request):
    if request.method == 'POST':
        contact = Contact(name = request.POST.get('name'), email = request.POST.get('email'), 
                          subject = request.POST.get('subject'), message = request.POST.get('message'))
        contact.save()
        messages.success(request, 'Your messge was sent successfully')
        return HttpResponseRedirect('/')
    else:  
        messages.error(request, 'Error: something happened')
        
      
        
def rate(request):
    # reference = Rate.objects.filter(approve=False)
    form = ref_form()
    if request.method == 'POST':
        form = ref_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'thanks for your reviews..')
            return redirect('index')
        else:
            form = ref_form()
            messages.error(request, 'something went wrong')
            return redirect('form')
    context = {'form': form}
    return render(request, 'ref-form.html', context) 

@login_required(login_url= 'index')
def approve_ref(request, pk):
    ref = get_object_or_404(Rate, pk=pk) 
    ref.approve_ref()
    return redirect('/', pk=ref.pk)

def ref_list(request):
    approved_ref = Rate.objects.filter(approve=True)
    context = {'ref': approved_ref}
    return render(request, 'index.html', context)

@login_required(login_url= '/')
def unapproved_ref(request):
    reference = Rate.objects.filter(approve=False)
    context = {'reference': reference} 
    return render(request, 'unapproved_tes.html', context)

def download(request):
    file = os.path.join(settings.BASE_DIR, "cv_download/Davidson's Cv.pdf")
    open_file = open(file, 'rb')

    return FileResponse(open_file)
