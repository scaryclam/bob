from flask import Blueprint

from viewer import views


urls = [
    ['', views.SummaryView.as_view('index')],
]


def create_routes(application):
    bp = Blueprint('api', __name__, url_prefix='/')

    for url in urls:
        bp.add_url_rule(rule=url[0], view_func=url[1])
    application.register_blueprint(bp)
