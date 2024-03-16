from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin_tools/', include('admin_tools.urls')),

    path("admin/", admin.site.urls),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('reviews.urls')),

]

admin.site.site_header = "FLIX-API ADMINISTRATION"
admin.site.site_title = "Flix-API Administration"
