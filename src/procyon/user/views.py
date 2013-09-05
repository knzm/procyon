# -*- coding: utf-8 -*-

import colander as c
import deform.widget as w
from pyramid.view import view_config
from pyramid import security
from pyramid.httpexceptions import HTTPFound
from pyramid_deform import FormView


class LoginSchema(c.Schema):
    user_name = c.SchemaNode(c.String(), title=u"ユーザ名")
    password = c.SchemaNode(c.String(), title=u"パスワード",
                            widget=w.PasswordWidget())


class BaseLoginView(FormView):
    schema = LoginSchema()
    buttons = ('login',)

    def do_login(self, user_name, password):
        raise NotImplementedError

    def get_redirect_url(self):
        raise NotImplementedError

    def login_success(self, values):
        user_name = values['user_name']
        password = values['password']
        userid, headers = self.do_login(user_name, password)
        if userid is None:
            self.request.session.flash(u"ユーザ名とパスワードが一致しません")
            return

        response = HTTPFound(self.get_redirect_url())
        response.headerlist.extend(headers)
        return response


class BaseLogoutView(object):
    def __init__(self, request):
        self.request = request

    def get_redirect_url(self):
        raise NotImplementedError

    def __call__(self):
        headers = security.forget(self.request)
        response = HTTPFound(self.get_redirect_url())
        response.headerlist.extend(headers)
        self.request.session.flash(u"ログアウトしました")
        return response
