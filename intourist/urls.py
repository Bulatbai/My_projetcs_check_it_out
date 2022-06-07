
from django.urls import path
from . views import homepage, pirofile
urlpatterns = [
    path('res/', homepage, name='HHomepage' ),
    path('react/', pirofile, name='P_file')
]



