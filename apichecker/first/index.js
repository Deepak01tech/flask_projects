let main = document.getElementById("main");
let api = "http://127.0.0.1:5000/users"; // Change this to your actual API URL

let actual_data;

// Get form element
const form = document.getElementById("userForm");
const userList = document.getElementById("userList");

// Fetch and display existing data
async function getData() {
  let res = await fetch(api);
  let data = await res.json();
  actual_data = data;
  display(data);
}

// Submit form and add new user
form.addEventListener("submit", async (event) => {
  event.preventDefault(); // Prevent form from refreshing the page

  const formData = new FormData(form);
  const name = formData.get("name");
  const email = formData.get("email");

  // Send data to the backend
  let res = await fetch(api, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name, email }),
  });

  if (res.ok) {
    // Refresh data after adding the user
    getData();
    // Clear the form
    form.reset();
  } else {
    console.error("Error adding user");
  }
});

// Function to delete a user (without try-catch)
async function deleteUser(userId) {
  let res = await fetch(`${api}/${userId}`, {
    method: "DELETE",
  });

  if (res.ok) {
    // Re-fetch and display the updated user list
    getData();
  } else {
    console.error("Failed to delete the user");
  }
}

// Display data with a delete button
function display(data) {
  userList.innerHTML = ""; // Clear existing content

  data.forEach((user) => {
    let div = document.createElement("div");
    div.innerHTML = `
            <h2>${user.name}</h2>
            <p>${user.email}</p>
        `;

    // Create the Delete button
    let deleteButton = document.createElement("button");
    deleteButton.innerText = "Delete";
    deleteButton.addEventListener("click", () => {
      deleteUser(user.id); // Call deleteUser function with user ID
    });

    // Append the delete button and user info to the list
    div.appendChild(deleteButton);
    userList.appendChild(div);
  });
}

// Initial fetch of data
getData();
