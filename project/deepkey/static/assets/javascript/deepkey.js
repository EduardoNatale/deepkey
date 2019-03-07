const input = document.getElementById('input-password');
const tableBody1 = document.getElementById('table1');
const tableBody2 = document.getElementById('table2');
const tableBody3 = document.getElementById('table3');
let id1 = 0;
let id2 = 0;
let id3 = 0;
let manyTimes = 0;
let second = 0;

function add2table1(){
  // alert('dsa');
  second += 1;
  let row = document.createElement('tr');
  row.innerHTML += '<td>' + id1 + '</td>';
  row.innerHTML += '<td>' + manyTimes + '</td>';
  row.innerHTML += '<td>' + second + '</td>';
  tableBody1.appendChild(row);
  id1 += 1;
  manyTimes = 0;
}

function add2table2(e){
  let row = document.createElement('tr');
  row.innerHTML += '<td>' + id2 + '</td>';
  row.innerHTML += '<td>' + e.key + '</td>';
  row.innerHTML += '<td>' + e.keyCode + '</td>';
  tableBody2.appendChild(row);
  id2 += 1;
}

function scrollDiv1(){
  if(document.getElementById('divTable1').scrollTop<(document.getElementById('divTable1').scrollHeight-document.getElementById('divTable1').offsetHeight)){-1
    document.getElementById('divTable1').scrollTop=document.getElementById('divTable1').scrollTop+1000;
  }
}

function scrollDiv2(){
  if(document.getElementById('divTable2').scrollTop<(document.getElementById('divTable2').scrollHeight-document.getElementById('divTable2').offsetHeight)){-1
    document.getElementById('divTable2').scrollTop=document.getElementById('divTable2').scrollTop+1000;
  }
}

function scrollDiv3(){
  if(document.getElementById('divTable3').scrollTop<(document.getElementById('divTable3').scrollHeight-document.getElementById('divTable3').offsetHeight)){-1
    document.getElementById('divTable3').scrollTop=document.getElementById('divTable3').scrollTop+1000;
  }
}

input.onkeydown = function(e) {
    add2table2(e);
    scrollDiv2();
    manyTimes += 1;
}

setInterval(function(){
  add2table1();
  scrollDiv1();
}, 1000);
