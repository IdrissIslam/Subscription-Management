# Copyright (C) 2020 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Subscription Package Portal",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "category": "Generic Modules/Human Resources",
    "summary": "Show current Subscription Package Portal in a website.",
    "author": "Idris Eslam Idris",
    "website": "mzn.sa",
    "depends": ["subscription_package", "web",'sale_management'],
    "data": [
        "views/customer_template.xml",
    ],
    "installable": True,
}
