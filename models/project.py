# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api
log = logging.getLogger(__name__)


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    default_deadline = fields.Date(string='Fecha limite predeterminada')


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def default_get(self, fields_list):
        result = super(ProjectTask, self).default_get(fields_list)

        if result.get('partner_id'):
            partner_id = self.env['res.partner'].browse(result['partner_id'])
            if partner_id.wt_bankcode:
                result.update({'name': partner_id.wt_bankcode})

        if result.get('stage_id'):
            task_type_id = self.env['project.task.type'].browse(result['stage_id'])
            if task_type_id.default_deadline:
                result.update({'date_deadline': task_type_id.default_deadline})
        return result

