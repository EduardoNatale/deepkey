const textArea1 = document.getElementById('txtArea1');
const textArea2 = document.getElementById('txtArea2');
let manyTimes = 0;
let second = 0;
let lText = []
let id = 0;

function add2table3(type) {
  let d = new Date();
  let n = d.getTime();
  lText.push([id, n, type]);
  console.log(lText);
  id += 1;
}

textArea2.onkeydown = function(e) {
  if (e.keyCode != 13) {
    manyTimes += 1;
    add2table3('DOWN');
  }
}

textArea2.onkeyup = function(e) {
  if (e.keyCode != 13) {
    add2table3('UP');
  }
}

function myFunction() {
    document.getElementById('data').value = lText;
}

setInterval(function(){
  second += 1;
}, 1000);