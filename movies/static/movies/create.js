$(document).ready(function()){

    var genre_count = $('#genre-wrapper select').length;

    $('#more-genre-button').on('click', function() {
        $('#genre-wrapper').append('                        <div class="detail"><div class="inp"><select name="category-'+ category_count +'-title" class="form-control" id="id_category-'+ genre_count +'-title"><option value="" selected="">---------</option><option value="Sn">Snacks</option><option value="Br">Breakfast</option><option value="De">Dessert</option><option value="Di">Dinner</option><option value="Dr">Drinks</option><option value="He">Healthy</option><option value="Lu">Lunch</option><option value="Se">Seafood</option></select></div></div>');
        genre_count += 1;
    });




    $('#create-form').on('submit', function () {
             $('#id_genre-TOTAL_FORMS').val(genre_count);
    }

});