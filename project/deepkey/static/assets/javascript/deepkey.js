const input = document.getElementById('input-password')
const input1 = document.getElementById('input-password1')

input.onkeydown = function(e) {

    input1.value = e.key;

}
