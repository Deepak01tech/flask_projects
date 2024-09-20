// Select elements
const input = document.getElementById("todo-input");
const addBtn = document.getElementById("add-btn");
const todoList = document.getElementById("todo-list");

// Function to add a new task
function addTodo() {
  const todoText = input.value.trim();
  if (todoText === "") return; // Prevent empty tasks

  const li = document.createElement("li");
  li.innerHTML = `<span>${todoText}</span><button class="delete-btn">Delete</button>`;

  todoList.appendChild(li);
  input.value = ""; // Clear input field

  // Delete task when button is clicked
  const deleteBtn = li.querySelector(".delete-btn");
  deleteBtn.addEventListener("click", () => {
    todoList.removeChild(li);
  });
}

// Add task on button click
addBtn.addEventListener("click", addTodo);

// Add task on Enter key press
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    addTodo();
  }
});
