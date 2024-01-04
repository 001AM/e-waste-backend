app_name = 'base'

from django.urls import path
from base.api.views import CustomUserView, BlacklistTokenView, CustomUserDetailView, CustomUserProductView,CustomUserProductSellerView, LoginView, EducationView
from base.register.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', CustomUserView.as_view(), name='register'),
    path('details/', CustomUserDetailView.as_view(), name='userdetail'),
    path('products/', CustomUserProductView.as_view(), name='products'),
    path('products/seller/', CustomUserProductSellerView.as_view(), name='seller'),
    path('logout/blacklist/', BlacklistTokenView.as_view(), name='blacklist'),
    path('login/', LoginView.as_view(), name='token_login'),
   # path('logout/', LogoutView.as_view(), name='token_login'),
    path('education/', EducationView.as_view(), name='education'),
    path('events/', EventCardView.as_view(), name='eventcard'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL ,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)