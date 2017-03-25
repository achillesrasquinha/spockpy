function startCounter(counter, callback) {
	$('.counter').html(counter);
	console.log($('.counter').html());

	if ( counter == 0 ) {
		callback()
	} else {
		setTimeout(function ( ) {
			counter = counter - 1;
			startCounter(counter, callback)
		}, 1000);
	}
}

$(document).ready(function() {
	$('.play').click(function () {
		console.log('play clicked');
		var counter = 3;

		startCounter(counter, function () {
			console.log('counter done');
		});
	});
})
	