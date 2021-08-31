from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('blog_grid_sidebar', views.blog_grid_sidebar,name='blog_grid_sidebar'),
    path('accounts', views.accounts,name='accounts'),
    # path('assets', views.assets,name='assets'),
    # path('procurement', views.procurement,name='procurement'),
    # path('production', views.production,name='production'),
    path('page_about_us', views.page_about_us,name='page_about_us'),
    path('page_contact', views.page_contact,name='page_contact'),
    # path('page_careers', views.page_careers,name='page_careers'),
    # path('enquiry/contact_lead/', views.contact_lead, name='contact_lead'),

    # path('support', views.support,name='support'),
    path('products', views.products,name='products'),
    path('Gallery', views.gallery,name='gallery'),
    # path('Terms&Conditions', views.Terms_Conditions,name='Terms&Conditions'),
    # path('CRM', views.CRM,name='CRM'),
    # path('pms', views.pms,name='pms'),
    # path('selling', views.selling,name='selling'),
    # path('clients', views.clients,name='clients'),
    # path('HRMS', views.HRMS,name='HRMS'),
    # path('coming_soon', views.coming_soon,name='coming_soon'),
    # path('enquiry/contact_lead/free_demo', views.contact_lead,name='contact_lead'),
    # path('manufacturing', views.manufacturing,name='manufacturing'),
    # path('stock_inventory', views.stock_inventory,name='stock_inventory'),
    # path('policy', views.policy,name='policy'),
    # path('consulting', views.consulting,name='consulting'),
    path('index1',views.PostList.as_view(),name='blog_grid_sidebar'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
