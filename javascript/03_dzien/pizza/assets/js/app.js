

fetch("https://instagram.apppi.pl")
    .then(res => res.json())
    .then(function (response) {
        let html ="";
        for (let i = 0; i < response.length; i++) {
            html += '<div class="item">' + '<img src="' + response[i].url +'"></div>';
        }
        document.getElementById("instagram-content").innerHTML = html;
    }).catch(error =>{
        alert(error);
    })

window.addEventListener('scroll', function() {
    let navigation = document.getElementsByTagName('nav')[0];
    if (window.pageYOffset > 100) {
        navigation.classList.add('blue');
    } else {
        navigation.classList.remove('blue');
    }
    if (window.pageYOffset > 0) {
        document.body.classList.add('move')
    } else {
        document.body.classList.remove('move')
    }
    // console.log(navigation);
})

function initMap() {
    // The location of Uluru
    var pizzaHutBonarka = {lat: 50.0293445, lng: 19.94444918};
    // The map, centered at Uluru
    var map = new google.maps.Map(
        document.getElementById('googlemaps'), 
        {
            zoom: 14, 
            center: pizzaHutBonarka,
            styles: [
                {
                    "featureType": "all",
                    "elementType": "all",
                    "stylers": [
                        {
                            "color": "#ff7000"
                        },
                        {
                            "lightness": "69"
                        },
                        {
                            "saturation": "100"
                        },
                        {
                            "weight": "1.17"
                        },
                        {
                            "gamma": "2.04"
                        }
                    ]
                },
                {
                    "featureType": "all",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#cb8536"
                        }
                    ]
                },
                {
                    "featureType": "all",
                    "elementType": "labels",
                    "stylers": [
                        {
                            "color": "#ffb471"
                        },
                        {
                            "lightness": "66"
                        },
                        {
                            "saturation": "100"
                        }
                    ]
                },
                {
                    "featureType": "all",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "gamma": 0.01
                        },
                        {
                            "lightness": 20
                        }
                    ]
                },
                {
                    "featureType": "all",
                    "elementType": "labels.text.stroke",
                    "stylers": [
                        {
                            "saturation": -31
                        },
                        {
                            "lightness": -33
                        },
                        {
                            "weight": 2
                        },
                        {
                            "gamma": 0.8
                        }
                    ]
                },
                {
                    "featureType": "all",
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "landscape",
                    "elementType": "all",
                    "stylers": [
                        {
                            "lightness": "-8"
                        },
                        {
                            "gamma": "0.98"
                        },
                        {
                            "weight": "2.45"
                        },
                        {
                            "saturation": "26"
                        }
                    ]
                },
                {
                    "featureType": "landscape",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "lightness": 30
                        },
                        {
                            "saturation": 30
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "saturation": 20
                        }
                    ]
                },
                {
                    "featureType": "poi.park",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "lightness": 20
                        },
                        {
                            "saturation": -20
                        }
                    ]
                },
                {
                    "featureType": "road",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "lightness": 10
                        },
                        {
                            "saturation": -30
                        }
                    ]
                },
                {
                    "featureType": "road",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "saturation": 25
                        },
                        {
                            "lightness": 25
                        }
                    ]
                },
                {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": [
                        {
                            "lightness": -20
                        },
                        {
                            "color": "#ecc080"
                        }
                    ]
                }
            ]
        });
    // The marker, positioned at Uluru
    var marker = new google.maps.Marker({
        position: pizzaHutBonarka, 
        map: map,
        icon: './assets/images/marker2.png'
    });
  }