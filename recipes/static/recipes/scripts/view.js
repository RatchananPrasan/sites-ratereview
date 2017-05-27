$(document).ready(function() {
    var $rate_icon_group = $('#rate-icon-group');
    var $rate_icon_group_span = $('#rate-icon-group span');
    
    $rate_icon_group.on('click', 'span', function() {
        var current_star = parseInt($(this).find('input').val());
        for(var i=0;i < current_star; i++) {
            $rate_icon_group_span.eq(i).addClass('warning-color');
        }
        for(var i=current_star;i < 5; i++) {
            $rate_icon_group_span.eq(i).removeClass('warning-color');
        }
        $('#id_rate').val(current_star);
    });
    
    $('#form-rate').on('submit', function() {
        if ($('#id_rate').val() == "") {
            alert('Please select rating by clicking on the star icon.');
            return false;
        }
    });
});