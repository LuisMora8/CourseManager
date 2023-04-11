// Display the courses as a table
function displayStudentsCourses(data) {
  let table = '<table border="1">';
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
    console.log("displayCourses");
}

// Registration table
function displayCoursesToAdd(data) {
  console.log(data);
  let table = '<table border="1">';
  table += `<tr><th>Course Name</th><th>Professor</th><th>Time</th><th>Enrollment</th><th>Add Class</th></tr>`;
  data.forEach((data, index) => {
      table = table + `<tr>`;
      table = table + `<td>${data.course}</td>`;
      table = table + `<td>${data.prof}</td>`;
      table = table + `<td>${data.time}</td>`;
      table = table + `<td>${data.enrollment}</td>`;
      
      table = table + `<td><button>+</button></td>`;
      table += `</tr>`;
    });
    table += "</table>";
    document.getElementById("courselist").innerHTML = table;
    console.log("displayCourses");
}