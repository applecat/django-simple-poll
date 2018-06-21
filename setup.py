from setuptools import setup, find_packages

# Dynamically calculate the version based on django.VERSION.
version = __import__('poll').get_version()


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='django-simple-poll',
    version=version,
    author='Dmitry Akinin',
    author_email='d.akinin@gmail.com',
    description='Django simple poll application',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/applecat/django-simple-poll',
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
