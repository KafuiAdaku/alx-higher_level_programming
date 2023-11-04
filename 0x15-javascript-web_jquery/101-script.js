$(document).ready(() => {
  $('DIV#add_item').click(() => {
    const item = $('<li></li>').text('Item');
    $('UL.my_list').append(item);
  });
  $('DIV#remove_item').click(() => {
    $('UL.my_list').find('li:last').remove();
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
});
