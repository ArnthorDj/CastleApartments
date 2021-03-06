// JavaScript file so that the Search Bar works, we get the data from view.py and display the results with this function.

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
                        <a href="/real_estate/info/${d.id}">
                            <img src="${d.main_image}" height="250" width="350"> 
                            <h4 class="black-font">${d.street}, ${d.zip_code_id} ${d.city}</h4>
                            <h4 class="black-font"><b>Country:</b> ${d.country}</h4>
                            <p class="black-font">Bedrooms: ${d.bedrooms}, Bathrooms: ${d.bathrooms}, 
                            Size: ${d.size} square meters</p>
                            <p class="black-font">Type: ${d.type}</p>
                            <p class="black-font">${d.price} kr.</p>
                        </a>
                    </div>`
                });
                $('#main').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error){
                console.error(error);
            }
        })

    });
});