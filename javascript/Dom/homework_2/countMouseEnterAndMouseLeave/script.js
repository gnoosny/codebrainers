document.addEventListener("DOMContentLoaded", function () {
	
	
	const moves = document.getElementById('element');
	let mouseEnter = 0;
	let mouseLeave = 0;
	
	moves.addEventListener('mouseenter', function(){
        console.log('mouseenter');
        console.log('mouseEnter');
		mouseEnter +=1
		const enter = document.getElementsByClassName('mouseenter');
		enter[0].innerHTML = 'mouseenter: ' + mouseEnter;
    });
	moves.addEventListener('mouseleave', function(){
        console.log('mouseleave');
        console.log('mouseLeave');
		mouseLeave +=1
		const leave = document.getElementsByClassName('mouseleave');
		leave[0].innerHTML = 'mouseleave: ' + mouseEnter;
    });
	
});
