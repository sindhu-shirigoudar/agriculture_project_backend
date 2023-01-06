$(window).scroll(function() {
    var scroll = $(window).scrollTop();
    
      $(".parallax-one").css({
          top: 250 + (scroll/250)
      });
  });
  
  $(window).scroll(function() {
    var scroll = $(window).scrollTop();
      $(".parallax-two").css({
          top: 388 + (scroll/2)
      });
  });