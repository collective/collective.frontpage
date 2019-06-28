(function ($) {
  'use strict'; // Start of use strict

  $(document).ready(function () {
    $('.editable-section').hover(function (e) {
      $(this).toggleClass('active');
    });
  });

})(jQuery); // End of use strict
