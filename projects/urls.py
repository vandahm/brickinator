from django.urls import path
from . import views

app_name = 'studio'

'''
app/projects/
app/projects/1/
app/projects/1/collaborators/
app/projects/1/collaborators/edit/
app/projects/1/studio/
app/projects/1/instructions/
'''


urlpatterns = [
    path('', views.list, name='index'), # list projects
    path('', views.detail, name='detail'), # project detail view
    path()

]