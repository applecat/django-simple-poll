# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, loader
from django.db import transaction
from django.utils import simplejson
from utils import set_cookie
from poll.models import *

def vote(request, poll_pk):
    if request.is_ajax():
        try:
            poll = Poll.objects.get(pk=poll_pk)
        except:
            return HttpResponse('Wrong parameters', status=400)

        item_pk = request.GET.get("item", False)
        if not item_pk:
            return HttpResponse('Wrong parameters', status=400)            
        
        try:
            item = Item.objects.get(pk=item_pk)        
        except:
            return HttpResponse('Wrong parameters', status=400)
                    
        if request.user.is_authenticated():
            user = request.user
        else:
            user = None
        
        vote = Vote.objects.create(
            poll=poll,
            ip=request.META['REMOTE_ADDR'],
            user=user,
            item=item,
        )
        
        response = HttpResponse(status=200)
        set_cookie(response, poll.get_cookie_name(), poll_pk)
        
        return response
    return HttpResponse(status=400)


def poll(request, poll_pk):
    try:
        poll = Poll.objects.get(pk=poll_pk)
    except:
        return HttpResponse('Wrong parameters', status=400)

    items = Item.objects.filter(poll=poll)

    return render_to_response("poll/poll.html", {
        'poll': poll,
        'items': items,
    }, context_instance=RequestContext(request))
    

def result(request, poll_pk):
    try:
        poll = Poll.objects.get(pk=poll_pk)
    except:
        return HttpResponse('Wrong parameters', status=400)
    
    items = Item.objects.filter(poll=poll)
    
    return render_to_response("poll/result.html", {
        'poll': poll,
        'items': items,
    })
