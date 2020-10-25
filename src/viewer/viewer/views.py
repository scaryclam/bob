import json

from flask import Response
from flask.views import MethodView

from viewer.services import JobService



class SummaryView(MethodView):
    def get_context_data(self):
        service = JobService()
        jobs = service.get_active_jobs()
        return {'jobs': jobs}

    def get(self):
        payload = self.get_context_data()
        response = Response(
            json.dumps(payload), 200, {'Content-type': 'application/json'})
        return response
