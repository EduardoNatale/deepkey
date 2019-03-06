const input = document.getElementById('input-password')
const input1 = document.getElementById('input-password1')
const tableBody = document.querySelector('.table');
let id = 0

function add2table(e){
  let row = document.createElement('tr');
  row.innerHTML += '<td>' + id + '</td>';
  row.innerHTML += '<td>' + e.key + '</td>';
  row.innerHTML += '<td>' + e.keyCode + '</td>';
  tableBody.appendChild(row);
  id += 1;
}

function ScrollDiv(){
  if(document.getElementById('ecran').scrollTop<(document.getElementById('ecran').scrollHeight-document.getElementById('ecran').offsetHeight)){-1
    document.getElementById('ecran').scrollTop=document.getElementById('ecran').scrollTop+1000;
  }
}

input.onkeydown = function(e) {
    input1.value = e.key;
    add2table(e);
    ScrollDiv();
}
