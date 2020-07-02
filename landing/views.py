from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from urllib.parse import urlencode
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import Choice,Question

import json

def login(request):
    return render(request, 'landing/index.html')

def token(request):
    return render(request, 'landing/results.html')

def profile(request):
    return render(request, 'landing/detail.html')

def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect('http://tukangtempe.herokuapp.com/landing/dashboard')
    else:
        return render(request, 'landing/index.html')

@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email'],
    }

    return render(request, 'landing/dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })

def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/landing/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)

# class IndexView(generic.ListView):
#     template_name = 'landing/index.html'
#     context_object_name = 'latest_question_list'
    
#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]
    
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'landing/detail.html'

# class ResultView(generic.DetailView):
#     model = Question
#     template_name = 'landing/results.html'

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'landing/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('landing:results', args=(question.id,)))
