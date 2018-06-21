# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

from .utils import set_cookie
from .models import Poll, Item, Vote


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

        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

        Vote.objects.create(
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
    except Poll.DoesNotExists:
        return HttpResponse('Wrong parameters', status=400)

    items = Item.objects.filter(poll=poll)

    return render(request, "poll/poll.html", {
        'poll': poll,
        'items': items,
    })


def result(request, poll_pk):
    try:
        poll = Poll.objects.get(pk=poll_pk)
    except Poll.DoesNotExists:
        return HttpResponse('Wrong parameters', status=400)

    items = Item.objects.filter(poll=poll)

    return render(request, "poll/result.html", {
        'poll': poll,
        'items': items,
    })
