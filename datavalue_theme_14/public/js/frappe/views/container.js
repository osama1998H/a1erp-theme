// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// MIT License. See license.txt

// page container
frappe.provide("frappe.pages");
frappe.provide("frappe.views");

window.cur_page = null;
frappe.modules_list = [];
frappe.module_items_list = [];
frappe.active_module = {};
frappe.theme_settings = {};
frappe.is_app_loaded = false;
frappe.is_page_changed = false;

frappe.views.Container = class Container {
    // Container contains pages inside `#container` and manages page creation, switching
    constructor() {
        this.container = $("#body").get(0);
        this.page = null; // current page
        this.pagewidth = $(this.container).width();
        this.pagemargin = 50;
        localStorage.container_fullwidth = true;
        $('body').addClass('full-width');

        var me = this;

        $(document).trigger('app-loaded');
        frappe.is_app_loaded = true;
        document.documentElement.setAttribute("data-theme", document.documentElement.getAttribute('data-dv-theme'));
        if ($('body').data('close-sub-menu') == '1') {
            $('.btn-toggle-main-menu').removeClass('menu-shown');
            $('body').addClass('hide-main-menu');
        }

        $(document).on("page-change", function () {
            // set data-route in body
            var route_str = frappe.get_route_str();
            var route_obj = frappe.get_route();
            let current_page = $('.content.page-container:visible', this);
            $("body").attr("data-route", route_str);
            $("body").attr("data-sidebar", me.has_sidebar() ? 1 : 0);
            setTimeout(() => $('input#navbar-search').trigger('blur'), 250);
            $('.dv-nav-search ul[role="listbox"]').prop('hidden', true);
            $(document).trigger('show-side-menu');
        });

        $(document).bind("rename", function (event, dt, old_name, new_name) {
            frappe.breadcrumbs.rename(dt, old_name, new_name);
        });
    }

    add_page(label) {
        var page = $('<div class="content page-container"></div>')
            .attr("id", "page-" + label)
            .attr("data-page-route", label)
            .hide()
            .appendTo(this.container)
            .get(0);
        page.label = label;
        frappe.pages[label] = page;

        return page;
    }

    change_to(label) {
        cur_page = this;
        if (label.tagName) {
            // if sent the div, get the table
            var page = label;
        } else {
            var page = frappe.pages[label];
        }
        if (!page) {
            console.log(__("Page not found") + ": " + label);
            return;
        }

        // hide dialog
        if (window.cur_dialog && cur_dialog.display && !cur_dialog.keep_open) {
            if (!cur_dialog.minimizable) {
                cur_dialog.hide();
            } else if (!cur_dialog.is_minimized) {
                cur_dialog.toggle_minimize();
            }
        }

        // hide current
        if (this.page && this.page != page) {
            $(this.page).hide();
            $(this.page).trigger("hide");
        }

        // show new
        if (!this.page || this.page != page) {
            this.page = page;
            // $(this.page).fadeIn(300);
            $(this.page).show();
        }

        $(document).trigger("page-change");

        this.page._route = frappe.router.get_sub_path();
        $(this.page).trigger("show");
        !this.page.disable_scroll_to_top && frappe.utils.scroll_to(0);
        frappe.breadcrumbs.update();

        return this.page;
    }

    has_sidebar() {
        var flag = 0;
        var route_str = frappe.get_route_str();
        // check in frappe.ui.pages
        flag = frappe.ui.pages[route_str] && !frappe.ui.pages[route_str].single_column;

        // sometimes frappe.ui.pages is updated later,
        // so check the dom directly
        if (!flag) {
            var page_route = route_str.split("/").slice(0, 2).join("/");
            flag = $(`.page-container[data-page-route="${page_route}"] .layout-side-section`)
                .length
                ? 1
                : 0;
        }

        return flag;
    }
};
