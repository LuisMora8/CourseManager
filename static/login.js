let BASE = "http://127.0.0.1:5000";
// var email = document.forms['form']['email'];
// var password = document.forms['form']['password'];

// var email_error = document.getElementById('email_error');
// var password_error = document.getElementById('pass_error');

// email.addEventListener('textInput', email_authentication);
// password.addEventListener('textInput', password_authentication);

// function authentication(){
// 	if (email.value.length < 9) {
// 		email.style.border = "1px solid red";
// 		email_error.style.display = "block";
// 		email.focus();
// 		return false;
// 	}
// 	if (password.value.length < 6) {
// 		password.style.border = "1px solid red";
// 		password_error.style.display = "block";
// 		password.focus();
// 		return false;
// 	}

// }
// function email_authentication(){
// 	if (email.value.length >= 8) {
// 		email.style.border = "1px solid silver";
// 		email_error.style.display = "none";
// 		return true;
// 	}
// }
// function password_authentication(){
// 	if (password.value.length >= 5) {
// 		password.style.border = "1px solid silver";
// 		password_error.style.display = "none";
// 		return true;
// 	}
// }
function auth_login() {
	username=document.getElementById("email").value
	if(username=='admin'){
		document.loggedin.action = BASE+'/admin/'
		 document.loggedin.submit();
	}
	var xhttp = new XMLHttpRequest();
	console.log(BASE+'/'+username)
  xhttp.open("GET", BASE+'/'+username);
  xhttp.onload = function() {
     let data = this.responseText;
		 console.log(data);
		 document.loggedin.action = data
		 document.loggedin.submit();
  };
  xhttp.send();
}

//Student

// Display the courses as a table
function displayStudentsCourses(url) {
  var xhttp = new XMLHttpRequest();
	console.log(url);
  xhttp.open(url);
	xhttp.onload = function() {
    // let data = this.responseText;
		// displayStudentsCourses(data)
  };
   xhttp.send();
}

function createScheduleTable(data) {
  let table = '<table id="schedule">';
  table += `<tr><th>Course Name</th><th>Professor</th><th>Time</th><th>Enrollment</th></tr>`;
  data.forEach((data, index) => {
      table = table + `<tr>`;
      table = table + `<td>${data.course}</td>`;
      table = table + `<td>${data.prof}</td>`;
      table = table + `<td>${data.time}</td>`;
      table = table + `<td>${data.enrollment}</td>`;
      table += `</tr>`;
    });
    table += "</table>";
    document.getElementById("courselist").innerHTML = table;
}