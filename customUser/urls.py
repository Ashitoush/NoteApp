from django.urls import path
from .views import (
    signin, signup, signout, userProfile, addNote, readmore, delete, edit
)
urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    path('userProfile/', userProfile, name='userProfile'),
    path('addNote/', addNote, name='addNote'),
    path('readmore/<int:id>', readmore, name='readmore'),
    path('delete/<int:id>', delete, name='delete'),
    path('edit/<int:id>', edit, name='edit'),
]