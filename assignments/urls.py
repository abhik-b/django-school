from django.urls import path
from .views import AssignmentDetailView, vote, results, search

app_name = 'assignments'
urlpatterns = [
    # path('', ClasssListView.as_view(), name='class-list'),
    path('<pk>/', AssignmentDetailView.as_view(), name='assignment-detail'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('<int:question_id>/results/', results, name='results'),
    path('search/<class_id>', search, name='search-results'),
    # path('classnotes/<id>/', notes, name='class-notes')
]
