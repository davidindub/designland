//  For message notifications
const toastLiveMessages = document.getElementsByClassName("message-toast");

console.log(toastLiveMessages);

for (let toastElement of toastLiveMessages) {
    console.log(toastElement);
    const toast = new bootstrap.Toast(toastElement);
    toast.show();
}

// On list page - sets the sort drop down to match the url param
const searchParams = new URLSearchParams(window.location.search);
const sortOrder = searchParams.get("sort");
const options = document.querySelector(".sort-select").children;

for (let option of options) {
    if (option.value == sortOrder) {
        console.log(option.value);
        option.setAttribute('selected', true)
    }
}