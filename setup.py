#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='django-auth-policy',
    version='0.9.11.dev',
    zip_safe=False,
    description='Enforces a couple of common authentication policies for the '
                'Django web framework.',
    author='Rudolph Froger',
    author_email='rudolphfroger@dreamsolution.nl',
    maintainer='Rudolph Froger',
    maintainer_email='rudolphfroger@dreamsolution.nl',
    url='https://github.com/rudolphfroger/django-auth-policy',
    license='BSD',
    packages=find_packages(exclude=["testsite", "testsite.*", "*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'django_auth_policy': ['locale/*/LC_MESSAGES/*.mo',
                                         'locale/*/LC_MESSAGES/*.po']},
    install_requires=['Django>=1.7'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Security',
        'Topic :: Internet :: WWW/HTTP :: Session',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
