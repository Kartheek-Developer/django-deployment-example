from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,TemplateView, DetailView,
                                  ListView,CreateView,UpdateView,DeleteView)
from . import models

# Create your views here.

class SchoolListView(ListView):
    # context_object_name = 'schools'
    model = models.School
    #it will create an object called school_list and
    # school_list.html is the default template name for ListView. If u r using ListView then
    # Django searches for school_list.html automatically.So u don't need to mention template name explicitly.
    # However if u r using other name for template other than school_list.html,
    # then u should mention template name in your views class.

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")

class IndexView(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'BASIC INJECTION'
    #
    #     return context



