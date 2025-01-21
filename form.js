

const userdata1 = [];
function submitData() {
 username = document.getElementById('username');
 if (typeof(username) == 'undefined' || username == null || username.value == '') {
   alert("Please enter a username");}
  else {
    userdata1.push(username.value);}

  //console.log(username.value);
 
 age = document.getElementById('age');
 if (age.value>0 && age.value<111){
  userdata1.push(age.value);
 }
 else{
   alert("Please enter a valid age");
 }
const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
if (checkboxes.length === 0) {
  alert("Please select at least one checkbox");
} else if (checkboxes.length > 1) {
  alert("Please select only one checkbox");
} else {
  userdata1.push(checkboxes[0].value);
}
 
}





function readFile(file, user_data) {
  const reader = new FileReader();
  reader.onload = function(event) {
    
    const csv = event.target.result;
    
    const updated_csv = `${csv}\n${user_data.join(",")}`;

    const blob = new Blob([updated_csv], {type: "text/csv"});
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'user_data.csv';
    link.click();

  };
  reader.onerror = function(event) {
    console.error("error reading file");
  };
  reader.readAsText(file);
}

document.addEventListener('DOMContentLoaded', function() {
  const fileinput = document.getElementById('file');
  if (fileinput) {
    fileinput.addEventListener('change', function(event) {
      const file = event.target.files[0];
      if (file) {
        readFile(file, userdata1);
      } else {
        console.error("file not found");
      }
    });
  } else {
    console.error("file input element not found");
  }
});
