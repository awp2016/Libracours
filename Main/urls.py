from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^profile/(?P<pk>\d+)/$', views.UserProfileView.as_view(), name='profile_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
