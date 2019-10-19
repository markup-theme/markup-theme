
/*
* Supports the `.. content-tabs` extension
*/

$(function() {

    var top_sel = {}

    $('div.content-tabs').each(function() {
        var contenttab_sel = $('<ul />', { class: "contenttab-selector" });
        var i = 0;

        $('.tab-content', this).each(function() {
            var sel_item = $('<li />', {
                class: $(this).attr('id'),
                text: $(this).find('.tab-title').text()
            });
            $(this).find('.tab-title').remove();
            if (i++) {
                $(this).hide();
            } else {
                sel_item.addClass('selected');
            }
            contenttab_sel.append(sel_item);
            $(this).addClass('contenttab');
        });

        $('.tab-content', this).eq(0).before(contenttab_sel);
        contenttab_sel = null;
        i = null;
    });


    $('.contenttab-selector li').click(function(evt) {
        evt.preventDefault();

        var tabsblock = $(this).parents('.content-tabs');
        var sel_class = $(this).attr('class');
        $('div.contenttab',tabsblock).hide();
        $('div#' + sel_class,tabsblock).show();

        $('ul.contenttab-selector li', tabsblock).removeClass('selected');
        $('ul.contenttab-selector li.' + sel_class, tabsblock).addClass('selected');

        sel_class = null;
    });

});

