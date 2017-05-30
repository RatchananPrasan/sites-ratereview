$(document).ready(function() {

    var genre_count = 1;
                  
    $('#genre-wrapper').on('click', 'span', function() {
        $('#genre-wrapper').append('<div class="form-group"><select name="genre-'+genre_count+'-genre" class="form-control" id="id_genre-'+genre_count+'-genre"><option value="" selected="">---------</option><option value="action">Action</option><option value="adventure">Adventure</option><option value="animation">Animation</option><option value="biography">Biography</option><option value="comedy">Comedy</option><option value="crime">Crime</option><option value="documentary">Documentary</option><option value="drama">Drama</option><option value="family">Family</option><option value="fantasy">Fantasy</option><option value="film-noir">Film-Noir</option><option value="history">History</option><option value="horror">Horror</option><option value="music">Music</option><option value="musical">Musical</option><option value="mystery">Mystery</option><option value="romance">Romance</option><option value="sci-fi">Sci-Fi</option><option value="sport">Sport</option><option value="thriller">Thriller</option><option value="war">War</option><option value="western">Western</option></select></div>');
        genre_count += 1;
    });

    var actor_count = 1;
    
    $('#actor-wrapper').on('click', 'span', function() {
        $('#actor-wrapper').append('<div class="form-group"><input type="text" name="actor-'+actor_count+'-actor_name" class="form-control" placeholder="Actor/Actress..." maxlength="50" id="id_actor-'+actor_count+'-actor_name"></div>');
        actor_count += 1;    
    });
    
    $('#create-form').on('submit', function() {
        $('#id_genre-TOTAL_FORMS').val($('#genre-wrapper select').length);    
        $('#id_actor-TOTAL_FORMS').val($('#actor-wrapper input[type="text"]').length);
    });
});