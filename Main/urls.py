from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home', views.HomeView.as_view(), name='home'),
    url(r'^login', views.LoginView.as_view(), name='login'),
    url(r'^register', views.RegisterView.as_view(), name='register'),
    url(r'^pdf', views.PdfView.as_view(), name='pdf'),
    url(r'^profile/(?P<pk>\d+)/$', views.UserProfileView.as_view(),
        name='profile_details'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^submitPost/$', views.SubmitPost.as_view(), name='submit_post'),
    url(r'^test/$', views.SubjectView.as_view(), name='view_subject'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
