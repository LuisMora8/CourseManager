// Display the courses as a table
let x =1
// table = table + `<td>
        // <a href={{ url_for('/classGrade', name=${data.id}) }}">${data.id}</a>
        // </td>`;
function displayProfessors(data) {
    console.log(x)
    x= x+1
    console.log(data);
    let table = '<table border="1">';
    table += `<tr><th>Course Name</th><th>Professor</th><th>Time</th><th>Enrollment</th></tr>`;
    data.forEach((data, index) => {
        table = table + `<tr>`;
        table = table + `<td><a href="/classGrades/${data.id}">${data.className}</a></td>`;
        table = table + `<td>${data.profName}</td>`;
        table = table + `<td>${data.time}</td>`;
        table = table + `<td>${data.enrolled}</td>`;
        table += `</tr>`;
      });
      table += "</table>";
      document.getElementById("Proflist").innerHTML = table;
      console.log("displayProfessors");
  }


  // function showClass(id){
  //   var xhttp = new XMLHttpRequest();
  //   xhttp.open("GET","http://127.0.0.1:5000/classGrades")
  //   xhttp.onload = function(){
  //       console.log("testing show classes")
  //       window.alert("hello")
  //   };
  //   xhttp.send();
  // }


  // function displayClassGrades(data) {
  //   console.log(x)
  //   x= x+1
  //   console.log(data);
  //   let table = '<table border="1">';
  //   table += `<tr><th>Course Name</th><th>Professor</th><th>Time</th><th>Enrollment</th></tr>`;
  //   data.forEach((data, index) => {
  //       table = table + `<tr>`;
  //       table = table + `<td>${data.profName}</td>`;
  //       table = table + `<td>${data.time}</td>`;
  //       table = table + `<td>${data.enrolled}</td>`;
  //       table += `</tr>`;
  //     });
  //     table += "</table>";
  //     document.getElementById("Proflist").innerHTML = table;
  //     console.log("displayProfessors");
  // }
  // function openClass(id){
  //   alert(id)
  //   console.log(id)
  // }
