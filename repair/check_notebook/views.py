from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, FormView

from .forms import InputSeriesForm
from repair_home.models import InfoTmp


class CheckNoteBook(View):
    template_name = 'main/check_notebooks.html'
    form_class = InputSeriesForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            series = form.cleaned_data['series']
            data = InfoTmp.objects.all()
            return render(request, 'main/notebook_search_ok.html', {'detail_notebook': data})

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form}
        return render(request, self.template_name, context)
