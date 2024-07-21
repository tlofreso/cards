document.addEventListener('DOMContentLoaded', function() {
    var addressInput = document.getElementById('id_street');
    var cityInput = document.getElementById('id_city');
    var stateInput = document.getElementById('id_state');
    var zipcodeInput = document.getElementById('id_zipcode');
    var countryInput = document.getElementById('id_country');

    if (addressInput) {
        var autocomplete = new google.maps.places.Autocomplete(addressInput, {
            types: ['address']
        });

        autocomplete.addListener('place_changed', function() {
            var place = autocomplete.getPlace();
            for (var i = 0; i < place.address_components.length; i++) {
                var addressType = place.address_components[i].types[0];
                if (addressType === 'street_number' || addressType === 'route') {
                    addressInput.value = place.name;
                } else if (addressType === 'locality') {
                    cityInput.value = place.address_components[i].long_name;
                } else if (addressType === 'administrative_area_level_1') {
                    stateInput.value = place.address_components[i].short_name;
                } else if (addressType === 'postal_code') {
                    zipcodeInput.value = place.address_components[i].long_name;
                } else if (addressType === 'country') {
                    countryInput.value = place.address_components[i].long_name;
                }
            }
        });
    }
});