let URL = "http://127.0.0.1:5000/student/1";

// Display the courses as a table
function displayStudentsCourses() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", URL+'/your-courses');
  xhttp.onload = function() {
    let data = JSON.parse(this.responseText);
    createScheduleTable(data)
  };
  xhttp.send();
}

function createScheduleTable(data) {
  let table = '<table id="schedule" border="1">';
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

// Registration table
function displayRegistration() {
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET",URL+"/add-courses");
  xhttp.onload = function() {
    let data = JSON.parse(this.responseText);
    createRegistrationTable(data)
  };
  xhttp.send();
}

function addClass(course_name) {
  var xhttp = new XMLHttpRequest();
  print(course_name)
  xhttp.open("POST", URL+'/add-courses/'+course_name);
  xhttp.setRequestHeader("Content-Type", "application/json");
  const body = {"course_name": course_name};
  xhttp.onload = function() {
    let data = JSON.parse(this.responseText);
    createRegistrationTable(data)
  };
  xhttp.send(JSON.stringify(body));
}

<<<<<<< HEAD
function removeClass(course_name) {
  var xhttp = new XMLHttpRequest();
  xhttp.open("DELETE", URL+'/add-courses/'+course_name);
=======
function removeClass(course_name, url) {
  var xhttp = new XMLHttpRequest();
  xhttp.open("DELETE", BASE+url+'/add-courses/'+course_name);
>>>>>>> f648643a83b08a593919b453799c1ed98f202d6a
  xhttp.setRequestHeader("Content-Type", "application/json");
  const body = {"course_name": course_name};
  xhttp.onload = function() {
    let data = JSON.parse(this.responseText);
    createRegistrationTable(data)
  };
  xhttp.send(JSON.stringify(body));
}

function createRegistrationTable(data) {
<<<<<<< HEAD
  let table = '<table id="schedule" border="1">';
=======
  let table = '<table id="schedule">';
>>>>>>> f648643a83b08a593919b453799c1ed98f202d6a
    table += `<tr><th>Course Name</th><th>Professor</th><th>Time</th><th>Enrollment</th><th>Add/Remove Class</th></tr>`;
    data.forEach((data, index) => {
      table = table + `<tr>`;
      table = table + `<td>${data.course}</td>`;
      table = table + `<td>${data.prof}</td>`;
      table = table + `<td>${data.time}</td>`;
      table = table + `<td>${data.enrollment}</td>`;
      let course_name = data.course.replace(" ", "%20");
      if (data.enrolled) {
        table = table + `<td><button onclick="removeClass('${course_name}')">-</button></td>`;
      } else {
        table = table + `<td><button onclick="addClass('${course_name}')">+</button></td>`;
      }
      table += `</tr>`;
    });
    table += "</table>";
    document.getElementById("courselist").innerHTML = table;
}

function getId(element) {
  alert("row" + element.parentNode.parentNode.rowIndex + 
  " - column" + element.parentNode.cellIndex);
}