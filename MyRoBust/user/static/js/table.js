 $(document).ready(function() {
    let initialTableSettings = {
      "pageLength": 10,
      "lengthMenu": [
        [10, 20, 30, -1],
        [10, 20, 30, "All"]
      ],
      dom: 'flrtBi<"posR"p>',
      buttons: [
        'copy',
        'excel'
      ]
    }

    $.fn.dataTable.ext.search.push(
      function(settings, data, dataIndex) {
        var min = $('#min').datepicker("getDate");
        var max = $('#max').datepicker("getDate");
        // need to change str order before making  date obect since it uses a new Date("mm/dd/yyyy") format for short date.
        var startDate = new Date(data[0])
        if (min == null && max == null) {
          return true;
        }
        if (min == null && startDate <= max) {
          return true;
        }
        if (max == null && startDate >= min) {
          return true;
        }
        if (startDate <= max && startDate >= min) {
          return true;
        }
        return false;
      }
    );

    $("#min").datepicker({
      onSelect: function() {
        table.draw();
      },
      changeMonth: true,
      changeYear: true,
      dateFormat: "dd/mm/yy"
    });
    $("#max").datepicker({
      onSelect: function() {
        table.draw();
      },
      changeMonth: true,
      changeYear: true,
      dateFormat: "dd/mm/yy"
    });
    var table = $('#myHistoryTable').DataTable(initialTableSettings);

    // Event listener to the two range filtering inputs to redraw on input
    $('#min, #max').change(function() {
      table.draw();
    });

  });

  $(document).ready(function() {
    //Activate tooltip
    $('[data-toggle="tooltip"]').tooltip();
  });