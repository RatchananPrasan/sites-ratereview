$(document).ready(function () {

    var $upload_cover_image;

    function update_cover_image(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#cover-image-display').removeClass('hidden');
                $upload_cover_image.croppie('bind', {
                    url: e.target.result
                });
            }
            reader.readAsDataURL(input.files[0]);
        } else {
            $('#cover-image-display').addClass('hidden');
        }
    }

    $upload_cover_image = $('#cover-image-display').croppie({
        boundary: {
            width: 300,
            height: 300
        },
        viewport: {
            width: 200,
            height: 200
        }
    });

    $('#id_cover_image-image').on('change', function () {
        update_cover_image(this);
    });

    var image_count = $('#more-image input[type="file"]').length;
    $('#more-image-button').on('click', function () {
        $('#more-image').append('<input class="file-input" type="file" name="more_image-'+ image_count +'-image" id="id_more_image-'+ image_count +'-image">');
        image_count += 1;
    });
    
    var ingredients_count = $('#ingredients-wrapper input[type="text"]').length;
    $('#more-ingredients-button').on('click', function() {
        $('#ingredients-wrapper').append('<div class="form-group"><input type="text" name="ingredients-'+ ingredients_count +'-text" class="form-control" id="id_ingredients-'+ ingredients_count +'-text"></div>');;
        ingredients_count += 1;
    });

    var directions_count = $('#directions-wrapper input[type="text"]').length;
    $('#more-directions-button').on('click', function() {
        $('#directions-wrapper').append('<div class="form-group"><input type="text" name="directions-'+ directions_count +'-text" class="form-control" id="id_directions-'+ directions_count +'-text"></div>');
        directions_count += 1;
    });
    
    var category_count = $('#category-wrapper select').length;
    $('#more-category-button').on('click', function() {
        $('#category-wrapper').append('<div class="form-group"><select name="category-'+ category_count +'-title" class="form-control" id="id_category-'+ category_count +'-title"><option value="" selected="">---------</option><option value="Sn">Snacks</option><option value="Br">Breakfast</option><option value="De">Dessert</option><option value="Di">Dinner</option><option value="Dr">Drinks</option><option value="He">Healthy</option><option value="Lu">Lunch</option><option value="Se">Seafood</option></select></div>');
        category_count += 1;
    });

    $('#create-form').on('submit', function () {
        if ($('#id_cover_image-image').val()) {
            $upload_cover_image.croppie('result', {
                type: 'base64',
                format: 'jpeg',
                size: 'viewport'
            }).then(function (img) {
                $('#cover_image_64').val(img);
            });
        }
        
        $('#id_more_image-TOTAL_FORMS').val(image_count);
        
        $('#id_category-TOTAL_FORMS').val(category_count);
        
        $('#id_directions-TOTAL_FORMS').val(directions_count);
        
        $('#id_ingredients-TOTAL_FORMS').val(ingredients_count);
    });
});
