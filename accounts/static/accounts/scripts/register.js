var check_username = false;
var check_password1 = false;
var check_password2 = false;
var check_email = false;

function validate(obj) {
    var object_type = obj.attr('type');
    var text_input = obj.val();
    if (object_type == 'password' && obj.attr('name') == 'password2') {
        if (text_input != $('#password1').val() || text_input.length < 8 || text_input.includes(' ')) {
            check_password2 = false;
            return false;
        } else {
            check_password2 = true;
            return true;
        }
    }
    if (object_type == 'text' || object_type == 'password') {
        var result;
        if (text_input.length < 8 || text_input.includes(' ')) {
            result = false;
        } else {
            result = true;
        }

        if (object_type == 'password') {
            check_password1 = result;
            $('#password2').trigger('change');
        } else {
            check_username = result;
        }
        return result;
    } else if (object_type == 'email') {
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        check_email = re.test(text_input);
        return check_email;
    }
}


$(document).ready(function () {

    $('#register-container').fadeIn('slow');

    var $ok_span = $('<span class="glyphicon glyphicon-ok form-control-feedback removable" aria-hidden="true"></span>')
    var $remove_span = $('<span class="glyphicon glyphicon-remove form-control-feedback removable" aria-hidden="true"></span>')

    var error_class = 'has-error has-feedback';
    var ok_class = 'has-success has-feedback';

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
    });

    var $form_group = $('.form-group');
    $('button[type="submit"]').on('click', function () {
        if (check_username && check_password1 && check_password2 && check_email) {
            return true;
        }
        
        if (!check_username) {
            $form_group.eq(0).effect('shake', 'slow');
        }
        if (!check_password1) {
            $form_group.eq(1).effect('shake', 'slow');
        }
        if (!check_password2) {
            $form_group.eq(2).effect('shake', 'slow');
        }
        if (!check_email) {
            $form_group.eq(3).effect('shake', 'slow');
        }
        return false;
    })
});
