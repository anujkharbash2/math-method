document.getElementById("equationForm").onsubmit = async function(e) {
    e.preventDefault();
    let a = document.getElementById("a").value;
    let b = document.getElementById("b").value;

    let response = await fetch('/solve', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ a: a, b: b })
    });

    let data = await response.json();
    let resultDiv = document.getElementById("result");
    resultDiv.innerHTML = ""; // Clear previous result

    data.steps.forEach(step => {
        let p = document.createElement("p");
        p.innerText = step;
        resultDiv.appendChild(p);
    });
}
