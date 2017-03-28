Simple Django poll application.

Installation
------------

```
pip install django-simple-poll
```

Install latest from github:
```
pip install -e git+https://github.com/applecat/django-simple-poll.git#egg=django-simple-poll
```

Requirements
------------
Django 1.10+, Python 2.7, 3.4+

Usage
-----

1. Add 'poll' application in the ``INSTALLED_APPS`` settings:

    ```
    INSTALLED_APPS = (
        ...
        'poll',
    )
    ```

2. Add the poll's url to your urls.py.

    ```
    urlpatterns = [
        ...
        url(r'^poll/', include('poll.urls')),
    ]
    ```

3. Run ```python manage.py migrate```

4. Go to site's admin area and create a new poll:
![82721122-13db-11e7-905a-b90019b0fbde](https://cloud.githubusercontent.com/assets/390483/24417739/393a782a-13f2-11e7-8c09-fd6d0cf228f0.png)

5. Add this tags in your template file to show the poll:

    ```
    {% load poll_tags %}
    ...
    {% poll %}
    ```

6. Check if jQuery is already included on the page. If don't — add it:
```
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
```

7. Make vote, see the results:

![2017-03-28 17 17 10](https://cloud.githubusercontent.com/assets/390483/24410357/8973a134-13db-11e7-9788-94fe3462d1ce.png)
![2017-03-28 17 17 05](https://cloud.githubusercontent.com/assets/390483/24410353/870887e8-13db-11e7-81b6-b5a721696e32.png)


Customization
-------------

Of course, you can (and probably, should) customize Simple Poll's templates. You can simply do this by overriding `base.html`, `poll.html` and `result.html` in `templates/poll` directory.
