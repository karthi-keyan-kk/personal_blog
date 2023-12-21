let title = document.getElementById("title")
let content = document.getElementById("content")
let add_btn = document.getElementById("add_btn")

setInterval(enable, 1000)
function enable(){
    if (content.value.length > 0 && title.value.length){
        add_btn.disabled = false
    }
    else{
        add_btn.disabled = true
    }
}