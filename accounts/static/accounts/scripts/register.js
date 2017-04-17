function validate(obj) {
    var object_type = obj.attr('type');
    var text_input = obj.val();
    if (object_type == 'password' && obj.attr('name') == 'password2') {
        if (text_input != $('#password1').val() || text_input.length < 8 || text_input.includes(' ')) {
            return false;
        } else {
            return true;
        }
    }
    if (object_type == 'text' || object_type == 'password') {
        $('#password2').trigger('change');
        if (text_input.length < 8 || text_input.includes(' ')) {
            return false;
        } else {
            return true;
        }
    } else if (object_type == 'email') {
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(text_input);
    }
}


$(document).ready(function () {
    var $ok_span = $('<span class="glyphicon glyphicon-ok form-control-feedback removable" aria-hidden="true"></span>')
    var $remove_span = $('<span class="glyphicon glyphicon-remove form-control-feedback removable" aria-hidden="true"></span>')

    var error_class = "has-error has-feedback";
    var ok_class = "has-success has-feedback";

    $('form').on('change', 'input', function () {
        var obj = $(this);
        var parent = obj.closest('.form-group');
        var hidden = obj.parents('.form-group').find('p');
        if (validate(obj)) {
            if (parent.hasClass(error_class)) {
                parent.removeClass(error_class);
                parent.children().remove('span.removable');
            }
            if (!parent.hasClass(ok_class)) {
                parent.addClass(ok_class);
                parent.append($ok_span.clone());
            }
            if (!hidden.hasClass('hidden')) {
                hidden.addClass('hidden');
            }
        } else {
            if (parent.hasClass(ok_class)) {
                parent.removeClass(ok_class);
                parent.children().remove('span.removable');
            }
            if (!parent.hasClass(error_class)) {
                parent.addClass(error_class);
                parent.append($remove_span.clone());
            }
            if (hidden.hasClass('hidden')) {
                hidden.removeClass('hidden');
            }
        }
    })
});
