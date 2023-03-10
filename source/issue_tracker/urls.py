from django.urls import path
from issue_tracker.views.tasks import IndexView, CreateTask, TaskDetail, TaskUpdate, DeleteTask
from issue_tracker.views.projects import ProjectsView, ProjectDetail, ProjectCreateView, ProjectUpdateView, \
    DeleteProjectView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("add/task/", CreateTask.as_view(), name='create_task'),
    path('detail/task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task/delete/<int:pk>/', DeleteTask.as_view(), name='task_delete'),
    path('projects/', ProjectsView.as_view(), name='index_projects'),
    path("add/project/", ProjectCreateView.as_view(), name='create_project'),
    path('detail/project/<int:pk>', ProjectDetail.as_view(), name='project_detail'),
    path('project/update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/delete/<int:pk>/', DeleteProjectView.as_view(), name='project_delete'),
]
