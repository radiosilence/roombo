from fabric.api import *
from devops import (
    initialise as _initialise,
    upgrade,
    manage,
    celery,
    restart,
    virtualenv,
    shell,
    _init,
)

env.project = ''
env.repo = 'roombo'
env.app = env.repo
env.application = 'django'
env.debug_host = '0.0.0.0:'


def debug():
    local('./manage.py runserver {}'.format(env.debug_host))


def test(app=None):
    app = app or 'roombo customers instruments reports'
    local('REUSE_DB=1 ./manage.py test {} --settings=roombo.settings.test --with-color --with-fixture-bundling'.format(app))


def initialise(instance, *args, **kwargs):
    if instance == 'test':
        env.domains = ['roombo.linkscreative.co.uk']
    elif instance == 'live':
        env.domains = ['roombo-live.linkscreative.co.uk']
        
    _initialise(instance, *args, **kwargs)
    with virtualenv():
        run('mkdir -p media/uploads')
        if instance == 'test':
            manage('loaddata testdata')