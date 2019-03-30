

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