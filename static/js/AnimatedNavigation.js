var AnimatedNavigation = (function() {

	var docElem = document.documentElement,
		header = document.querySelector( '.main-header' ),
		didScroll = false,
		changeHeaderOn = 250;

	function init() {
		window.addEventListener( 'scroll', function( event ) {
			if( !didScroll ) {
				didScroll = true;
				setTimeout( scrollPage, 100 );
			}
		}, false );
	}

	function scrollPage() {
		var sy = scrollY();
		if ( sy >= changeHeaderOn ) {
			classes.add( header, 'main-header-compressed' );
		}
		else {
			classes.remove( header, 'main-header-compressed' );
		}
		didScroll = false;
	}

	function scrollY() {
		return window.pageYOffset || docElem.scrollTop;
	}

	init();

})();
