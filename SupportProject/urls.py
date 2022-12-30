from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from core.views import ContactFormView, JobsFormView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    path('about/', TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path('mission/', TemplateView.as_view(template_name="pages/mission.html"), name="mission"),
    path('services/', TemplateView.as_view(template_name="pages/services.html"), name="services"),
    path('contacts/', ContactFormView.as_view(), name="contacts"),
    path('jobs/', JobsFormView.as_view(), name="jobs"),
    # path('contact/form/', ContactFormView.as_view(), name='contact_form')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
