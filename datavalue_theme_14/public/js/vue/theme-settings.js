(function ($) {

    'use strict';

    if ($('#page-login').length) {
        $('#page-login').each(function () {
            let page = $(this);
            frappe.call({
                type: 'POST',
                method: 'datavalue_theme_14.api.get_theme_settings',
                args: {},
                callback: function (response) {
                    let settings = response.message;
                    if (settings.full_page_background == '1') {
                        $('.page_content', page).removeClass('min-background').addClass('full-background');
                    } else {
                        $('.page_content', page).removeClass('full-background').addClass('min-background');
                    }
                    if (settings.transparent_background == '1' && settings.enable_background == '1') {
                        $('.page_content', page).addClass('widget-background-transparent');
                    } else {
                        $('.page_content', page).removeClass('widget-background-transparent');
                    }
                    if (settings.background_type == 'Single Photo' && settings.enable_background == '1') {
                        $('.page_content', page).css({
                            'background-image': 'url("' + settings.background_photo + '")'
                        });
                    } else if (settings.background_type == 'Slideshow' && settings.enable_background == '1') {
                        let photos = '';
                        if (settings.slideshow_photos && settings.slideshow_photos.length) {
                            settings.slideshow_photos.map((item) => {
                                photos += `<div class="login-page-slideshow-item"><img src="${item.photo}"></div>`;
                            });
                        }
                        $('.page_content', page).append(`
                            <div class="login-page-slideshow-container">
                                 <div class="owl-carousel">${photos}</div>
                            </div>                        
                        `);
                        $('head').append(`
                            <link rel="stylesheet" class="login-slideshow-css" href="/assets/datavalue_theme_14/plugins/owl-carousel/owl.carousel.css">
                            <link rel="stylesheet" class="login-slideshow-css" href="/assets/datavalue_theme_14/plugins/owl-carousel/owl.theme.css">
                            <link rel="stylesheet" class="login-slideshow-css" href="/assets/datavalue_theme_14/plugins/owl-carousel/owl.transitions.css">
                        `);
                        $('body').append(`
                            <script class="login-slideshow-js" src="/assets/datavalue_theme_14/plugins/owl-carousel/owl.carousel.min.js"></script>
                        `);
                        setTimeout(function () {
                            $('.page_content .login-page-slideshow-container .owl-carousel', page).owlCarousel({
                                autoPlay: 5000,
                                stopOnHover: true,
                                lazyEffect: 'fade',
                                transitionStyle: 'fade',
                                navigation: false, // Show next and prev buttons
                                slideSpeed: 1000,
                                paginationSpeed: 1000,
                                singleItem: true,
                                pagination: false,
                                responsive: true
                            });
                        }, 250);
                    }
                }
            });
        });
    }

})(jQuery);
