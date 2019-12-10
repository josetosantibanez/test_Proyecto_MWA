const PARSER = document.createElement("div");
const listBody = elem(".list-body");
const itemInput = elem(".item-input");

function elem(selector) {
  return document.querySelector(selector);
}

function newItem(value) {
  PARSER.innerHTML = `<div class="list-item">
            <input class="status" type="checkbox" title="Mark as complete"/>
            <span class="item">${value}</span>
            <span class="remove-item" title="Remove Item"></span>
        </div>`;

  return PARSER.firstChild;
}

function addItem() {
  if (itemInput.value) listBody.appendChild(newItem(itemInput.value));

  itemInput.value = "";
}

listBody.addEventListener("click", e => {
  let target = e.target;

  if (target.classList.contains("remove-item")) target.parentNode.remove();
});

itemInput.addEventListener("keydown", e => {
  if (e.which == 13) addItem();
});

elem(".add-item").addEventListener("click", e => {
  addItem();
});
