from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import HomeView
from myapp.views import CandidateView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', HomeView.as_view(), name='home'),
	path('<int:pk>', CandidateView.as_view(), name='candidate'),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
