# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, http
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from datetime import datetime, timedelta
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
import logging
import base64

_logger = logging.getLogger(__name__)


class CustomersPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        # Fetching sale orders for the current user's customer
        sale_orders = self.env['sale.order'].search([
            ('partner_id', '=', self.env.user.partner_id.id),
            ('state', '=', 'sale')  # Adjust state as needed
        ])

        values.update({
            'sale_orders': sale_orders,  # Adding sale orders to values
        })

        return values
    
    @http.route(['/my/subscription_packages', '/my/subscription_packages/page/<int:page>'],
                type='http', auth='user', website=True)
    def portal_my_subscription_packages(self, page=1, **kw):
        values = self._prepare_portal_layout_values()
        SubscriptionPackage = http.request.env['subscription.package']

        domain = [('partner_id', '=', http.request.env.user.partner_id.id)]

        subscription_count = SubscriptionPackage.search_count(domain)
        pager = portal_pager(
            url="/my/subscription_packages",
            url_args={},
            total=subscription_count,
            page=page,
            step=self._items_per_page
        )

        subscriptions = SubscriptionPackage.search(domain,
                                                   limit=self._items_per_page,
                                                   offset=pager['offset'])
        values.update({
            'subscriptions': subscriptions,
            'pager': pager,
            'page_name': 'subscription',
        })
        return http.request.render('subscription_package.portal_my_subscriptions',
                                   values)
