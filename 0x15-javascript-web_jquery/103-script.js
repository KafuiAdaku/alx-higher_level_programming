$(document).ready(() => {
  const fetchTranslation = () => {
    const langCode = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, (data) => {
      $('DIV#hello').text(data.hello);
    });
  };

  $('INPUT#btn_translate').on({
    click: fetchTranslation
  });

  $('INPUT#language_code').on({
    focus: fetchTranslation,
    keyup: function (event) {
      if (event.key === 'Enter') {
        fetchTranslation();
      }
    }
  });
});
