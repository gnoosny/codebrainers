document.addEventListener("DOMContentLoaded", function () {

    //alert("Alert");
    // const btn = document.getElementById('przycisk');
    //  console.log(btn.tagName);
    const year = document.getElementsByClassName('currentYear');
    let date = new Date();
    year[0].innerHTML = '2019';

    const btn = document.getElementById('showText');

    btn.addEventListener('click', function(){
        alert('o k@##$$#')
    })

    btn.addEventListener('mouseenter', function(){
        alert('o k@##$$#')
    })

    const bunny = document.getElementById('kroliczek');
    bunny.addEventListener('mouseleave', function(){
        alert('czemu opuszczasz króliczka?')
    })

    const beetle = document.getElementById('beetle');
    beetle.addEventListener('mouseenter', function(){
        console.log('mouseenter');
    })
    beetle.addEventListener('mouseleave', function(){
        console.log('mouseleave');
    })
    beetle.addEventListener('mouseover', function(){
        console.log('mouseover');
    })
    beetle.addEventListener('mouseout', function(){
        console.log('mouseout');
    })
})
//mouseenter, mouseleave, mouseover, mouseout
