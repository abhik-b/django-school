from django.urls import path
from .views import NoteDetailView, search
app_name = 'notes'
urlpatterns = [
    # path('', ClasssListView.as_view(), name='class-list'),
    path('<pk>/', NoteDetailView.as_view(), name='notes-detail'),
    path('search/<class_id>', search, name='search-results'),
    # path('classnotes/<id>/', notes, name='class-notes')
]
