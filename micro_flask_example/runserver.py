# -*- coding: utf-8 -*-
import cherrypy
import click

from micro_flask_example import create_app


app = create_app()


def run_dev():
    """
    Run the application using the built-in server.
    """
    app.config.from_object("micro_flask_example.settings_dev")
    app.run()


def run_prod():
    """
    Run the application in the well-established CherryPy
    WSGI server. That server is multithreaded and
    has been production ready for many years.

    .. seealso: http://cherrypy.org/
    """
    app.config.from_object("micro_flask_example.settings_prod")
    cherrypy.config.update({
        "environment": "production",
        "server.socket_host": "0.0.0.0",
        "server.socket_port": 5000,
        "log.screen": True
    })
    cherrypy.tree.graft(app)
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()


@click.command()
@click.option('--dev', 'mode', flag_value='dev')
@click.option('--prod', 'mode', flag_value='prod')
def run(mode):
    """
    Entrypoint to run the application from the
    command line, choosing between the `dev` and
    `prod` modes.
    """
    if mode == 'dev':
        run_dev()
    elif mode == 'prod':
        run_prod()


if __name__ == '__main__':
    run()
