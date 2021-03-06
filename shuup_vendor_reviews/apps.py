# -*- coding: utf-8 -*-
# This file is part of Shuup Product Reviews Addon.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = "shuup_vendor_reviews"
    label = "shuup_vendor_reviews"
    verbose_name = "Shuup Vendor Reviews"
    provides = {
        "admin_module": [
            "shuup_vendor_reviews.admin_module.SupplierReviewsModule"
        ],
        "xtheme_plugin": [
            "shuup_vendor_reviews.plugins.VendorReviewStarRatingsPlugin",
            "shuup_vendor_reviews.plugins.VendorReviewCommentsPlugin"
        ],
        "customer_dashboard_items": [
            "shuup_vendor_reviews.dashboard_items:VendorReviewDashboardItem"
        ],
        "front_urls": [
            "shuup_vendor_reviews.urls:urlpatterns"
        ]
    }
