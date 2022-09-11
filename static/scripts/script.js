/* jshint esversion: 11 */

//  For message notifications
const toastLiveMessages = document.getElementsByClassName("message-toast");

for (let toastElement of toastLiveMessages) {
    const toast = new bootstrap.Toast(toastElement);
    toast.show();
}