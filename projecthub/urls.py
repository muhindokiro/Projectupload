from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.project_today,name='projectToday'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^new/review$', views.new_review, name='new-review'),
    url(r'^profile$', views.profile, name='profile')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)