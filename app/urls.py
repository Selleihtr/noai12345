from django.urls import path
import app.views

urlpatterns = [
    path('', view=app.views.index_view),
    path('datatables.net/', view=app.views.datatables_net),
]