
from django.contrib import admin
from django.urls import include, path 

urlpatterns = [
    path("", include("G_agence.urls")),  # Redirect the empty path to the "G_agence" app URLs
    path('admin/', admin.site.urls),
    path('api/', include('G_agence.urls')),  # Include the 'G_agence' app API URLs under the 'api/' prefix
    # You can add more app URLs or API URLs here
]

