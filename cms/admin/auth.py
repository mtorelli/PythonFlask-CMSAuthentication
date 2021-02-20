from cms.admin import admin_bp
from cms.admin.models import User
from flask import render_template, request, redirect, url_for, flash
from flask import session, g
from functools import wraps


def protected(route_function):
    def wrapped_route_function(**kwargs):
        return route_function(**kwargs)
