document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("greetButton");
    if (button) {
        button.addEventListener("click", function () {
            window.location.href = "/training/";
        });
    } else {
        console.error("Button with ID 'greetButton' not found.");
    }
});