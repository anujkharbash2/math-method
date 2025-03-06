document.getElementById("echelonForm").onsubmit = async function(e) {
    e.preventDefault();
    let matrix = document.getElementById("matrix").value;

    let rows = matrix.trim().split("\n").map(row => row.trim().split(" ").map(Number));

    let response = await fetch('/echelon', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ matrix: rows })
    });

    let data = await response.json();
    let resultDiv = document.getElementById("echelonResult");
    resultDiv.innerHTML = ""; 

    if (data.steps) {
        data.steps.forEach(step => {
            let p = document.createElement("p");
            p.innerText = step;
            resultDiv.appendChild(p);
        });

        resultDiv.innerHTML += "<h3>Final Row Echelon Form:</h3>";
        data.result.forEach(row => {
            resultDiv.innerHTML += `[${row.join(", ")}]<br>`;
        });
    } else {
        resultDiv.innerHTML = "Invalid Input!";
    }
}
