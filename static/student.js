// Dummy data to create table from function
var data = [
  {
    "course": "Physics 121",
    "prof": "Susan Walker",
    "time": "TR",
    "enrollment": "5/10"
  },
  {
    "course": "CS 106",
    "prof": "Ammon Hepworth",
    "time": "W",
    "enrollment": "6/10"
  }
];

// Display the courses as a table
function displayCourses() {
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