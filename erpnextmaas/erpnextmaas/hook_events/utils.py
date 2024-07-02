from __future__ import unicode_literals
from num2words import num2words
import frappe


@frappe.whitelist()
def get_amount_in_ar(amount):
    words = num2words(amount, to='currency', lang='ar')
    formatted_amount = f"{words} ريال سعودي فقط ({amount:,} ريال سعودي)"
    return formatted_amount
