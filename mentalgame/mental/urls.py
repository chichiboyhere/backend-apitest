from django.urls import path
from .import views

urlpatterns=[
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('postMyResult/', views.postMyResult, name='post-my-result'),
    path('register/', views.registerUser, name='register'),
    path('getMyResults/', views.getMyResults, name='get-my-results'),
    path('getQuantitativeSpsec/', views.getQuantitativeSpsec, name='getQuantitativeSpsec'),
    path('postQuantitativeSpsec/', views.postQuantitativeSpsec, name='postQuantitativeSpsec'),
    path('getVerbalSpsec/', views.getVerbalSpsec, name='getVerbalSpsec'),
    path('postVerbalSpsec/', views.postVerbalSpsec, name='postVerbalSpsec')
]