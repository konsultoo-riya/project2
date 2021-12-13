

from datetime import datetime

from dateutil.relativedelta import relativedelta as rd

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class ResPartnerExt(models.Model):

    _inherit = 'res.partner'
    _description = 'Partner'

    @api.constrains("email")
    def clear_duplicates(self):
        duplicate_contacts = []
        user_obj = self.env['res.users']
        cale_obj = self.env['calendar.contacts']
        for partner in self:
            if partner.email and partner.id not in duplicate_contacts:
                duplicates = self.search([('id', '!=', partner.id), ('email', '=', partner.email)])
                if duplicates:
                    raise ValidationError(
                        _("This email is already set to customer try another")
                    )

                for dup in duplicates:
                    user = user_obj.search([('partner_id', '=', dup.id)])
                    calender = cale_obj.search([('partner_id', '=', dup.id)])
                    if not user and not calender:
                        duplicate_contacts.append(dup.id)
        self.browse(duplicate_contacts).unlink()
