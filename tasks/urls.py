
from django.urls import path
from tasks.views import maanger_dashboard, jk,second_page,test,test_2,test_3

urlpatterns = [
    path('manager-dashboard/', maanger_dashboard),
    path('jk/', jk),# এখানে "jk.html" নয়, jk হবে
    path('second-page/', second_page),
    path('test/',test),
    path('test_2/',test_2),
    path('test_3/',test_3)
]
