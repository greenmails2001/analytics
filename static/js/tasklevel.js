/**
 * Created by lanpq on 11/15/2016.
 */
$(function(){
function CreateGroup(group_name)
{
    // Create Button(Image)
    //alert(group_name);
    $('td.' + group_name).prepend("<img class='" + group_name + " button_closed'> ");
    // Add Padding to Data
    $('tr.' + group_name).each(function () {
        var first_td = $(this).children('td').first();
        var padding_left = parseInt($(first_td).css('padding-left'));
        $(first_td).css('padding-left', String(padding_left + 25) + 'px');
    });
    RestoreGroup(group_name);

    // Tie toggle function to the button
    $('img.' + group_name).click(function(){
        ToggleGroup(group_name);
    });
}

function ToggleGroup(group_name)
{
    ToggleButton($('img.' + group_name));
    RestoreGroup(group_name);
}

function RestoreGroup(group_name)
{
    if ($('img.' + group_name).hasClass('button_open'))
    {
        // Open everything
        $('tr.' + group_name).show();

        // Close subgroups that been closed
        $('tr.' + group_name).find('img.button_closed').each(function () {
            sub_group_name = $(this).attr('class').split(/\s+/)[0];
            //console.log(sub_group_name);
            RestoreGroup(sub_group_name);
        });
    }

    if ($('img.' + group_name).hasClass('button_closed'))
    {
        // Close everything
        $('tr.' + group_name).hide();
    }
}

function ToggleButton(button)
{
    $(button).toggleClass('button_open');
    $(button).toggleClass('button_closed');
}

CreateGroup('group1');
CreateGroup('group2');
CreateGroup('sub_group1');
CreateGroup('sub_group2');
CreateGroup('sub_sub_group1');
});