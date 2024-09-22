let main = document.getElementById("main");
let api = "http://127.0.0.1:5000/users";

let actual_data;


const form = document.getElementById("userForm");
const userList = document.getElementById("userList");


async function getData() {
  let res = await fetch(api);
  let data = await res.json();
  actual_data = data;
  display(data);
}


form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const name = formData.get("name");
  const email = formData.get("email");


  let res = await fetch(api, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name, email }),
  });

  if (res.ok) {

    getData();

    form.reset();
  } else {
    console.error("Error adding user");
  }
});


async function deleteUser(userId) {
  let res = await fetch(`${api}/${userId}`, {
    method: "DELETE",
  });

  if (res.ok) {

    getData();
  } else {
    console.error("Failed to delete the user");
  }
}


function display(data) {
  userList.innerHTML = "";

  data.forEach((user) => {
    let div = document.createElement("div");
    div.innerHTML = `
            <h2>${user.name}</h2>
            <p>${user.email}</p>
        `;


    let deleteButton = document.createElement("button");
    deleteButton.innerText = "Delete";
    deleteButton.addEventListener("click", () => {
      deleteUser(user.id);
    });


    div.appendChild(deleteButton);
    userList.appendChild(div);
  });
}


getData();
