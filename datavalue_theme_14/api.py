from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.cache_manager import clear_user_cache


@frappe.whitelist()
def get_module_name_from_doctype(doc_name, current_module=""):
    # frappe.msgprint("======"+str(doc_name))
    condition = ""
    if doc_name:
        if current_module:
            condition = "and  w.`name` = {current_module} ".format(current_module=current_module)

        list_od_dicts = frappe.db.sql("""
            select *
                    from (
                            select  w.`name` `module`,
                                 (select restrict_to_domain from `tabModule Def` where `name` = w.module ) restrict_to_domain
                                             from  tabWorkspace w
                                             inner join
                                                        `tabWorkspace Link` l
                                                        on w.`name` = l.parent
                                                         where link_to = '{doc_name}'
                                                          %s
                                )	T
        """.format(doc_name=doc_name), (condition), as_dict=True, debug=False)
        if list_od_dicts:
            return [{"module": list_od_dicts[0]["module"]}]
        else:
            list_od_dicts = frappe.db.sql("""
                select *
                        from (
                                select  w.`name` `module`,
                                     (select restrict_to_domain from `tabModule Def` where `name` = w.module ) restrict_to_domain
                                                 from  tabWorkspace w
                                                 inner join
                                                            `tabWorkspace Link` l
                                                            on w.`name` = l.parent
                                                             where link_to = '{doc_name}'
                                    )	T
            """.format(doc_name=doc_name), as_dict=True, debug=False)
        if list_od_dicts:
            return [{"module": list_od_dicts[0]["module"]}]


@frappe.whitelist()
def change_language(language):
     frappe.db.set_value("User", frappe.session.user, "language", language)
     clear()
     return True


@frappe.whitelist()
def get_current_language():
    return frappe.db.get_value("User", frappe.session.user, "language")


@frappe.whitelist()
def get_company_logo():
    logo_path = ""
    current_company = frappe.defaults.get_user_default("company")
    if current_company:
        logo_path = frappe.db.get_value("Company", current_company, "company_logo")

    return logo_path


@frappe.whitelist(allow_guest=True)
def get_theme_settings():
    slideshow_photos = []
    settings_list = {}
    settings = frappe.db.sql("""
                       SELECT * FROM tabSingles WHERE doctype = 'Theme Settings';
    """, as_dict=True, debug=False)

    for setting in settings:
        settings_list[setting['field']] = setting['value']

    if (("background_type" in settings_list) and settings_list['background_type'] == 'Slideshow'):
        slideshow_photos = frappe.db.sql("""
                               SELECT `photo` FROM `tabSlideshow Photos` WHERE `parent` = 'Theme Settings';
            """, as_dict=True, debug=False)

    return {
        'enable_background': settings_list['enable_background'] if ("enable_background" in settings_list) else '',
        'background_photo': settings_list['background_photo'] if ("background_photo" in settings_list) else '',
        'background_type': settings_list['background_type'] if ("background_type" in settings_list) else '',
        'full_page_background': settings_list['full_page_background'] if ("full_page_background" in settings_list) else '',
        'transparent_background': settings_list['transparent_background'] if ("transparent_background" in settings_list) else '',
        'slideshow_photos': slideshow_photos,
        'dark_view': settings_list['dark_view'] if ("dark_view" in settings_list) else '',
        'theme_color': settings_list['theme_color'] if ("theme_color" in settings_list) else '',
        'show_icon_label': settings_list['show_icon_label'] if ("show_icon_label" in settings_list) else '',
        'hide_icon_tooltip': settings_list['hide_icon_tooltip'] if ("hide_icon_tooltip" in settings_list) else '',
        'always_close_sub_menu': settings_list['always_close_sub_menu'] if ("always_close_sub_menu" in settings_list) else '',
        'menu_opening_type': settings_list['menu_opening_type'] if ("menu_opening_type" in settings_list) else '',
        'loading_image': settings_list['loading_image'] if ("loading_image" in settings_list) else ''
    }

def clear():
    frappe.local.session_obj.update(force=True)
    frappe.local.db.commit()
    clear_user_cache(frappe.session.user)
    frappe.response['message'] = _("Cache Cleared")
