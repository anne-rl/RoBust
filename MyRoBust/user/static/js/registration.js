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
    var date_input = $('input[name="birthdate"]'); //our date input has the name "date"
    var container = $('.bootstrap-iso form').length > 0 ? $('.bootstrap-iso form').parent() : "body";
    var options = {
      format: 'mm/dd/yyyy',
      container: container,
      todayHighlight: true,
      autoclose: true,
    };
    date_input.datepicker(options);
  });
