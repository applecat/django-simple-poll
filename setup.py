from setuptools import setup, find_packages

# Dynamically calculate the version based on django.VERSION.
version = __import__('poll').get_version()

print find_packages()

setup(
    name='django-simple-poll',
    version=version,
    description='Django simple poll application',
    author='Dmitry Akinin',
    author_email='d.akinin@gmail.com',
    url='https://github.com/applecat/django-simple-poll',
    download_url='https://github.com/applecat/django-simple-poll/tarball/v0.1.3',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
)
