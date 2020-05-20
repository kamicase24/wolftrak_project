# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api
log = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    wt_bancode = fields.Char(string='Código BAN')