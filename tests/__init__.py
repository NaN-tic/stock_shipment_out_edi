# This file is part stock_shipment_out_edi module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
try:
    from trytond.modules.party.tests.test_stock_shipment_out_edi import suite
except ImportError:
    from .test_stock_shipment_out_edi import suite

__all__ = ['suite']
