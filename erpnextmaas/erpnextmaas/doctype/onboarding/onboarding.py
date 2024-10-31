# Copyright (c) 2024, malikhamzaali48@gmail.com and contributors
# For license information, please see license.txt


import frappe
from frappe.desk.notifications import notify_mentions
from frappe.utils import today, now
from frappe import _
from frappe.model.document import Document


class Onboarding(Document):
	def validate(self):
		self.add_onboarding_reference()

	def add_onboarding_reference(self):
		if self.sales_invoice:
			if not frappe.db.exists(
				"Sales Invoice", {"onboarding": self.name, "name": self.sales_invoice}
			):
				si = frappe.get_doc("Sales Invoice", self.sales_invoice)
				si.db_set("onboarding", self.name)
			if frappe.db.exists(
				"Sales Invoice",
				{"onboarding": self.name, "name": ["!=", self.sales_invoice]},
			):
				invoices = frappe.get_all(
					"Sales Invoice",
					{"onboarding": self.name, "name": ["!=", self.sales_invoice]},
				)
				for d in invoices:
					si = frappe.get_doc("Sales Invoice", d.name)
					si.db_set("onboarding", "")
		else:
			si_list = frappe.get_all("Sales Invoice", {"onboarding": self.name})
			for d in si_list:
				si = frappe.get_doc("Sales Invoice", d.name)
				si.db_set("onboarding", "")

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
