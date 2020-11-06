/*
	lazyLoadGoogleMaps v1.0.2, updated 2016-11-22
	By Osvaldas Valutis, www.osvaldas.info
	Available for use under the MIT License
*/



(window.googleMapsScriptLoaded = function () {
	$(window).trigger("googleMapsScriptLoaded");
}),
	(function (i, a) {
		"use strict";
		var e = i(a),
			n = i("body"),
			o = e.height(),
			t = 0,
			r = function (i, a) {
				var e = null;
				return function () {
					var n = this,
						o = arguments;
					clearTimeout(e),
						(e = setTimeout(function () {
							a.apply(n, o);
						}, i));
				};
			},
			s = function (i, a) {
				var e, n;
				return function () {
					var o = this,
						t = arguments,
						r = +new Date();
					e && e + i > r
						? (clearTimeout(n),
						  (n = setTimeout(function () {
								(e = r), a.apply(o, t);
						  }, i)))
						: ((e = r), a.apply(o, t));
				};
			},
			c = !1,
			l = !1,
			p = i([]),
			g = function () {
				(t = e.scrollTop()),
					p.each(function () {
						var a = i(this),
							e = a.data("options");
						if (a.offset().top - t > 1 * o) return !0;
						if (!c && !l) {
							var r = { callback: "googleMapsScriptLoaded", signed_in: e.signed_in };
							e.key && (r.key = e.key),
								e.libraries && (r.libraries = e.libraries),
								e.language && (r.language = e.language),
								e.region && (r.region = e.region),
								n.append('<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&' + i.param(r) + '"></script>'),
								(l = !0);
						}
						if (!c) return !0;
						var s = new google.maps.Map(this, { zoom: 15 });
						e.callback !== !1 && e.callback(this, s), (p = p.not(a));
					});
			};
		e
			.on("googleMapsScriptLoaded", function () {
				(c = !0), g();
			})
			.on("scroll", s(500, g))
			.on(
				"resize",
				r(1e3, function () {
					(o = e.height()), g();
				})
			),
			(i.fn.lazyLoadGoogleMaps = function (a) {
				return (
					(a = i.extend({ key: !1, libraries: !1, signed_in: !1, language: !1, region: !1, callback: !1 }, a)),
					this.each(function () {
						var e = i(this);
						e.data("options", a), (p = p.add(e));
					}),
					g(),
					(this.debounce = r),
					(this.throttle = s),
					this
				);
			});
	})(jQuery, window, document);

if ($("#map").length && !$("#map").is(".init")) {
	$("#map").lazyLoadGoogleMaps({
		key: "AIzaSyCo7hljuelb86soVC97y4atK-n_brWfc34",
		// just an API key if you have one

		libraries: false,
		// libraries to load, i.e. 'geometry,places'

		signed_in: false,
		// sign-in on a map enabled/disabled

		language: false,
		// set language, i.e. 'en', 'en-GB'

		region: false,
		// set region, i.e. 'GB'

		callback: function () {
			$stylesMap = [
				{
					featureType: "water",
					elementType: "geometry",
					stylers: [
						{
							color: "#e9e9e9",
						},
						{
							lightness: 17,
						},
					],
				},
				{
					featureType: "landscape",
					elementType: "geometry",
					stylers: [
						{
							color: "#f5f5f5",
						},
						{
							lightness: 20,
						},
					],
				},
				{
					featureType: "road.highway",
					elementType: "geometry.fill",
					stylers: [
						{
							color: "#ffffff",
						},
						{
							lightness: 17,
						},
					],
				},
				{
					featureType: "road.highway",
					elementType: "geometry.stroke",
					stylers: [
						{
							color: "#ffffff",
						},
						{
							lightness: 29,
						},
						{
							weight: 0.2,
						},
					],
				},
				{
					featureType: "road.arterial",
					elementType: "geometry",
					stylers: [
						{
							color: "#ffffff",
						},
						{
							lightness: 18,
						},
					],
				},
				{
					featureType: "road.local",
					elementType: "geometry",
					stylers: [
						{
							color: "#ffffff",
						},
						{
							lightness: 16,
						},
					],
				},
				{
					featureType: "poi",
					elementType: "geometry",
					stylers: [
						{
							color: "#f5f5f5",
						},
						{
							lightness: 21,
						},
					],
				},
				{
					featureType: "poi.park",
					elementType: "geometry",
					stylers: [
						{
							color: "#dedede",
						},
						{
							lightness: 21,
						},
					],
				},
				{
					elementType: "labels.text.stroke",
					stylers: [
						{
							visibility: "on",
						},
						{
							color: "#ffffff",
						},
						{
							lightness: 16,
						},
					],
				},
				{
					elementType: "labels.text.fill",
					stylers: [
						{
							saturation: 36,
						},
						{
							color: "#333333",
						},
						{
							lightness: 40,
						},
					],
				},
				{
					elementType: "labels.icon",
					stylers: [
						{
							visibility: "off",
						},
					],
				},
				{
					featureType: "transit",
					elementType: "geometry",
					stylers: [
						{
							color: "#f2f2f2",
						},
						{
							lightness: 19,
						},
					],
				},
				{
					featureType: "administrative",
					elementType: "geometry.fill",
					stylers: [
						{
							color: "#fefefe",
						},
						{
							lightness: 20,
						},
					],
				},
				{
					featureType: "administrative",
					elementType: "geometry.stroke",
					stylers: [
						{
							color: "#fefefe",
						},
						{
							lightness: 17,
						},
						{
							weight: 1.2,
						},
					],
				},
			];
			//$('#geomarker').data('latitude')
			//$('#geomarker').data('longitude')
			var center = {
				lat: $('#geomarker').data('latitude'),
				lng: $('#geomarker').data('longitude'),
			};
			var marker, icon;

			function initMap() {
				map = new google.maps.Map(document.getElementById("map"), {
					zoom: 11,
					center: center,
					styles: $stylesMap,
					zoom: 16,
					scrollwheel: false,
					clickableIcons: false,
				});

				icon = {
					url: "/static/app/img/pin-color.svg", // url
					scaledSize: new google.maps.Size(35, 56), // scaled size
					origin: new google.maps.Point(0, 0), // origin
					anchor: new google.maps.Point(17, 18), // anchor
				};

				marker = new google.maps.Marker({
					icon: icon,
					position: center,
					map: map,
				});
			}

			initMap();
		},
	});
}
