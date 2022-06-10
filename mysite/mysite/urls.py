from django.contrib import admin
from django.urls import include, path

from myboard.views import view1 # 지정 
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')), # 위임

    path('board/', include('myboard.urls')), # board/ 들어 왔을 경우 위임
]
