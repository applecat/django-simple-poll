try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('poll.views',
    url(r'^vote/(?P<poll_pk>\d+)/$', 'vote', name='poll_ajax_vote'),
    url(r'^poll/(?P<poll_pk>\d+)/$', 'poll', name='poll'),
    url(r'^result/(?P<poll_pk>\d+)/$', 'result', name='poll_result'),
)
