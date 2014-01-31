# -*- coding: utf-8 -*-

import datetime
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.db.models.manager import Manager
from django.core.exceptions import ValidationError


class PublishedManager(Manager):
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set().filter(is_published=True)

class Poll(models.Model):
    title = models.CharField(max_length=250, verbose_name=_('question'))
    date = models.DateField(verbose_name=_('date'), default=datetime.date.today)
    is_published = models.BooleanField(default=True, verbose_name=_('is published'))

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-date']
        verbose_name = _('poll')
        verbose_name_plural = _('polls')

    def __unicode__(self):
        return self.title

    def get_vote_count(self):
        return Vote.objects.filter(poll=self).count()
    vote_count = property(fget=get_vote_count)

    def get_cookie_name(self):
        return str('poll_%s' % (self.pk))


class Item(models.Model):
    poll = models.ForeignKey(Poll)
    value = models.CharField(max_length=250, verbose_name=_('value'))
    pos = models.SmallIntegerField(default='0', verbose_name=_('position'))

    class Meta:
        verbose_name = _('answer')
        verbose_name_plural = _('answers')
        ordering = ['pos']

    def __unicode__(self):
        return u'%s' % (self.value,)

    def get_vote_count(self):
        return Vote.objects.filter(item=self).count()
    vote_count = property(fget=get_vote_count)


class Vote(models.Model):
    poll = models.ForeignKey(Poll, verbose_name=_('poll'))
    item = models.ForeignKey(Item, verbose_name=_('voted item'))
    ip = models.IPAddressField(verbose_name=_('user\'s IP'))
    user = models.ForeignKey(get_user_model(), blank=True, null=True,
                             verbose_name=_('user'))
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('vote')
        verbose_name_plural = _('votes')

    def __unicode__(self):
        user = get_user_model()
        if isinstance(self.user, user):
            return getattr(user, user.USERNAME_FIELD)
        return self.ip
