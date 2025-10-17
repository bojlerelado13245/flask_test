function submitForm() {
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  if (!username || !email) {
    document.getElementById("output").textContent =
      "Error: Both username and email are required.";
    return;
  }
  fetch("http://127.0.0.1:5000/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, email }),
  })
    .then((res) => res.json())
    .then((data) => {
      document.getElementById(
        "output"
      ).textContent = `Server response: ${data.message}, Username: ${data.username}, Email: ${data.email}`;
      getSql(); // Refresh the table
    })
    .catch((err) => {
      document.getElementById("output").textContent = `Error: ${err.message}`;
    });
}

function getSql() {
  fetch("http://127.0.0.1:5000/get_sql", {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  })
    .then((res) => res.json())
    .then((data) => {
      let sqlDiv = document.getElementById("sql");

      // Create table dynamically
      let tableHTML = `
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Username</th>
              <th>Email</th>
            </tr>
          </thead>
          <tbody>
            ${data
              .map(
                (item) => `
              <tr>
                <td>${item.id}</td>
                <td>${item.username}</td>
                <td>${item.email}</td>
              </tr>`
              )
              .join("")}
          </tbody>
        </table>
      `;

      sqlDiv.innerHTML = tableHTML;
    })
    .catch((err) => {
      document.getElementById("sql").textContent = `Error: ${err.message}`;
    });
}

// Optional: load table on page load
window.addEventListener("DOMContentLoaded", getSql);
