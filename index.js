var table = new DataTable('#example', {
    "ajax": {
        "url": "MOCK_DATA.json"
    },
    "columns": [
        { "data": "first_name", render: (data, type, row) => data + ' ' + row['last_name'], },
        { "data": "date_of_birth" },
        { "data": "street_address" },
        { "data": "city" },
        { "data": "state" },
        { "data": "zipcode" },
        { "data": "email" },
        { "data": "phone_number" },
        { "data": "first_name", visible: false},
        { "data": "last_name", visible: false}
    ],
    initComplete: function (settings,json) {
        table.column(4)
        .data()
        .unique()
        .sort()
        .each(function (d, j) {
            $('#state_input').append(new Option(d));
        });
    },
    dom: 'lrtip',

});
table.on('click', 'tbody tr', (e) => {
    let classList = e.currentTarget.classList;

    if (classList.contains('selected')) {
        classList.remove('selected');
        $('#selected_name').text('');
        $('#selected_email').text('');
        $('#selected_phone').text('');
        $('#selected_address').text('');
    }
    else {
        table.rows('.selected').nodes().each((row) => row.classList.remove('selected'));
        classList.add('selected');
        $('#selected_name').text(e.currentTarget.cells[0].innerHTML);
        $('#selected_email').text(e.currentTarget.cells[6].innerHTML);
        $('#selected_phone').text(e.currentTarget.cells[7].innerHTML);
        $('#selected_address').text(e.currentTarget.cells[2].innerHTML);
    }
});

function filter(element, col_no) {
    $(element).on('change',function() {
    table
    .column(col_no)
    .search(this.value)
    .draw();
    });
}

function populate_filter() {
    filter('#first_name_input',8)
    filter('#last_name_input',9)
    filter('#email_input',6)
    filter('#date_of_birth_input',1)
    filter('#address_input',2)
    filter('#city_input',3)
    filter('#state_input',4)
    filter('#phone_input',7)
    filter('#zipcode_input',5)
}

$(document).ready(function(){

    populate_filter() 

$('#search').on('click', function () {
    populate_filter() 
});
});