  /* global $ */
  /* global FileReader */
  /* global document */
  /* eslint-env es6 */
  /* eslint-disable */
  $(document).ready(function () {
    // Prepare the preview for profile picture
    $("#profilePicture").change(function () {
      readURL(this);
    });
  });

  function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
        $('#profilePicturePreview').attr('src', e.target.result).fadeIn('slow');
      }
      reader.readAsDataURL(input.files[0]);
    }
  }
  $(document).ready(function () {
    $(".dropdown").hover(function () {
      var dropdownMenu = $(this).children(".dropdown-menu");
      if (dropdownMenu.is(":visible")) {
        dropdownMenu.parent().toggleClass("open");
      }
    });
  });
