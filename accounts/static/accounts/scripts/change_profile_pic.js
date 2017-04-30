$(document).ready(function() {
    var $uploadCrop;
    
    function updateFile(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function(e) {
                $('#image-wrap').removeClass('hidden');
                $uploadCrop.croppie('bind', {
                    url: e.target.result
                })
            }

            reader.readAsDataURL(input.files[0]);
        }
    }
    
    $uploadCrop = $('#image-wrap').croppie({
        boundary: {
            width: 300,
            height: 300,
        },
        viewport: {
            width: 128,
            height: 128,
            type: 'circle'
        }
    });
    
    $('#id_image').on('change', function() {
        updateFile(this);
    });
    
    $('#image-form').on('submit', function() {
        $uploadCrop.croppie('result', {
            type: 'base64',
            format: 'jpeg',
            size: 'viewport',
            circle: false
        }).then(function(img) {
           $('#image64').val(img);
        });
    });
});