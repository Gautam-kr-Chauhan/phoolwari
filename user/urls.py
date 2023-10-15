from django.urls import path
from user.views import signup,signin,signout
urlpatterns = [
    path('sign up/',signup,name='signup'),
    path('sign in/',signin,name='signin'),
    path('sign out/',signout,name='signout'),
    # path('add_flowers/',add_flowers,name='add_flowers')
    
]
