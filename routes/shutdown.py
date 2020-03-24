from flask import request, current_app, Blueprint



shutdown = Blueprint('shutdown', __name__)


def __shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@shutdown.route('/')
def __shutdown():
    __shutdown_server()
    return 'Server shutting down...'