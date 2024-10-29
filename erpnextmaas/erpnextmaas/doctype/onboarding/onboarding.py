# Copyright (c) 2024, malikhamzaali48@gmail.com and contributors
# For license information, please see license.txt


import frappe
import json
from frappe.model.document import Document
from frappe import _
from frappe.contacts.address_and_contact import load_address_and_contact
from frappe.email.inbox import link_communication_to_document
from frappe.model.mapper import get_mapped_doc
from frappe.query_builder import DocType, Interval
from frappe.query_builder.functions import Now
from frappe.utils import flt, get_fullname, today

from erpnext.crm.utils import (
	CRMNote,
	copy_comments,
	link_communications,
	link_open_events,
	link_open_tasks,
)

from erpnext.setup.utils import get_exchange_rate
from erpnext.utilities.transaction_base import TransactionBase


class Onboarding(Document):
	pass


def update_status_date_pass():
	onboarding_list = frappe.db.get_all(
		"Onboarding", {"end_date": [">=", today()], "status": ["!=", "Delayed"]}
	)
	for d in onboarding_list:
		doc = frappe.get_doc("Onboarding", d.name)
		doc.db_set("status", "Delayed")
