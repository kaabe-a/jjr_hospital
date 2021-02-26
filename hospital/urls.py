from django.urls import path
from . views import hospitalm_list_view,hospital_create_view,hospital_detal_view, \
		hospital_delete_view,hospital_update_view
urlpatterns = [
	path('',hospitalm_list_view,name='list_view'),
	path('create/',hospital_create_view,name='create'),
	path('<int:id>/',hospital_detal_view,name='detail'),
	path('<int:id>/delete/',hospital_delete_view,name='delete'),
	path('<int:id>/update/',hospital_update_view,name='update'),
]