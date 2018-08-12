from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice_id = request.POST.get('choice')
    if not choice_id:
        return render(request, 'polls/detail.html', dict(question=question, error_message="You didn't select a choice."))
    else:
        selected_choice = get_object_or_404(Choice, pk=choice_id)
        selected_choice.vote()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

