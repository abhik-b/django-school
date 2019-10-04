from django.urls import path
from .views import ProjectDetailView, search
from django.conf.urls.static import static
from django.conf import settings
app_name = 'projects'
urlpatterns = [
    # path('', ClasssListView.as_view(), name='class-list'),
    path('<pk>/', ProjectDetailView.as_view(), name='projects-detail'),
    path('search/<class_id>', search, name='search-results'),
    # path('classnotes/<id>/', notes, name='class-notes')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
