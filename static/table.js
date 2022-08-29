let button_click_counter = 0;
function back_to_main(){
    button_click_counter += 1;
    if (button_click_counter == 3){
        location.href = './';
        button_click_counter = 0;
    }
}