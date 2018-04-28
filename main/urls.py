from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload-form', views.upload_form, name='upload-form'),
    path('faq', views.faq, name='faq'),
    # path('case-lookup', views.case_lookup, name='case-lookup'),
    # path('case/<str:case_id>/', views.case_details, name='case-details'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('doc-link-test', views.doc_link_test),
    path('case/document/<uuid:doc_uuid>', views.view_document, name='view-document'),
]
