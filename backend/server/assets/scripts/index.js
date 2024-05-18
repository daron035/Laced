import Alpine from "alpinejs";

// Add Alpine object to the window scope
window.Alpine = Alpine;

// initialize Alpine
Alpine.start();

// import HTMX and inject it into the window scope
window.htmx = require("htmx.org");

// window.addEventListener("load", () => {
//   document.getElementById("message").textContent = "FROM JAVASCRIPT!";
// });

// window.addEventListener("load", () => {
//   const myImg = new Image();
//   myImg.src = TestImage;
//   myImg.style.width = "200px";
//   myImg.style.height = "200px";
//
//   document.body.appendChild(myImg);
// });
