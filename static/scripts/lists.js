// On list page - sets the sort drop down to match the url param
const searchParams = new URLSearchParams(window.location.search);
const sortOrder = searchParams.get("sort");
const options = document.querySelector(".sort-select").children;

for (let option of options) {
    if (option.value == sortOrder) {
        option.setAttribute('selected', true);
    }
}