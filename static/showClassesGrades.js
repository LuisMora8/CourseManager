function displayClassGrades(data) {
    
    console.log(data);
    let table = '<table border="1">';
    table += `<tr><th>Student Name</th><th>Grades</th>`;
    data.forEach((data, index) => {
        table = table + `<tr>`;
        table = table + `<td>${data.studentName}</td>`;
        table = table + `<td>${data.grades}</td>`;
        table += `</tr>`;
      });
      table += "</table>";
      document.getElementById("studentGradeslist").innerHTML = table;
      console.log("displayStudentGrades");
  }
  function openClass(id){
    alert(id)
    console.log(id)
  }