from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse

from .models import Thread, Post


class IndexView(generic.ListView):
    template_name = 'forum/index.html'
    context_object_name = "thread_list"

    def get_queryset(self):
        return Thread.objects.order_by('-pub_date')
    
    
class DetailView(generic.DetailView):
    model = Thread
    template_name = 'forum/detail.html'


def new_post(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    try:
        post_text = request.POST['post_text']
        if post_text == "":
            raise ValueError()
    except ValueError:
        return render(request, "forum/detail.html", {
            'thread': thread,
            'error_message': "You didn't write anything",
        })
    except KeyError:
        return render(request, "forum/detail.html", {
            'thread': thread,
            'error_message': "Something goes wrong",
        })
    else:
        thread.post_set.create(post_text=post_text, pub_date=timezone.now(), post_author=request.user)
        return HttpResponseRedirect(reverse('forum:detail', args=(thread_id,)))


def new_thread(request):
    try:
        theme = request.POST['theme']
        post_text = request.POST['post_text']
        if theme == "":
            raise ValueError("empty theme")
        if post_text == "":
            raise ValueError("empty post")
    except ValueError as err:
        return render(request, "forum/index.html", {
            'thread_list': Thread.objects.order_by('-pub_date'),
            'error_message': "Error: " + err.args[0],
        })
    except KeyError:
        return render(request, "forum/index.html", {
            'thread_list': Thread.objects.order_by('-pub_date'),
            'error_message': "Something goes wrong",
        })
    else:
        thread = Thread(theme=theme, pub_date=timezone.now())
        thread.save()
        thread.post_set.create(post_text=post_text, pub_date=timezone.now(), post_author=request.user)
        return HttpResponseRedirect(reverse('forum:detail', args=(thread.id,)))
    