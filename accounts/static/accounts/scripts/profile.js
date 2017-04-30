var post_num = 5;

$(document).ready(function() {
    $('textarea').addClass('text-input');
    
    $message_container = $('#message-output');
        
    $message_container.on('click', '.reply-link', function() {
        $post_reply_box = $(this).parents('.row-message').find('.reply-box');
        $post_reply_box.toggleClass('hidden');
        $post_reply_box.find('textarea').trigger('focus');
    });
    
    $message_container.on('submit', '.reply-form', function() {
        $form = $(this);
        $replies_container = $form.parents('.row-message').find('.reply-output');
        $.ajax({
            type : $form.attr('method'),
            url : $form.attr('action'),
            data : $form.serialize(),
            success : function(data) {
                $form.find('textarea').val('');
                
                $replies_container.fadeOut('slow', function() {
                    $replies_container.html(data);
                    $replies_container.fadeIn('slow');
                });
            },
            error : function() {
                alert('Something Went Wrong!!!');
            }
        });
        return false;
    });
    
    $message_container.on('submit', '.reply-delete-form', function() {
        $reply_delete_form = $(this);
        $output_container = $reply_delete_form.parents('.reply-output');
        
        $.ajax({
            type: $reply_delete_form.attr('method'),
            url: $reply_delete_form.attr('action'),
            data: $reply_delete_form.serialize(),
            success: function(data) {
                $output_container.fadeOut('slow', function() {
                    $output_container.html(data);
                    $output_container.fadeIn('slow');
                });
            },
            error: function() {
                alert('Something Went Wrong');
            }
        });
        return false;
    });
    
    $('#profile-post').on('submit', function() {
        $post_form = $(this);
        
        $.ajax({
            type: $post_form.attr('method'),
            url: $post_form.attr('action'),
            data: $post_form.serialize(),
            success: function(data) {
                $message_container.fadeOut('slow', function() {
                    $message_container.prepend(data);
                    $message_container.fadeIn('slow');
                    $message_container.find('textarea').addClass('text-input');
                    $post_form.find('textarea').val('');
                    post_num += 1;
                });
            },
            error: function() {
                alert('Something Went Wrong!!!');
            }
        });
        return false;
    });
    
    $more_post_form = $('#more-post-form');
    $more_post_form_val = $('#post_num');
    $more_post_form.on('submit', function() {
        $more_post_form_val.val(post_num);
        
        $.ajax({
            type: $more_post_form.attr('method'),
            url: $more_post_form.attr('action'),
            data: $more_post_form.serialize(),
            success: function(data) {
                post_num += 5;
                $message_container.append(data);
                $message_container.find('textarea').addClass('text-input');
            },
            
            error: function() {
                $('#no-more-posts').removeClass('hidden');
                $(window).off('scroll');
            }
        })
        return false;
    });
    
    $(window).on('scroll', function() {
        if( $(window).scrollTop() + $(window).height() == $(document).height() ) {
            $more_post_form.trigger('submit');
        }
    });
    
});