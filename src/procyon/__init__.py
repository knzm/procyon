from .base import DBSession

def includeme(config):
    config.include(".base")
    config.include(".user")

    if hasattr(config, 'add_jinja2_search_path'):
        config.add_jinja2_search_path('procyon:templates')
