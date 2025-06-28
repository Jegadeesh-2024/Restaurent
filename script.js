document.getElementById("reservationForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const data = {
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      reservation_datetime: document.getElementById("date").value,
      people: document.getElementById("people").value
    };

    fetch("http://127.0.0.1:5000/reserve", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
      alert(result.message);
    })
    .catch(err => console.error("Error:", err));
  });
  form.reset()