

$(document).ready(function() {

   $("#search-btn").on("click", function(e){
    e.preventDefault();
    var searchText = $('#search-box').val();
    $.ajax({
        url: '/real_estate?search_filter=' + searchText,
        type: 'GET',
        success: function (resp) {
            var newHtml = resp.data.map(d => {
                return `<div class="well real_estate">
                            <a href="real_estate/$(d.id)">
                                <img src="${d.main_image}"> 
                                <h4>${d.street}, ${d.zip_code_id}, ${d.city} </h4>
                                <p>Bedrooms: ${d.bedrooms}, Bathrooms: ${d.bathromms}, Size: ${d.size} square meters</p>
                                <p>Type: ${d.type}</p>
                                <p>${d.price} kr.</p>
                            </a>
            
                         </div>`
            });
            $('.main').html(newHtml.join(''));
            $('#search-box').val('');
        },
        error: function(xhr, status, error){
            console.error(error);
        }
    })
           console.log('Hér er ég. halló!!')

   });
});