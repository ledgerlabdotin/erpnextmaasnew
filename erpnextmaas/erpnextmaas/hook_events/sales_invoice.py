import frappe
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def make_onboarding(source_name, target_doc=None, ignore_permissions=False):
    if frappe.db.exists("Onboarding", {"sales_invoice": source_name}):
        return frappe.throw("Onboarding Already Exists Against this Invoice")

    doclist = get_mapped_doc(
        "Sales Invoice",
        source_name,
        {
            "Sales Invoice": {
                "doctype": "Onboarding",
                "field_map": {
                    "customer": "customer_name",
                    "name": "sales_invoice",
                    "language": "preferred_language",
                },
            },
        },
        target_doc,
        ignore_permissions=ignore_permissions,
    )

    return doclist
