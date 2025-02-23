let userdata = [["loki5129",18,true]];

function submitData() {
 let userdata1 = []
 let username = document.getElementById('username').value;
 let age = document.getElementById('age').value;
 if (!username) {
   alert("Please enter a username");
   return;
 }else {
    userdata1.push(username);
  }
 if (!age || age<0 && age>111){
   return;
 }else{
  userdata1.push(Number(age));
  
 }

 const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
 if (checkboxes.length === 0) {
   alert("Please select at least one checkbox");
 }else if (checkboxes.length > 1) {
  alert("Please select only one checkbox");
 }else {
  userdata1.push(checkboxes[0].value === "True" ? true : false);
  }

  userdata.push([...userdata1]);

 }


function test(){
  alert(userdata[1][2])}

function table(){
 //if (userdata[1]===undefined||userdata[1]===null||userdata[1]===""|| typeof(userdata[1])===undefined){
 console.log("userdata[1]:", userdata[1]);
 if (!userdata[1]|| userdata[1]==""|| userdata[1]==[]){
   alert("missing required data")
   return;
 }
  var x = document.createElement("table")
  x.setAttribute("id","mytable");
  document.body.appendChild(x);

  var y = document.createElement("TR");
  y.setAttribute("id", "myTr");
  document.getElementById("mytable").appendChild(y);

  var z = document.createElement("TD");
  var p = document.createTextNode("1");
  z.appendChild(p)
  document.getElementById("myTr").appendChild(z);

  var z = document.createElement("TD");
  var t = document.createTextNode(userdata[0]);
  z.appendChild(t);
  document.getElementById("myTr").appendChild(z);


  
  var y = document.createElement("TR");
  y.setAttribute("id", "myTr2");
  document.getElementById("mytable").appendChild(y);

  var z = document.createElement("TD");
  var p = document.createTextNode("2");
  z.appendChild(p)
  document.getElementById("myTr2").appendChild(z);

  var k = document.createElement("TD");
  var r = document.createTextNode(userdata[1]);
  k.appendChild(r);
  document.getElementById("myTr2").appendChild(k);
}


function analysis() {
  if(userdata[1] == null||userdata[1]=="" ||userdata[1]==undefined|| typeof(userdata[1])==undefined){
    alert("missing requird data")
  }else{
   if (userdata[1][2]===false) {
      var result = "Pokémon might not be your thing, but you could still enjoy the games or anime!";
   }else {
    var age =userdata[1][1]
    if (age < 10) {
      result= "You might enjoy starting with Pikachu or Eevee!";
    } else if (age <= 15 && age > 10) {
      result="You could try training classic starters like Charmander, Squirtle, or Bulbasaur.";
    } else if (age <= 25) {
     result= "Consider competitive battling with Pokémon like Garchomp or Aegislash.";
    } else {
     result= "You might appreciate strategy-based Pokémon like Metagross or Tyranitar.";
    }
    document.getElementById("result").innerHTML = result
    document.getElementById("analysis_button").disabled = true;
  }
  }
}

