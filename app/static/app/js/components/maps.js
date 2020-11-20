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
		key: "AIzaSyCMALW2kJxKFPHCewCJWSS4bnHZtNCm3iU",
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
					"featureType": "all",
					"elementType": "labels.text.fill",
					"stylers": [
						{
							"color": "#a8afbf"
						}
					]
				},
				{
					"featureType": "all",
					"elementType": "labels.text.stroke",
					"stylers": [
						{
							"visibility": "on"
						},
						{
							"color": "#373d48"
						},
						{
							"weight": 2
						},
						{
							"gamma": "1"
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
					"featureType": "administrative",
					"elementType": "geometry",
					"stylers": [
						{
							"weight": 0.6
						},
						{
							"gamma": "0"
						},
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "administrative.country",
					"elementType": "geometry.stroke",
					"stylers": [
						{
							"visibility": "on"
						},
						{
							"color": "#111115"
						}
					]
				},
				{
					"featureType": "administrative.country",
					"elementType": "labels.text",
					"stylers": [
						{
							"visibility": "on"
						},
						{
							"weight": "0.50"
						}
					]
				},
				{
					"featureType": "administrative.country",
					"elementType": "labels.text.stroke",
					"stylers": [
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "administrative.province",
					"elementType": "labels.text",
					"stylers": [
						{
							"visibility": "on"
						}
					]
				},
				{
					"featureType": "administrative.locality",
					"elementType": "labels.text",
					"stylers": [
						{
							"visibility": "on"
						}
					]
				},
				{
					"featureType": "administrative.locality",
					"elementType": "labels.text.stroke",
					"stylers": [
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "administrative.neighborhood",
					"elementType": "labels.text",
					"stylers": [
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "administrative.land_parcel",
					"elementType": "labels",
					"stylers": [
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "administrative.land_parcel",
					"elementType": "labels.text",
					"stylers": [
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "landscape",
					"elementType": "geometry",
					"stylers": [
						{
							"color": "#1b1c25"
						},
						{
							"gamma": "1"
						},
						{
							"weight": "10"
						}
					]
				},
				{
					"featureType": "landscape",
					"elementType": "geometry.stroke",
					"stylers": [
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "landscape.natural",
					"elementType": "labels.text",
					"stylers": [
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "landscape.natural.landcover",
					"elementType": "labels.text",
					"stylers": [
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "landscape.natural.terrain",
					"elementType": "labels.text",
					"stylers": [
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "poi",
					"elementType": "geometry",
					"stylers": [
						{
							"color": "#0050ff"
						},
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "poi",
					"elementType": "labels.text",
					"stylers": [
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "poi.park",
					"elementType": "geometry",
					"stylers": [
						{
							"color": "#424d66"
						},
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "road",
					"elementType": "geometry",
					"stylers": [
						{
							"color": "#21222c"
						},
						{
							"lightness": "0"
						}
					]
				},
				{
					"featureType": "transit",
					"elementType": "geometry",
					"stylers": [
						{
							"visibility": "off"
						}
					]
				},
				{
					"featureType": "water",
					"elementType": "geometry",
					"stylers": [
						{
							"color": "#16171f"
						},
						{
							"gamma": "1.00"
						}
					]
				},
				{
					"featureType": "water",
					"elementType": "labels.text",
					"stylers": [
						{
							"visibility": "on"
						},
						{
							"lightness": "-60"
						}
					]
				}
			];
			let lat = $('#geomarker').data('latitude')
			let lng = $('#geomarker').data('longitude')
			var center = {
				lat: lat,
				lng: lng,
			};
			var marker, icon;

			function initMap() {
				map = new google.maps.Map(document.getElementById("map"), {
					zoom: 12,
					center: center,
					styles: $stylesMap,
					zoom: 17,
					scrollwheel: false,
					clickableIcons: false,
				});

				icon = {
					url: $('#maps_ico').data('maps-ico'), // url
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
