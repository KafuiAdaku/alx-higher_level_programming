$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const langCode = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`,
      (data) => {
        $('DIV#hello').text(data.hello);
      });
  });
});
