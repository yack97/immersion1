window.addEventListener("scroll", function () {
    var name = document.querySelector(".name");
    var section = document.querySelector("#formulario1");
    var offset = section.offsetTop - window.innerHeight;
  
    if (window.pageYOffset > offset) {
      name.classList.add("active");
    } else {
      name.classList.remove("active");
    }
  });
  