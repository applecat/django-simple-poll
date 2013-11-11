Simple Django poll application

Usage
=====

1. Add 'poll' application in the ``INSTALLED_APPS`` settings:

INSTALLED_APPS = (
    # ...
    'poll',
)

2. Add the poll's url to your urls.py.

urlpatterns = patterns('',
	# ...
    url(r'^poll/', include('poll.urls')),
)

3. Run python manage.py syncdb or python manage.py migrate poll if you using South.

4. Add this tags in your template file to show poll:

{% load poll_tags %}
{% poll %}
	
-----
Based on https://bitbucket.org/RafRaf/django-poll-system
