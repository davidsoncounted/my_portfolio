from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib import admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('contact', views.contact, name = 'contact'),
    path('portfolio-details/<str:pk>/', views.portfolio, name = 'portfolio-details'),
    path('form', views.rate, name = 'form'),
    path('unapproved', views.unapproved_ref, name = 'unapproved'),
    path('ref', views.ref_list, name = 'ref'),
    path('create-post', views.create_post, name = 'create-post'),
    path('category', views.category, name = 'category'),
    path('portfolio', views.portfolio_page, name = 'portfolio'),
    path('download', views.download, name = 'download'),
    path('approve/<str:pk>/', views.approve_ref, name = 'approve'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
