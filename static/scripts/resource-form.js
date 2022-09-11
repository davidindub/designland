console.log("Hello");

const formTagButtons = document.getElementsByClassName(".form-tag");
console.log(formTagButtons);
const tagsInput = document.querySelector("input[name='tags']");


for (let formTagButton of formTagButtons) {
    formTagButton.addEventListener("click", () => {
        console.log("clicked");
        valToAdd = formTagButton.innerHTML.replace("#", "");
        console.log(valToAdd);
        // tagsInput.value += formTagButton.innerHTML;

    })
}