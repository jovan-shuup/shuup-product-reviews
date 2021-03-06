# -*- coding: utf-8 -*-
# This file is part of Shuup Product Reviews Addon.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from shuup.admin.shop_provider import get_shop
from shuup.admin.utils.picotable import Column, TextFilter
from shuup_product_reviews.admin_module.views import BaseProductReviewListView
from shuup_vendor_reviews.models import VendorReview


class VendorReviewListView(BaseProductReviewListView):
    model = VendorReview
    url_identifier = "vendor_reviews"

    default_columns = [
        Column(
            "supplier",
            _("Vendor"),
            filter_config=TextFilter(
                filter_field="supplier__name",
                placeholder=_("Filter by vendor...")
            )
        )
    ] + BaseProductReviewListView.default_columns

    mass_actions = [
        "shuup_vendor_reviews.admin_module.mass_actions.ApproveVendorReviewMassAction",
        "shuup_vendor_reviews.admin_module.mass_actions.RejectVendorReviewMassAction"
    ]

    def get_queryset(self):
        return VendorReview.objects.filter(shop=get_shop(self.request))
