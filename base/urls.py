app_name = 'base'

from django.urls import path
from base.api.views import CustomUserView, BlacklistTokenView, CustomUserDetailView, CustomUserProductView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', CustomUserView.as_view(), name='register'),
    path('details/', CustomUserDetailView.as_view(), name='userdetail'),
    path('products/', CustomUserProductView.as_view(), name='userdetail'),
    path('logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL ,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)