# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "e_comm"
app_title = "E Comm"
app_publisher = "Pratik"
app_description = "My New E commerce web site"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "pratik.m@indictrans"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/e_comm/css/e_comm.css"
# app_include_js = "/assets/e_comm/js/e_comm.js"

# include js, css files in header of web template
# web_include_css = "/assets/e_comm/css/e_comm.css"
# web_include_js = "/assets/e_comm/js/e_comm.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

doctype_js = {
	"Customer" : ["customize/customer/customer.js",]
}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "e_comm.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "e_comm.install.before_install"
# after_install = "e_comm.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "e_comm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"e_comm.tasks.all"
# 	],
# 	"daily": [
# 		"e_comm.tasks.daily"
# 	],
# 	"hourly": [
# 		"e_comm.tasks.hourly"
# 	],
# 	"weekly": [
# 		"e_comm.tasks.weekly"
# 	]
# 	"monthly": [
# 		"e_comm.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "e_comm.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "e_comm.event.get_events"
# }

doc_events = {
	"Customer": {
		"validate": ["e_comm.customize.customer.customer.validate",]

	}
}

fixtures = ["Custom Field"]
