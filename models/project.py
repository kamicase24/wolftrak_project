# -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta
import logging
from odoo import models, fields, api
log = logging.getLogger(__name__)


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    default_deadline = fields.Integer(string='Días para la fecha limite predeterminada')


class ProjectTask(models.Model):
    _inherit = 'project.task'

    @api.model
    def default_get(self, fields_list):
        result = super(ProjectTask, self).default_get(fields_list)

        if result.get('user_id'):
            user_id = self.env['res.users'].search([('login', '=', 'dpstac@wolftrakglobal.com')], limit=1)
            if user_id:
                result.update({'user_id': user_id.id})

        if result.get('partner_id'):
            partner_id = self.env['res.partner'].browse(result['partner_id'])
            if partner_id.wt_bancode:
                result.update({'name': partner_id.wt_bancode})

        if result.get('stage_id'):
            task_type_id = self.env['project.task.type'].browse(result['stage_id'])
            if task_type_id.default_deadline:
                today = date.today()
                log.info("today %s" % today)
                deadline = today + timedelta(days=task_type_id.default_deadline)
                log.info("deadline %s " % deadline)
                week_day = deadline.isoweekday()
                if week_day == 6:
                    log.info("sabado")
                    deadline = today + timedelta(days=task_type_id.default_deadline+2)
                if week_day == 7:
                    log.info("domingo")
                    deadline = today + timedelta(days=task_type_id.default_deadline+1)

                result.update({'date_deadline': deadline})
        return result

    @api.onchange('partner_id')
    def onchange_partner(self):
        if self.partner_id:
            if self.partner_id.wt_bancode:
                self.name = self.partner_id.wt_bancode
            else:
                self.name = ''
        else:
            self.name = ''