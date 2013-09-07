====================
procyon
====================

Overview
--------------------

procyon is a collection of reusable components for Pyramid.

Currently, it includes the following components:

- A base model and a DB session that is configured in the common way.
- A user model and login/logout views.
- Some common panels.

Especially, the base model is not required.
You can also use the user model with your own base model.

Setup
--------------------

Use the :meth:`Configurator.include` method:

.. code-block:: python

  config = Configurator()
  config.include('procyon')

or add procyon to the ``pyramid.includes`` list in your ini file:

::

  pyramid.includes =
      procyon

Both are equivalent.

Using models
--------------------

There are various cases to define and use models with procyon.

Use the default base model with your own user model (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define a model class in your code that looks like:

.. code-block:: python

  from procyon import BaseModel, UserModelMixin

  class UserModel(BaseModel, UserModelMixin):
      __tablename__ = 'user'

then, set it via the configurator:

.. code-block:: python

  config.set_user_model(UserModel)

You can still choose not to use :class:`UserModelMixin`.  In this
case, the model should provides :class:`procyon.user.IUserModel`.

Create a default user model and use it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Simply, call :meth:`Configurator.set_default_user_model` method with
an optional ``tablename`` argument.

.. code-block:: python

  config.set_default_user_model(tablename='user')

If you want to get the user model later, use :meth:`request.get_user_model` API.

Use your own base model (advanced)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

  from procyon import UserModelMixin

  class UserModel(YourBaseModel, UserModelMixin):
      __tablename__ = 'user'

``YourBaseModel`` is any class you defined somewhere that provides
:class:`IBaseModel`.

Using views
--------------------

:class:`~procyon.user.views.BaseLoginView` and
:class:`~procyon.user.views.BaseLogoutView` are provided.
All you need is to override them and to define some lacking methods.

.. code-block:: python

  from procyon.user.views import BaseLoginView, BaseLogoutView
  from yourapp.security import login

  class LoginView(BaseLoginView):
      def do_login(self, user_name, password):
          # you should return a (userid, headers) tuple
          return login(self.request, user_name, password)
  
      def get_redirect_url(self):
          # return any url you want to redirect to after login
          return self.request.route_url('top')

  class LogoutView(BaseLogoutView):
      def get_redirect_url(self):
          # return any url you want to redirect to after logout
          return self.request.route_url('top')

LoginView and LogoutView are now class views ready to register via
:func:`view_config` or :meth:`Configurator.add_view`.

.. note::

  If you use :mod:`repoze.who`, :func:`login` function in the above
  example can be defined like this:

  .. code-block:: python
      
    def login(request, user_name, password):
        from repoze.who.api import get_api
        who_api = get_api(request.environ)
    
        credentials = {
            'login': user_name,
            'password': password,
            }
        return who_api.login(credentials)

Using panels
--------------------

procyon also provides some 'panels' for :mod:`pyramid_panels`.

There are some extra requirements for this functionality:

- :mod:`pyramid_panels`
- :mod:`pyramid_jinja2`
- Twitter Bootstrap CSS

All available panels are listed here.

.. function:: panel('flash', queue='')

  Show a flash message area.
  ``queue`` is the queue name. Default is ``""``.

  This panel requires some session factory to be set up.
  See the 'Session' chapter in the Pyramid documentation for detail.

.. function:: panel('login_menuitem')

  Show a login menu item.  A user model must be configured as
  described in the above section.

If you already enable :mod:`pyramid_panels`, you can then use them
with the following configuration:

.. code-block:: python

    config.include('procyon.panels')
