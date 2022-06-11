from django.urls import path
from myboard.views import view1

urlpatterns = [ # 웹페이지 위치
    path('list', view1.listFunc),
    
    path('insert', view1.insertFunc),
    path('insertok', view1.insertOkFunc),
    
    path('search', view1.searchFunc),
    
    path('content', view1.contentFunc),
    
    path('update', view1.updateFunc),
    path('updateok', view1.updateOkFunc),
    
    path('delete', view1.deleteFunc),
    path('deleteok', view1.deleteOkFunc),
    
]