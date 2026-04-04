const addButton = document.querySelector("#add_item");
const myList = document.querySelector("ul.my_list");
addButton.addEventListener("click", function () {
    const newLi = document.createElement("li");
    newLi.textContent = "Item";
    myList.appendChild(newLi);
});