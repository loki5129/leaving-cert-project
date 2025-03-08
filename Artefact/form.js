//calls functions on startup to ensure the database is made and add the main user
initialize_database()
main_user_update()


function main_user_update(){
 let users=JSON.parse(localStorage.getItem("userdata"))//gets the database and makes it editable
 //defines the main users data
 let main_user_name = "loki5129" 
 let main_user_age = 18
 let main_user_state =true
 //checks if the main user is areadly in the database
 let  main_user_check = users.some(user => user.name === main_user_name)
 if (main_user_check){//if main is in the database 
 //pass
 } else{//if it is not
  add_data(main_user_name,main_user_age,main_user_state)//call the add_data function to add main user to the database
 }
}





function initialize_database(){//function to create the database if does not exist 
  if (!localStorage.getItem("userdata")){//is the database vaild
    localStorage.setItem("userdata",JSON.stringify([]));//if not create database
  }
}



function add_data(name,age,state){//fucntion to add the user's data to the database
  let users = JSON.parse(localStorage.getItem("userdata"))//get the database and makes it editable
  let new_user ={//combines the user data in required formant
    name: name,
    age: age,
    state: state
  };
  let username_exist=users.some(user => user.name === name);//checks if username is already in the database
  if (username_exist){
    alert("username invaild");//if the username is already in and alert that the useranme is invaild
  } else{//if it is  not add it to the database
  users.push(new_user);
  localStorage.setItem("userdata",JSON.stringify(users))
}
}



function clear_database(){//fucntion to clear the database and remove the table 
  localStorage.clear()//clear loclstorage removing all the data in the database
  initialize_database()//create the empty database
  main_user_update()//add the main user's data back into the datbase
  clear_table()//remove and empty the table
}



function submitData() {//funtion to submit and validate the user's data
 let userdata1 = []//empty list to store the user's data
 //takes in the values inside the form and turns age into a numebr
 let username = document.getElementById('username').value; 
 let age = Number(document.getElementById('age').value);
 //console.log(age) //test for age
 if (!username) {//checks if they entered a usersname and alerts if not
   alert("Please enter a username");
   return;
 }else {
    userdata1.push(username);//if username is entered add it to the userdata
  }
 if (!age || age<0 ||age>111){//ensures the age is in a vailed range and alerts if not
   alert("enter vaild age")
   return;

 }else{
  userdata1.push(Number(age));//if it is  inside add it to the user data
  
 }

 const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');//gets the checkboxs for the form
 if (checkboxes.length === 0) {//if more than one checkbox is check and alerts
   alert("Please select at least one checkbox");
   return
 }else if (checkboxes.length > 1) {//if no checkbox is checked alert
  alert("Please select only one checkbox");
  return
 }else {
  userdata1.push(checkboxes[0].value === "True" ? true : false);//if the true value of box is check the value is true if not its faslse
  }
  state = userdata1[2]//adds the state to the users data
  add_data(username,age,state)//add the users data to the database

 }



 function local_test() {//this function is made to test the local stroage and how it stores data
 
  localStorage.setItem("data",[["name","23","true"]]);//test values in a test database
  let test2 = localStorage.getItem("data")//get test data
  console.log(test2)//show in console to test how database is storing the data
 }




function full_record(){//funciton to test the full database
  let users=JSON.parse(localStorage.getItem("userdata"))//gets the database
  console.log(users)//shows it in the console
}




function table(){//fucntion to create a table to display the all users data
  let users=JSON.parse(localStorage.getItem("userdata"));//take in the database
  
  if (!users||users.length === 0){//if the database is emptpy
    alert("no users found");
    return;//alert and end
   } 
   // checks if there is a table already being show
  table = document.getElementById("table")
  if (!table){//if the table is not already show
    var table = document.createElement("table");//get the table
    table.setAttribute("id", "table"); //set attribute for the table

    //create a header row 
    let header_row = document.createElement("tr");
    let headers =["user id","username","age","state"]//define header names
    
    headers.forEach(header => {//loop through each index of header names and create text in the header for each
      let th = document.createElement("TH");
      let header_text = document.createTextNode(header);
      th.appendChild(header_text);
      header_row.appendChild(th);
    });
//add the header row to the table and write it to the website
    table.appendChild(header_row);
    document.body.appendChild(table);
    
  }

  //count how row in the table exucling the header
   let row_count =  table.getElementsByTagName("tr").length - 1;
  
 
  for (let i =row_count;i< users.length; i++){//for the differnce between the length of the table and the amount of users iterate through loop
   let user = users[i];//get the is the user with the user id of the 
   if (!user){//check if the user is vaild and alerts the id if not
    alert("missing required data for user " +i);
    continue;//skips this iteration
    } 
    let row_there = document.getElementById("tr" + i);//check if there is a row with this id
    if (row_there){//if there is a row with teh id skipp the iteraion
      continue;
    }
    //create the row and give it an unqine id 
    let row =document.createElement("Tr");
    row.id = "mytr"+ i;

    //create a cell and text node for the row and add it to the row
    let cell = document.createElement("TD");
    let text = document.createTextNode(i + 1);
    cell.appendChild(text);
    row.appendChild(cell);

    let data = [user.name,user.age,user.state];//gets the user's data
    data.forEach(element =>{//for each index create a cell with a text node holding the data
      let cell = document.createElement("TD")
      let text = document.createTextNode(element);
      cell.appendChild(text),
      row.appendChild(cell)//add cell with text to the row
    });
   table.appendChild(row)//add row to table
  }
}



function clear_table(){//functioin to remove the table for the website 
 const table = document.getElementById("table"); //gets all elements that use table
 table.remove(); //uses remove to remove the table from the website
}


