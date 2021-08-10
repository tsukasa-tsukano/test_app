$(function() {
    var today = new Date();
    var y = today.getFullYear();
    $('#mdp-demo').multiDatesPicker({
        altField: '#altField',
        changeMonth: true,
        dateFormat: 'yy/mm/dd',
    });
});
