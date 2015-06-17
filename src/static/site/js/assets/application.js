$(function() {

  /*-----------------------------------------------------------------------------------*/
  /*  Anchor Link
  /*-----------------------------------------------------------------------------------*/
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') 
      || location.hostname == this.hostname) {
        var target = $(this.hash);
    target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
    if (target.length) {
      //if (target.selector.indexOf('section-2')>0)
      //_gaq.push(['_trackEvent', 'Click', 'Button Segregatory', 'Zobacz']);
      $('html,body').animate({
        scrollTop: target.offset().top - 50
      }, 1000);
        return false;
      }
    }
  });

  /*-----------------------------------------------------------------------------------*/
  /*  Tooltips
  /*-----------------------------------------------------------------------------------*/
  $('.tooltip-side-nav').tooltip();
  // fancybox
    $(".fancybox").fancybox({       
        padding : 0,
        autoResize: true,
        beforeShow: function () {
          this.title = $(this.element).attr('title');
          this.title = '<h4>' + this.title + '</h4>' + '<p>' + $(this.element).parent().find('img').attr('alt') + '</p>';
        },
        helpers : {
          title : { type: 'inside' },
        }
      });

});
