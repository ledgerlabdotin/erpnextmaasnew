# Copyright (c) 2024, malikhamzaali48@gmail.com and contributors
# For license information, please see license.txt


import frappe
from frappe.desk.notifications import notify_mentions
from frappe.utils import today, now
from frappe import _
from frappe.model.document import Document


class Onboarding(Document):
	@frappe.whitelist()
	def add_note(self, note):
		self.append(
			"notes", {"note": note, "added_by": frappe.session.user, "added_on": now()}
		)
		self.save()
		notify_mentions(self.doctype, self.name, note)


def update_status_date_pass():
	onboarding_list = frappe.db.get_all(
		"Onboarding", {"end_date": [">=", today()], "status": ["!=", "Delayed"]}
	)
	for d in onboarding_list:
		doc = frappe.get_doc("Onboarding", d.name)
		doc.db_set("status", "Delayed")
