function displayClassGrades(data) {
    let x = 1;
    console.log(data);
    let table = '<table border="1">';
    table += `<tr><th>Student Name</th><th>Grades</th>`;
    data.forEach((data, index) => {
        table = table + `<tr>`;
        table = table + `<td>${data.studentName}</td>`;
        table = table + `<td>
        <input type = 'text'  id = 'textEdit${x}' value = '${data.grades}'>
        </td>`;
        table = table + `<td><button onclick="edit('${data.studentName}','${x}')">edit</button></td>`;
        table += `</tr>`;
        x=x+1;
      });
      table += "</table>";
      document.getElementById("studentGradeslist").innerHTML = table;
      console.log("displayStudentGrades");
  }
//   function openClass(id){
//     alert(id)
//     console.log(id)
//   }
function edit(name,id){
    console.log(name);
    console.log(id)
    console.log(document.getElementById("textEdit"+id).value)
    let grade = document.getElementById("textEdit"+id).value
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET","http://127.0.0.1:5000/"+name+"/"+grade);
    xhttp.send();
    // console.log(id)
}
function submitFunction(data){
    // var xhttp = new XMLHttpRequest();
    // data.forEach((data,index)=>{
    //     var test = document.getElementById('textEdit').value;
    //     console.log(test)
    // })
    var test = document.getElementById('textEdit1').value;

    console.log(test);

}