const navitationMenu = document.querySelectorAll("nav")[0];
const userProfile = document.getElementById("userProfile");
const btMenu = document.getElementById("btMenu");

function hideMenu() {
  if (navitationMenu.style.display == "none") {
    navitationMenu.style.display = "inline-block";
    userProfile.style.backgroundColor = "var(--color2)";
    userProfile.style.borderRight = "2px solid black";
    
  } else {
    navitationMenu.style.display = "none";
    userProfile.style.backgroundColor = "white";
    userProfile.style.border = "none";
  }
}

btMenu.addEventListener("click", hideMenu);