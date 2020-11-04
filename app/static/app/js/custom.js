$(window).on("load", function () {
	if (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
		$("body").addClass("ios");
	} else {
		$("body").addClass("web");
	}
	var currentValue = 0;
	for (var i = 0; i < Math.abs(100); ++i) {
		setTimeout(function () {
			currentValue += 1;
			if (currentValue <= 10) {
				$(".load-screen__number").text("00" + currentValue);
			} else if (currentValue >= 10 && currentValue < 100) {
				$(".load-screen__number").text("0" + currentValue);
			} else {
				$(".load-screen__number").text(currentValue);
			}
		}, 20 * i);
	}
	setTimeout(function () {
		$("body").removeClass("loaded");
		$("body").addClass("loading");
		AOS.init({
			offset: 0,
			duration: 500,
			once: true,
			disable: "mobile",
		});
		var $anim_scroll = $("body.loading .slick-current .main-slider__title"),
			anim_time = 0.5,
			anim_stagger = 0.05,
			initial_delay = 0.3,
			easing = Power2.easeOut,
			elem_y = 35;
		for (var i = 0; i < $anim_scroll.length; i++) {
			var $anim = $anim_scroll.eq(i).find(".letter-measure");
			var tl = new TimelineLite();
			tl.staggerTo($anim, anim_time, { y: 0, opacity: 1, ease: easing }, anim_stagger, (i + 1) * 0.3);
		}
	}, 2000);
	var isshow = localStorage.getItem("isshow");
	if (isshow == null) {
		localStorage.setItem("isshow", 1);
		$(".popup-cookies").addClass("active");
	}
});

/* viewport width */
function viewport() {
	var e = window,
		a = "inner";
	if (!("innerWidth" in window)) {
		a = "client";
		e = document.documentElement || document.body;
	}
	return { width: e[a + "Width"], height: e[a + "Height"] };
}
/* viewport width */
$(function () {
	/* placeholder*/
	$("input, textarea").each(function () {
		var placeholder = $(this).attr("placeholder");
		$(this).focus(function () {
			$(this).attr("placeholder", "");
		});
		$(this).focusout(function () {
			$(this).attr("placeholder", placeholder);
		});
	});
	/* placeholder*/
	$(".js-cookies-close").click(function () {
		$(".popup-cookies").removeClass("active");
		return false;
	});
	/*button open main nav begin*/
	$(".js-button-nav").click(function () {
		$(".menu-wrapper").addClass("is-active");
		$("body").addClass("noscroll");
		$("html").addClass("noscroll");
		return false;
	});
	$(".nav-mask, .js-close-nav").click(function () {
		$(".menu-wrapper").removeClass("is-active");
		$("body").removeClass("noscroll");
		$("html").removeClass("noscroll");
		return false;
	});

	/*button open main nav end*/
	$(".js-list-faq li a").click(function () {
		$(this).parent().toggleClass("active");
		$(this).parent().siblings().removeClass("active");
		$(this).parent().siblings().find(".list-faq__answer").slideUp();
		$(this).next().slideToggle();
		$(".main-nav-list").slideToggle();
		return false;
	});

	/*scroll id*/
	$(".js-anchor li a").click(function () {
		$(".menu-wrapper").removeClass("is-active");
		$("body").removeClass("noscroll");
		$("html").removeClass("noscroll");
		var target = $(this).attr("href");
		$("html, body").animate(
			{
				scrollTop: $(target).offset().top,
			},
			1000
		);
		return false;
	});
	$(".js-anchor-id").click(function () {
		var targetId = $(this).attr("href");
		$("html, body").animate(
			{
				scrollTop: $(targetId).offset().top,
			},
			1000
		);
		return false;
	});
	/*scroll id*/
	$(".js-scroll-right").on("click", function () {
		$(".advantages-row").animate(
			{
				scrollLeft: "+=200px",
			},
			"slow"
		);
		return false;
	});

	if ($(".file-img").length) {
		function readURL(input) {
			if (input.files && input.files[0]) {
				var holder = document.getElementById("holder");
				var reader = new FileReader();
				reader.onload = function (e) {
					holder.style.backgroundImage = "url(" + e.target.result + ")";
					$("#holder").addClass("img-active");
				};
				reader.readAsDataURL(input.files[0]);
			}
		}
		$("#imgInp").change(function () {
			readURL(this);
		});
		var holder = $("#holder");
		holder.ondrop = function (e) {
			this.classList.add("img-active");
			e.preventDefault();
			var file = e.dataTransfer.files[0],
				reader = new FileReader();
			reader.onload = function (event) {
				holder.style.backgroundImage = "url(" + event.target.result + ")";
			};
			reader.readAsDataURL(file);
			return false;
		};
	}

	/* components begin*/
	$(".js-aos-letter").each(function () {
		var $el = $(this);
		$el.splitText({ type: "words", animation: "explode" });
	});
	$(".js-aos-letter .word-measure").each(function () {
		var $el = $(this);
		$el.splitText({ type: "letters", animation: "explode" });
		TweenMax.set($el.find(".letter-measure"), { opacity: 0, y: 15 });
	});
	document.addEventListener("aos:in:title-0", function (detail) {
		var $anim_scroll = $(".title-0"),
			anim_time = 0.5,
			anim_stagger = 0.05,
			initial_delay = 0.3,
			easing = Power2.easeOut,
			elem_y = 35;

		for (var i = 0; i < $anim_scroll.length; i++) {
			var $anim = $anim_scroll.eq(i).find(".letter-measure");
			var tl = new TimelineLite();
			tl.staggerTo($anim, anim_time, { y: 0, opacity: 1, ease: easing }, anim_stagger, (i + 1) * 0.3);
		}
	});
	document.addEventListener("aos:in:title-1", function (detail) {
		var $anim_scroll = $(".title-1"),
			anim_time = 0.5,
			anim_stagger = 0.05,
			initial_delay = 0.3,
			easing = Power2.easeOut,
			elem_y = 35;

		for (var i = 0; i < $anim_scroll.length; i++) {
			var $anim = $anim_scroll.eq(i).find(".letter-measure");
			var tl = new TimelineLite();
			tl.staggerTo($anim, anim_time, { y: 0, opacity: 1, ease: easing }, anim_stagger, (i + 1) * 0.3);
		}
	});
	document.addEventListener("aos:in:title-2", function (detail) {
		var $anim_scroll = $(".title-2"),
			anim_time = 0.5,
			anim_stagger = 0.05,
			initial_delay = 0.3,
			easing = Power2.easeOut,
			elem_y = 35;

		for (var i = 0; i < $anim_scroll.length; i++) {
			var $anim = $anim_scroll.eq(i).find(".letter-measure");
			var tl = new TimelineLite();
			tl.staggerTo($anim, anim_time, { y: 0, opacity: 1, ease: easing }, anim_stagger, (i + 1) * 0.3);
		}
	});
	document.addEventListener("aos:in:title-3", function (detail) {
		var $anim_scroll = $(".title-3"),
			anim_time = 0.5,
			anim_stagger = 0.05,
			initial_delay = 0.3,
			easing = Power2.easeOut,
			elem_y = 35;

		for (var i = 0; i < $anim_scroll.length; i++) {
			var $anim = $anim_scroll.eq(i).find(".letter-measure");
			var tl = new TimelineLite();
			tl.staggerTo($anim, anim_time, { y: 0, opacity: 1, ease: easing }, anim_stagger, (i + 1) * 0.3);
		}
	});
	document.addEventListener("aos:in:title-4", function (detail) {
		var $anim_scroll = $(".title-4"),
			anim_time = 0.5,
			anim_stagger = 0.05,
			initial_delay = 0.3,
			easing = Power2.easeOut,
			elem_y = 35;

		for (var i = 0; i < $anim_scroll.length; i++) {
			var $anim = $anim_scroll.eq(i).find(".letter-measure");
			var tl = new TimelineLite();
			tl.staggerTo($anim, anim_time, { y: 0, opacity: 1, ease: easing }, anim_stagger, (i + 1) * 0.3);
		}
	});
	if ($(".js-main-slider").length) {
		$(".js-main-slider").slick({
			dots: true,
			infinite: true,
			fade: true,
			rows: 0,
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			autoplay: true,
			autoplaySpeed: 7000,
			pauseOnFocus: false,
			pauseOnHover: false,
		});
		$(".main-slider__title").each(function () {
			var $el = $(this);
			$el.splitText({ type: "words", animation: "explode" });
		});
		$(".main-slider__title .word-measure").each(function () {
			var $el = $(this);
			$el.splitText({ type: "letters", animation: "explode" });
		});
		TweenMax.set($(".main-slider__title").find(".letter-measure"), { opacity: 0, y: 15 });

		$(".js-main-slider").on("beforeChange", function (event, slick, currentSlide, nextSlide) {
			TweenMax.set($(".slick-slide.slick-current .main-slider__title").find(".letter-measure"), { opacity: 0, y: 15 });
			var $anim_scroll = $(".slick-slide:not(.slick-current) .main-slider__title"),
				anim_time = 0.5,
				anim_stagger = 0.05,
				initial_delay = 0.3,
				easing = Power2.easeOut,
				elem_y = 35;

			for (var i = 0; i < $anim_scroll.length; i++) {
				var $anim = $anim_scroll.eq(i).find(".letter-measure");
				var tl = new TimelineLite();
				tl.staggerTo($anim, anim_time, { y: 0, opacity: 1, ease: easing }, anim_stagger, (i + 1) * 0.3);
			}
		});
	}

	if ($(".js-reviews-slider").length) {
		$(".js-reviews-slider").slick({
			dots: true,
			infinite: false,
			speed: 300,
			rows: 0,
			slidesToShow: 4,
			slidesToScroll: 1,
			variableWidth: true,
			prevArrow: '<button type="button" data-role="none" class="slick-prev" aria-label="Previous" tabindex="0" role="button"><i class="icon-arrow-left"></i></button>',
			nextArrow: '<button type="button" data-role="none" class="slick-next" aria-label="Next" tabindex="0" role="button"><i class="icon-arrow-right"></i></button>',
			responsive: [
				{
					breakpoint: 500,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1,
						arrows: false,
						variableWidth: false,
						dots: true,
					},
				},
			],
		});
	}

	if ($(".js-catalog-list").length) {
		$(".js-catalog-list").slick({
			dots: true,
			infinite: false,
			speed: 300,
			rows: 0,
			slidesToShow: 1,
			slidesToScroll: 1,
			prevArrow: '<button type="button" data-role="none" class="slick-prev" aria-label="Previous" tabindex="0" role="button"><i class="icon-arrow-left"></i></button>',
			nextArrow: '<button type="button" data-role="none" class="slick-next" aria-label="Next" tabindex="0" role="button"><i class="icon-arrow-right"></i></button>',
			responsive: [
				{
					breakpoint: 6000,
					settings: "unslick",
				},
				{
					breakpoint: 1023,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1,
						adaptiveHeight: true,
						infinite: true,
					},
				},
			],
		});
	}

	if ($(".js-fancybox").length) {
		$(".js-fancybox").fancybox({
			margin: 30,
			padding: 0,
			touch: false,
			afterShow: function () {
				if (!throttleTimeout) {
					throttleTimeout = setTimeout(function () {
						api.reinitialise();
						throttleTimeout = null;
					}, 50);
				}
				if ($(".js-gallery-lg").length) {
					$(".js-gallery-lg").slick("getSlick").refresh();
					$(".js-gallery-sm").slick("getSlick").refresh();
				}
			},
			afterClose: function () {
				$("form").removeClass("hide-form").trigger("reset");
				$(".popup-thank").removeClass("show");
			},
		});
	}
	if ($(".js-gallery").length) {
		$(".js-gallery-lg").slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			fade: true,
			dots: false,
			asNavFor: ".js-gallery-sm",
		});
		$(".js-gallery-sm").slick({
			slidesToShow: 3,
			slidesToScroll: 1,
			asNavFor: ".js-gallery-lg",
			dots: false,
			focusOnSelect: true,
			arrows: false,
			responsive: [
				{
					breakpoint: 480,
					settings: {
						slidesToShow: 3,
					},
				},
			],
		});
	}
	/* styled scroll*/
	if ($(".js-scroll").length) {
		$(".js-scroll").jScrollPane({
			verticalDragMinHeight: 23,
			verticalDragMaxHeight: 23,
		});
		var api = $(".js-scroll").data("jsp");
		var throttleTimeout;
		$(".js-remove-basket-item").click(function () {
			$(this).parents(".basket-products__item").remove();
			if (!throttleTimeout) {
				throttleTimeout = setTimeout(function () {
					api.reinitialise();
					throttleTimeout = null;
				}, 50);
			}
			return false;
		});
		$(window).bind("resize", function () {
			if (!throttleTimeout) {
				throttleTimeout = setTimeout(function () {
					api.reinitialise();
					throttleTimeout = null;
				}, 50);
			}
		});
	}

	if ($(".js-rating").length) {
		$(".js-rating").addRating();
	}
	if ($(".js-range-slider").length) {
		function my_prettify(n) {
			if (n < 1000) {
				return n + " кг";
			} else {
				return (n / 1000).toFixed(0) + " тон";
			}
		}
		$(".js-range-slider").ionRangeSlider({
			min: 40,
			max: 22000,
			prettify: my_prettify,
		});
	}

	if ($(".js-phone-mask").length) {
		$(".js-phone-mask").mask("+38(000)000-00-00");
	}

	$("#review-form").validate({
		rules: {
			name: "required",
			entry: "required",
		},
		messages: {
			name: "*Обязательное поле",
			entry: "*Обязательное поле",
		},
		submitHandler: function (form) {
			$("#review-form").addClass("hide-form");
			$("#review-form").next().addClass("show");
		},
	});

	$("#order").validate({
		rules: {
			name: "required",
			tell: "required",
		},
		messages: {
			name: "*Обязательное поле",
			tell: "*Обязательное поле",
		},
		submitHandler: function (form) {
			$("#order").addClass("hide-form");
			$("#order").next().addClass("show");
		},
	});
	$("#callback").validate({
		rules: {
			name: "required",
			tell: "required",
		},
		messages: {
			name: "*Обязательное поле",
			tell: "*Обязательное поле",
		},
		submitHandler: function (form) {
			$("#callback").addClass("hide-form");
			$("#callback").next().addClass("show");
		},
	});
	$("#subscribe").validate({
		rules: {
			mail: "required",
		},
		messages: {
			mail: "*Обязательное поле",
		},
		submitHandler: function (form) {
			$(".js-thank").click();
		},
	});

	//

	$(".js-checked input:checkbox").live("change", function () {
		var $box = $(this);
		if ($box.is(":checked")) {
			$(".box-field_hidden").addClass("show");
		} else {
			$(".box-field_hidden").removeClass("show");
		}
	});
	/* components end*/
});

var handler = function () {
	var height_footer = $("footer").height();
	var height_header = $("header").height();
	//$('.content').css({'padding-bottom':height_footer+40, 'padding-top':height_header+40});

	var viewport_wid = viewport().width;
	var viewport_height = viewport().height;

	if (viewport_wid <= 1023) {
		if ($(".js-catalog-list").length) {
			$(".js-catalog-list").slick("getSlick").refresh();
		}
	}
};
$(window).bind("load", handler);
$(window).bind("resize", handler);

$(window).scroll(function () {
	var s = $(window).scrollTop(),
		d = $(document).height(),
		c = $(window).height();
	scrollPercent = (s / (d - c)) * 100;
	var position = scrollPercent;

	$("#progressbar").css("width", position + "%");
});

if ($(".call-phone").length) {
	var offset_this = $("#catalog-last").offset().top - $(window).height();
	$(window).scroll(function () {
		if ($(window).scrollTop() >= offset_this) {
			$(".call-phone").addClass("show");
		}
	});

	$(window).load(function () {
		if ($(window).scrollTop() >= offset_this) {
			$(".call-phone").addClass("show");
		}
	});


}

$('#subscribe').submit(function(event) {
		
		event.preventDefault();
		var data = $(this).serializeArray()
		if (this.mail.value) {
			var url = this.action
		$.post(url,data, function(data) {})
		}
		
	});

$('#review-form').submit(function(event) {
		event.preventDefault();

		var stars_container = $('#rating_feedback_container').children('span').children('span').text()
		if (stars_container == '-') {stars_container = 0}
		var data = $(this).serializeArray()
		data[3]['name'] = 'rating'
		data[3]['value'] = stars_container
		var url = this.action
		//$.post(url,data, function(data) {})
		$.ajaxSetup({
		  url: url, 
		  type: 'POST',
		  dataType: 'json',
		  beforeSend: function(){},
		  error: function(req, text, error){},
		  complete: function(){}
		});
	    var $that = $(this),
	    formData = new FormData($that.get(0));
	    formData.append('rating', stars_container)
	    $.ajax({
	      	contentType: false,
	      	processData: false,
	      	data: formData,
	      	success: function(json){
	        	if(json){
	        	}
	      	}
	    });
	
	});

$('#callback').submit(function(event) {
		
		event.preventDefault();
		var data = $(this).serializeArray()
		var url = this.action
		$.post(url,data, function(data) {})
		
	});

$('#order').submit(function(event) {	
	event.preventDefault();
	var data = $(this).serializeArray()
	var count_product = $('.irs-single').text()
	data['4'] = {'name':'count_product', 'value': count_product}
	var url = this.action
	$.post(url,data, function(data) {})
	});


$('#add_order_but').live('click', function(event) {
	$('#pk_value_input').remove()
	var pk_value = $(this).data('pk_product')
	var input_pk_value = $('<input>').attr({
		'value': pk_value,
		'name': 'product_pk',
		'id' : 'pk_value_input',
		'type' : 'hidden'
	});
	$('#order').append(input_pk_value)
});
	

	


	
	


/*animation*/
