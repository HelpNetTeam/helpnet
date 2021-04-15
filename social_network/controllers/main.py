from odoo.http import Controller, route, request
import requests
import json

class MyController(Controller):
    @route('/jwt-auth', auth='none', type='json')
    def handler(self):
        login = request.jsonrequest.['args']['login']
        login = request.jsonrequest.['args']['login']

        response = requests.get('http://localhost:8069/jsonrpc', json=request.jsonrequest)
        return json.loads(response.content).get('result')


