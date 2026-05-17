const API_URL = "http://127.0.0.1:8000/tasks";

// Load tasks when page opens
window.onload = fetchTasks;

// Fetch all tasks
async function fetchTasks() {

    const response = await fetch(API_URL);
    const tasks = await response.json();

    const taskList = document.getElementById("task-list");

    taskList.innerHTML = "";

    tasks.forEach(task => {

        const taskDiv = document.createElement("div");

        taskDiv.className = "task";

        taskDiv.innerHTML = `
            <h3>${task.title}</h3>
            <p>${task.description}</p>
            <p>Status: ${task.completed ? "Completed" : "Pending"}</p>

            <button onclick="toggleStatus(
                ${task.id},
                '${task.title}',
                '${task.description}',
                ${task.completed}
            )">
                ${task.completed ? "Mark Pending" : "Mark Complete"}
            </button>

            <button onclick="editTask(${task.id}, '${task.title}', '${task.description}', ${task.completed})">
                Edit
            </button>

            <button onclick="deleteTask(${task.id})">
                Delete
            </button>
        `;

        taskList.appendChild(taskDiv);
    });
}

// Add new task
async function addTask() {

    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    // Prevent empty title
    if (!title.trim()) {
        alert("Task title cannot be empty");
        return;
    }

    const taskData = {
        title: title,
        description: description,
        completed: false
    };

    await fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(taskData)
    });

    // Clear input fields
    document.getElementById("title").value = "";
    document.getElementById("description").value = "";

    fetchTasks();
}

// Delete task
async function deleteTask(taskId) {

    await fetch(`${API_URL}/${taskId}`, {
        method: "DELETE"
    });

    fetchTasks();
}

// Edit task
async function editTask(taskId, oldTitle, oldDescription, completed) {

    const newTitle = prompt("Enter new title:", oldTitle);

    if (newTitle === null || !newTitle.trim()) {
        return;
    }

    const newDescription = prompt(
        "Enter new description:",
        oldDescription
    );

    const updatedTask = {
        title: newTitle,
        description: newDescription || "",
        completed: completed
    };

    await fetch(`${API_URL}/${taskId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(updatedTask)
    });

    fetchTasks();
}

// Toggle task status
async function toggleStatus(taskId, title, description, completed) {

    const updatedTask = {
        title: title,
        description: description,
        completed: !completed
    };

    await fetch(`${API_URL}/${taskId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(updatedTask)
    });

    fetchTasks();
}