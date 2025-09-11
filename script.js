const input = document.getElementById("input-task");
const btn = document.querySelector(".btn");
const taskList = document.getElementById("task-list");

// إضافة مهمة جديدة
btn.addEventListener("click", addTask);
input.addEventListener("keypress", function (e) {
  if (e.key === "Enter") addTask();
});

function addTask() {
  const taskText = input.value.trim();
  if (taskText === "") {
    alert("Please enter a task!");
    return;
  }

  const li = document.createElement("li");
  li.textContent = taskText;

  // زر الحذف
  const span = document.createElement("span");
  span.innerHTML = "&times;";
  li.appendChild(span);

  taskList.appendChild(li);
  input.value = "";

  // عند الضغط على المهمة → تنشطب
  li.addEventListener("click", () => {
    li.classList.toggle("completed");
  });

  // عند الضغط على X → تحذف المهمة
  span.addEventListener("click", (e) => {
    e.stopPropagation(); // يمنع تنفيذ كليك على li
    li.remove();
  });
}