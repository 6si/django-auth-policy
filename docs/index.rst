.. _index:

==================
Django Auth Policy
==================

Quick setup
===========

* Install ``django_auth_policy`` using pip, easy_install or the
  provided setup.py.

* Add ``django_auth_policy`` to Django setting ``INSTALLED_APPS``.

* Add ``django_auth_policy.middleware.AuthenticationPolicyMiddleware`` to the
  Django setting ``MIDDLEWARE_CLASSES``, make sure to include it *after*
  Django's ``AuthenticationMiddleware``.

* Use the authentication form and the change password forms from
  ``django_auth_policy.forms``.

.. FIXME: Full example of log-in, log-out and change password views

* Add policies to your settings, a good starting point can be::

    AUTHENTICATION_POLICIES = (
        ('django_auth_policy.authentication.AuthenticationBasicChecks', {}),
        ('django_auth_policy.authentication.AuthenticationDisableExpiredUsers', {}),
        ('django_auth_policy.authentication.AuthenticationLockedUsername', {}),
        ('django_auth_policy.authentication.AuthenticationLockedRemoteAddress', {}),
    )

    PASSWORD_STRENGTH_POLICIES = (
        ('django_auth_policy.password_strength.PasswordMinLength', {}),
        ('django_auth_policy.password_strength.PasswordContainsUpperCase', {}),
        ('django_auth_policy.password_strength.PasswordContainsLowerCase', {}),
        ('django_auth_policy.password_strength.PasswordContainsNumbers', {}),
        ('django_auth_policy.password_strength.PasswordContainsSymbols', {}),
        ('django_auth_policy.password_strength.PasswordUserAttrs', {}),
        ('django_auth_policy.password_strength.PasswordDisallowedTerms', {
            'terms': ['Testsite']
        }),
    )

    PASSWORD_CHANGE_POLICIES = (
        ('django_auth_policy.password_change.PasswordChangeExpired', {}),
        ('django_auth_policy.password_change.PasswordChangeTemporary', {}),
    )

  Update the ``terms`` of ``PasswordDisallowedTerms`` to a list of terms one
  does not allow in passwords. Like the name and domainname of the current site.

.. FIXME: Add references to explanation of individual policies

* For Django >= 1.7 run the ``./manage.py check`` command as a sanity check to
  see if everything is in place. This command is **NO guarantee** that all
  policies are enforced since it's easy for developers to work around the checks
  performed by this command.
