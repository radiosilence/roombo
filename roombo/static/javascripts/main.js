requirejs.config({
    shim: {
        'jquery.cookie': ['jquery'],
        'chosen.jquery': ['jquery'],
        'jquery.scrollTo': ['jquery']
    }
});
require([
    'jquery',
    'jquery.cookie',
    undefined
], function(
    $,
    undefined
) {

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            }
        }
    });

});