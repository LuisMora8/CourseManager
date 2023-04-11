// Display the courses as a table
function displayProfessors(data) {
    console.log(data);
    let table = '<table border="1">';
    table += `<tr><th>Course Name</th><th>Professor</th><th>Time</th><th>Enrollment</th></tr>`;
    data.forEach((data, index) => {
        table = table + `<tr>`;
        table = table + `<td>${data.id}</td>`;
        table = table + `<td>${data.profName}</td>`;
        table = table + `<td>${data.time}</td>`;
        table = table + `<td>${data.enrolled}</td>`;
        table += `</tr>`;
      });
      table += "</table>";
      document.getElementById("Proflist").innerHTML = table;
      console.log("displayProfessors");
  }