# Infinite Laundry CRM Customization

These instructions are meant to customize the Infinite Laundry CRM.

---


cyb_web_customization

### For customizing login page:
Views/views.xml
template : custom_web_login_layout

You can change the button color

---

### For customizing offline page:
Views/views.xml
template : webclient_offline_custom

---

### For hidding preferences in Preference Modal
Views/views.xml
template : gff_view_form_simple_modif_custom_inherit

---

### There you can change the button color
Views/views.xml
web_login_custom

---

`static/src/scss/custom.scss` is where you can change theme color, that will be applied globaly

---

“Apps” and “Settings”
Those are related to access rights, those will be handled through access rights.

Note for data: We wouldn't load demo data while creating production db or if you want to load and remove after then you have to give me your odoo access or we can do in meeting.