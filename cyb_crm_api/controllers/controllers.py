# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class CrmLead(http.Controller):

    @http.route('/create_crm_lead', type='json', auth='user', methods=['POST'])
    def create_crm_lead(self, **kw):
        try:
            data = request.httprequest.data
            json_load = json.loads(data)
            name = json_load.get('name')
            email_from = json_load.get('email_from')
            phone = json_load.get('phone')
            expected_revenue = json_load.get('expected_revenue')
            probability = json_load.get('probability')
            date_deadline = json_load.get('date_deadline')

            if not name:
                return {'status': 400, 'error': "The 'name' field is required."}

            crm_lead = request.env['crm.lead'].sudo().create({
                'name': name,
                'email_from': email_from,
                'phone': phone,
                'expected_revenue': expected_revenue,
                'probability': probability,
                'date_deadline': date_deadline,
            })

            data = {'status': 200, 'message': "Crm Lead created successfully", 'crm_lead': crm_lead.id}
            return data
        except Exception as e:
            return json.dumps({'error': str(e)})

