# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api
log = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    wt_bankcode = fields.Char(string='Bank code')