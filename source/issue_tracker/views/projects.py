from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from issue_tracker.forms.project_form import ProjectForm
from issue_tracker.models import Project


class ProjectsView(ListView):
    template_name = 'project_templates/index_projects.html'

    model = Project
    context_object_name = 'projects'
    ordering = ('created_at',)
    paginate_by = 10
    paginate_orphans = 1

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        return queryset


class ProjectCreateView(CreateView):
    template_name = 'project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDetail(DetailView):
    template_name = 'project_templates/project_detail.html'
    model = Project


class ProjectUpdateView(UpdateView):
    template_name = 'project_templates/project_update.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class DeleteProjectView(DeleteView):
    template_name = 'project_templates/confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index_projects')
