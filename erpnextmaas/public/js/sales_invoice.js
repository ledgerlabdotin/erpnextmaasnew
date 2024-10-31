frappe.ui.form.on("Sales Invoice", {
	refresh: function (frm) {
		if (frm.doc.docstatus == 1) {
			frm.add_custom_button(
				__("Onboarding"),
				function () {
					frm.trigger("make_onboarding");
				},
				__("Create")
			);
		}
	},
	make_onboarding: function (frm) {
		frappe.model.open_mapped_doc({
			method: "erpnextmaas.erpnextmaas.hook_events.sales_invoice.make_onboarding",
			frm: frm,
		});
	},
});
