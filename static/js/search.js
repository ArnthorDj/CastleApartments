

$(document).ready(function() {

   $("#search-btn").on("click", function(e){
    e.preventDefault();
    var searchText = $('#search-box').val();
    $.ajax({
        url: '/real_estate?search_filter=' + searchText,
        type: 'GET',
        success: function (resp) {
            var newHtml = resp.data.map(d => {
                return `<div class="well real estate">
                            <a href="/real_estate/info/$(d.id)">
                                <img src="${d.main_image}" height="200" width="300"> 
                                <h4 style="color: black">${d.street}, ${d.zip_code_id}, ${d.city}</h4>
                                <p style="color: black">Bedrooms: ${d.bedrooms}, Bathrooms: ${d.bathromms}, Size: ${d.size} square meters</p>
                                <p style="color: black">Type: ${d.type}</p>
                                <p style="color: black">${d.price} kr.</p>
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

   });
});