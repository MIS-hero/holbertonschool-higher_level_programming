document.addEventListener("DOMContentLoaded", function () {
  const list = document.querySelector("ul.my_list");
  const addBtn = document.querySelector("#add_item");
  const removeBtn = document.querySelector("#remove_item");
  const clearBtn = document.querySelector("#clear_list");

  addBtn.addEventListener("click", function () {
    const li = document.createElement("li");
    li.textContent = "Item";
    list.appendChild(li);
  });

  removeBtn.addEventListener("click", function () {
    if (list.lastElementChild) {
      list.removeChild(list.lastElementChild);
    }
  });

  clearBtn.addEventListener("click", function () {
    list.innerHTML = "";
  });
});