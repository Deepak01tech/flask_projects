let API_URL = "http://localhost:5000";

document.addEventListener("DOMContentLoaded", function () {
    const loginButton = document.querySelector(".signup-btn");

    loginButton.addEventListener("click", async function (event) {
        event.preventDefault(); // Prevent form submission

        // Get email and password values
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        // Fetch data from API
        const response = await fetch(`${API_URL}/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password }),
        });

        const data = await response.json();
        if (response.ok) {
            localStorage.setItem("token", data.token);
            window.location.href = "blogitempage.html";
        } else {
            alert("wrong credential");
        }
    });

});


document.addEventListener("DOMContentLoaded", function () {
    const signupButton = document.querySelector(".signup-btn");

    signupButton.addEventListener("click", async function (event) {
        event.preventDefault(); // Prevent form submission

        // Get input values
        const username = document.getElementById("username").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        const response = await fetch(`${API_URL}/signup`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password }),
        });

        if (response.ok) {
            alert("Signup successful! Redirecting to login...");
            window.location.href = "login.html";
        } else {
            const data = await response.json();
            alert("field the correct details");
        }
    });
});

