// Copyright (c) 2024, malikhamzaali48@gmail.com and contributors
// For license information, please see license.txt
frappe.provide("erpnext");
frappe.provide("erpnext.crm");

// TODO commonify this code
erpnext.crm.Onboarding = class Onboarding extends frappe.ui.form.Controller {

	refresh() {
		this.show_notes();
		this.show_activities();
	}

	show_notes() {
		const crm_notes = new erpnext.utils.CRMNotes({
			frm: this.frm,
			notes_wrapper: $(this.frm.fields_dict.notes_html.wrapper),
		});
		crm_notes.refresh();
	}

	show_activities() {
		const crm_activities = new erpnext.utils.CRMActivities({
			frm: this.frm,
			open_activities_wrapper: $(this.frm.fields_dict.open_activities_html.wrapper),
			all_activities_wrapper: $(this.frm.fields_dict.all_activities_html.wrapper),
			form_wrapper: $(this.frm.wrapper),
		});
		crm_activities.refresh();
	}
};

extend_cscript(cur_frm.cscript, new erpnext.crm.Onboarding({ frm: cur_frm }));
