from . import __version__ as app_version

app_name = "datavalue_theme_14"
app_title = "Datavalue Theme 14"
app_publisher = "Abdo Hamoud"
app_description = "Data Value Frappe 14 Theme"
app_email = "abdo.host@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------


website_context = {
    "favicon": "/assets/datavalue_theme_14/images/logo-icon.png",
    "splash_image": "/assets/datavalue_theme_14/images/theme_splash_empty.jpg"
}

app_include_css = [
    "/assets/datavalue_theme_14/plugins/animate.css/animate.min.css",
    "/assets/datavalue_theme_14/plugins/fontawesome/all.min.css",
    "/assets/datavalue_theme_14/plugins/tooltip/tooltip-theme-twipsy.css",
    "/assets/datavalue_theme_14/plugins/flat-icons/flaticon.css",
    "datavalue_theme.bundle.css"
]

app_include_js = [
    "/assets/datavalue_theme_14/plugins/bootstrap4c-chosen/chosen.min.js",
    "/assets/datavalue_theme_14/plugins/nicescroll/nicescroll.js",
    "/assets/datavalue_theme_14/plugins/tooltip/tooltip.js",
    "/assets/datavalue_theme_14/plugins/jquery-fullscreen/jquery.fullscreen.min.js?ver=1",
    "datavalue_theme.bundle.js"
]

email_brand_image = "assets/datavalue_theme_14/images/logo-icon.png"

# include js, css files in header of web template
web_include_css = [
    "assets/datavalue_theme_14/plugins/fontawesome/all.min.css",
    "assets/datavalue_theme_14/css/login.css",
    "assets/datavalue_theme_14/css/dv-login.css?ver=1"
]
web_include_js = [
    "/assets/datavalue_theme_14/js/vue/theme-settings.js?ver=1"
]

# include js, css files in header of desk.html
# app_include_css = "/assets/datavalue_theme_14/css/datavalue_theme_14.css"
# app_include_js = "/assets/datavalue_theme_14/js/datavalue_theme_14.js"

# include js, css files in header of web template
# web_include_css = "/assets/datavalue_theme_14/css/datavalue_theme_14.css"
# web_include_js = "/assets/datavalue_theme_14/js/datavalue_theme_14.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "datavalue_theme_14/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "datavalue_theme_14.utils.jinja_methods",
#	"filters": "datavalue_theme_14.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "datavalue_theme_14.install.before_install"
# after_install = "datavalue_theme_14.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "datavalue_theme_14.uninstall.before_uninstall"
# after_uninstall = "datavalue_theme_14.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "datavalue_theme_14.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"datavalue_theme_14.tasks.all"
#	],
#	"daily": [
#		"datavalue_theme_14.tasks.daily"
#	],
#	"hourly": [
#		"datavalue_theme_14.tasks.hourly"
#	],
#	"weekly": [
#		"datavalue_theme_14.tasks.weekly"
#	],
#	"monthly": [
#		"datavalue_theme_14.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "datavalue_theme_14.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "datavalue_theme_14.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "datavalue_theme_14.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"datavalue_theme_14.auth.validate"
# ]
