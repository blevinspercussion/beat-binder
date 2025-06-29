from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Score 
from .forms import ScoreForm 
from django.contrib.auth.decorators import login_required

class ScoreListView(LoginRequiredMixin, ListView):
    model = Score 
    template_name = 'scores/scores_list.html'
    context_object_name = 'scores'
    queryset = Score.objects.filter(public=True).order_by('-created_at')
    paginate_by = 10

class ScoreDetailView(LoginRequiredMixin, DetailView):
    model = Score 
    template_name = 'scores/score_detail.html'
    context_object_name = 'score'

class ScoreCreateView(LoginRequiredMixin, CreateView):
    model = Score 
    form_class = ScoreForm 
    template_name = 'scores/score_form.html'
    success_url = reverse_lazy('scores:score_list')

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)