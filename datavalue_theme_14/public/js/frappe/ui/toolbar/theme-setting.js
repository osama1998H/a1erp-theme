// open-theme-setting

$(document).on('click', '.theme-setting-colors-select.theme-setting-modal button', function (event) {
    event.preventDefault();
    $('.theme-setting-colors-select.theme-setting-modal button').removeClass('active');
    $(this).addClass('active');
});
$(document).on('click', '.open-theme-setting', function (event) {
    event.preventDefault();
    let colors_list = ['Blue', 'Green', 'Red', 'Orange', 'Yellow', 'Pink', 'Violet']
    let d = new frappe.ui.Dialog({
        title: __('Theme Settings'),
        fields: [
            {
                label: 'Dark Style',
                fieldname: 'dark_style',
                fieldtype: 'Check',
                default: ($('html').attr('data-theme') == 'dark' && $('body').hasClass('dv-dark-style')) ? 1 : 0
            },
            {
                label: 'Colors',
                fieldname: 'colors_icons',
                fieldtype: 'HTML',
                options: `
                    <div class="theme-setting-colors-select theme-setting-modal">   
                        <h4>${__('Theme Colors')}</h4>
                        <div class="dv-row dv-row-sm"> 
                            ${colors_list.map(color => `<div class="dv-col"><button type="button" class="${($('body').data('theme-color') == color) ? 'active' : ''}" data-color="${color}" data-class="dv-${color}-style">${color}</button></div>`).join("")}
                        </div>
                    </div>
                `
            }
        ],
        primary_action_label: __('Save Settings'),
        primary_action(values) {
            let active_btn = $('.theme-setting-colors-select.theme-setting-modal button.active');
            let data = {
                color_name: active_btn.data('color'),
                color_class: active_btn.data('class'),
                dark_style: values.dark_style
            }
            frappe.db.set_value('Theme Settings', 'Theme Settings', {
                'dark_view': data.dark_style,
                'theme_color': data.color_name
            }, function () {
                frappe.ui.toolbar.clear_cache();
                setTimeout(() => d.hide(), 1000);
            });
        }
    });
    d.show();
});
