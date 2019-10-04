from django.urls import path
from .views import ClasssListView, ClasssDetailView, notes, projects, assignments, attendancecheck
app_name = 'classs'
urlpatterns = [
    path('', ClasssListView.as_view(), name='class-list'),
    path('<pk>/', ClasssDetailView.as_view(), name='class-detail'),
    path('classnotes/<id>/', notes, name='class-notes'),
    path('classprojects/<id>/', projects, name='class-projects'),
    path('classassignments/<id>/', assignments, name='class-assignments'),
    path('classattcheck/<id>', attendancecheck, name='class-att-check')
]
