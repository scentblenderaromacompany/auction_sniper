$(document).ready(function() {
    $('#search-form').on('submit', function(e) {
        e.preventDefault();
        let keywords = $('#keywords').val();
        $.post('/search', { keywords: keywords }, function(data) {
            $('#auction-table tbody').empty();
            data.forEach(function(auction) {
                $('#auction-table tbody').append(`
                    <tr data-auction='${JSON.stringify(auction)}'>
                        <td><img src="${auction.image}" alt="Auction Image"></td>
                        <td>${auction.title}</td>
                        <td>${auction.price}</td>
                        <td>${auction.time_left}</td>
                        <td>${auction.location}</td>
                        <td>${auction.shipping_cost}</td>
                        <td>${auction.ebay_price}</td>
                        <td><button class="track-btn">Track</button></td>
                    </tr>
                `);
            });
        });
    });

    $('#auction-table').on('click', '.track-btn', function() {
        let auction = $(this).closest('tr').data('auction');
        $.ajax({
            url: '/track',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(auction),
            success: function(response) {
                alert('Auction tracked successfully!');
            }
        });
    });

    $('#tracked-auctions-btn').on('click', function() {
        $.get('/tracked', function(data) {
            $('#tracked-auctions tbody').empty();
            data.forEach(function(auction) {
                $('#tracked-auctions tbody').append(`
                    <tr data-auction='${JSON.stringify(auction)}'>
                        <td><img src="${auction.image}" alt="Auction Image"></td>
                        <td>${auction.title}</td>
                        <td>${auction.price}</td>
                        <td>${auction.time_left}</td>
                        <td>${auction.location}</td>
                        <td>${auction.shipping_cost}</td>
                        <td>${auction.ebay_price}</td>
                    </tr>
                `);
            });
        });
    });

    $('#auction-table').on('click', 'tr', function() {
        let auction = $(this).data('auction');
        $('#auction-image').attr('src', auction.image);
        $('#auction-details').html(`
            <h2>${auction.title}</h2>
            <p>Price: ${auction.price}</p>
            <p>Time Left: ${auction.time_left}</p>
            <p>Location: ${auction.location}</p>
            <p>Shipping Cost: ${auction.shipping_cost}</p>
            <p>eBay Price: ${auction.ebay_price}</p>
        `);
        $('#auction-modal').show();
    });

    $('.close').on('click', function() {
        $('#auction-modal').hide();
    });
});
