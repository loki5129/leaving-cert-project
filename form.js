initialize_database()
main_user_update()
function main_user_update(){
 let users=JSON.parse(localStorage.getItem("userdata"))
 let main_user_name = "loki5129"
 let main_user_age = 18
 let main_user_state =true
 let  main_user_check = users.some(user => user.name === main_user_name)
 if (main_user_check){
 
 } else{
  add_data(main_user_name,main_user_age,main_user_state)
 }
}



function local_test() {
 
  localStorage.setItem("data",[["name","23","true"]]);
  let test2 = localStorage.getItem("data")
  console.log(test2)
 }

function initialize_database(){
  if (!localStorage.getItem("userdata")){
    localStorage.setItem("userdata",JSON.stringify([]));
  }
}

function add_data(name,age,state){
  let users = JSON.parse(localStorage.getItem("userdata"))
  let new_user ={
    name: name,
    age: age,
    state: state
  };
  let username_exist=users.some(user => user.name === name);
  if (username_exist){
    alert("username invaild");
  } else{
  users.push(new_user);
  localStorage.setItem("userdata",JSON.stringify(users))
}
}
function clear_database(){
  localStorage.clear()
  initialize_database()
  main_user_update()
  clear_table()
}
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
  state = userdata1[2]
  add_data(username,age,state)

 }
function full_record(){
  let users=JSON.parse(localStorage.getItem("userdata"))
  console.log(users)
}

function test(){
  //alert(userdata[1][2])}
  console.log(typeof(JSON.parse(localStorage.getItem("userdata"))))
}
function table(){
  let users=JSON.parse(localStorage.getItem("userdata"));
  
  if (!users||users.length === 0){
    alert("no users found");
    return;
   } 
  table = document.getElementById("table")
  if (!table){
    var table = document.createElement("table");
    table.setAttribute("id", "table");


    let header_row = document.createElement("tr");
    let headers =["user id","username","age","state"]
    
    headers.forEach(header => {
      let th = document.createElement("TH");
      let header_text = document.createTextNode(header);
      th.appendChild(header_text);
      header_row.appendChild(th);
    });

    table.appendChild(header_row);
    document.body.appendChild(table);
    
  }

  
   let row_count =  table.getElementsByTagName("tr").length - 1;
  
 
  for (let i =row_count;i< users.length; i++){
   let user = users[i];
   if (!user){
    alert("missing required data for user " +i);
    continue;
    } 
    let row_there = document.getElementById("tr" + i);
    if (row_there){
      continue;
    }
    let row =document.createElement("Tr");
    row.id = "mytr"+ i;
    
    let cell = document.createElement("TD");
    let text = document.createTextNode(i + 1);
    cell.appendChild(text);
    row.appendChild(cell);
    let data = [user.name,user.age,user.state];
    data.forEach(element =>{
      let cell = document.createElement("TD")
      let text = document.createTextNode(element);
      cell.appendChild(text),
      row.appendChild(cell)
    });
   table.appendChild(row)
  }
}
function clear_table(){
 const table = document.getElementById("table");
 table.remove();
}


function analysis() {
  /*if(userdata[1] == null||userdata[1]=="" ||userdata[1]==undefined|| typeof(userdata[1])==undefined){
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
  }*/
}

