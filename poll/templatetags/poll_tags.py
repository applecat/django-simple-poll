# -*- coding: utf-8 -*-

from django import template
from django.template.loader import render_to_string
from django.utils.html import format_html
from poll.models import *
from poll import views
register = template.Library()


@register.simple_tag(takes_context=True)
def poll(context):
    request = context['request']

    try:
        poll = Poll.published.latest("date")
    except Poll.DoesNotExists:
        return ''

    items = Item.objects.filter(poll=poll)

    if poll.get_cookie_name() in request.COOKIES:
        template = "poll/result.html"
    else:
        template = "poll/poll.html"

    content = render_to_string(template, {
        'poll': poll,
        'items': items,
    })

    return content


@register.simple_tag                                                                                                                         
def percentage(poll, item):
    poll_vote_count = poll.get_vote_count()
    if poll_vote_count > 0:
        return float(item.get_vote_count()) / float(poll_vote_count) * 100
