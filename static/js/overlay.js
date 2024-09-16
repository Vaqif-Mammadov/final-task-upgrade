let testedusers = [];

document.addEventListener("DOMContentLoaded", function () {
  const token = "bvmVNBMBMHB24512vbnmmm45vbgfhvn53VGBHJbjghj275fgcgvnf";
  fetch("/api/users/", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: token,
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      data.forEach((user) => {
        testedusers[user.id] = {
          email: user.email,
          phone: user.phone,
          username: user.username,
        };
      });
    })
    .catch((error) => console.error("Error", error));
});

//article option buttons

let articleoptions = document.getElementById("articleoptions");
if (articleoptions) {
  articleoptions.addEventListener("click", addClass);
}

function addClass(e) {
  for (i = 0; i <= 7; i++) {
    if (i % 2 !== 0) {
      articleoptions.childNodes[i].classList.remove("active");
    }
  }
  e.preventDefault();
  e.target.classList.add("active");
}

// eyes

eye = document.querySelectorAll(".eye");
eye1 = document.querySelectorAll(".eye1");
if (eye) {
  eye.forEach((eye) => {
    eye.addEventListener("mousedown", textviewer);
  });
  eye.forEach((eye) => {
    eye.addEventListener("mouseup", passwordviewer);
  });
}
if (eye1) {
  eye1.forEach((eye) => {
    eye.addEventListener("mousedown", textviewer);
  });
  eye1.forEach((eye) => {
    eye.addEventListener("mouseup", passwordviewer);
  });
}

//memberships

document.querySelectorAll(".plan").forEach((plan) => {
  plan.addEventListener("click", addAndRemoveClass);
});

function addAndRemoveClass(e) {
  document.querySelectorAll("#membershipplans .plan").forEach((plan) => {
    plan.classList.remove("plan2");
  });
  if (e.currentTarget.classList.contains("plan")) {
    e.currentTarget.classList.add("plan2");
    document.querySelectorAll(".plan2 ul li img").forEach((image) => {
      image.src = "/static/media/checkmark-circle-outline_green.svg";
    });
  }
  document.querySelectorAll("#homemembershipplans .plan").forEach((plan) => {
    plan.classList.remove("plan2");
    document.querySelectorAll(".plan ul li img").forEach((image) => {
      image.src = "static/media/checkmark-circle-outline%201.svg";
    });
  });
  if (e.currentTarget.classList.contains("plan")) {
    e.currentTarget.classList.add("plan2");
    document.querySelectorAll(".plan2 ul li img").forEach((image) => {
      image.src = "/static/media/checkmark-circle-outline_green.svg";
    });
  }
}

// Happy client's comments

let arrows = document.getElementById("arrows");
let arrowleft = document.getElementById("arrowleft");
let arrowright = document.getElementById("arrowright");
let happyClientsCount = 2;
let startcount = 1;

if (arrows) {
  arrowleft.addEventListener("click", less);
  arrowright.addEventListener("click", more);
  arrowleft = arrowleft.firstElementChild;
  arrowright = arrowright.lastElementChild;
}

function testarrow() {
  if (startcount === 1) {
    arrowleft.classList.remove("activearrow");
    arrowleft.classList.add("passivearrow");
    arrowright.classList.remove("passivearrow");
    arrowright.classList.add("activearrow");
  } else if (startcount > 1 && startcount < happyClientsCount) {
    arrowright.classList.remove("passivearrow");
    arrowright.classList.add("activearrow");
    arrowleft.classList.remove("passivearrow");
    arrowleft.classList.add("activearrow");
  } else if (startcount === happyClientsCount) {
    arrowleft.classList.remove("passivearrow");
    arrowleft.classList.add("activearrow");
    arrowright.classList.add("passivearrow");
    arrowright.classList.remove("activearrow");
  }
}
function pagecontrol() {
  if (startcount <= 3) {
    for (i = 3; i <= 7; i += 2) {
      arrows.childNodes[i].firstElementChild.classList.remove("rectangle");
      arrows.childNodes[i].firstElementChild.classList.add("ellipse");
    }
    arrows.childNodes[
      startcount + (startcount + 1)
    ].firstElementChild.classList.remove("ellipse");
    arrows.childNodes[
      startcount + (startcount + 1)
    ].firstElementChild.classList.add("rectangle");
  }
}

function less() {
  testarrow();
  if (startcount > 1) {
    startcount--;
    testarrow();
    pagecontrol();
  }
}

function more() {
  testarrow();
  if (startcount < happyClientsCount) {
    startcount++;
    testarrow();
    pagecontrol();
  }
}

// Login and Signup buttons overlays

let overlays = document.querySelectorAll(".overlay");
let closeoverlays = document.querySelectorAll(".close");
let signupbuttons = document.querySelectorAll(".signupButton");
let loginbuttons = document.querySelectorAll(".loginButton");
let signupOverlay = document.getElementById("signupOverlay");
let signinOverlay = document.getElementById("signinOverlay");
let confirmOverlay = document.getElementById("confirmOverlay");
let securityOverlay = document.getElementById("securityOverlay");
let securityContinue = document.getElementById("securityContinue");
let forgotoverlay = document.getElementById("forgotOverlay");
let forgotVerify = document.getElementById("forgotVerifyOverlay");
let newPasswordOverlay = document.getElementById("newPasswordOverlay");
let successOverlay = document.getElementById("successOverlay");
let poster = document.getElementById("poster");
let mailto = document.getElementById("mailto");
let confirmedemail = document.getElementById("confirmedemail");
let confirmedphone = document.getElementById("confirmedphone");
let passwordfield = document.getElementById("passwordlogin");
let usernamefield = document.getElementById("usernamelogin");
let buttoncontinue = document.getElementById("confirmContinue");
let forgotmailarea = document.getElementById("forgotmailarea");
let pass = document.querySelectorAll(".pass");
let globalemail;
let resendbutton = document.getElementById("resend");
let configElement = document.getElementById("config-data");
let configData = JSON.parse(configElement.textContent);
let isLoggedIn = configData.is_authenticated;

function buttonhider() {
  document.addEventListener("DOMContentLoaded", function () {

    if (!isLoggedIn) {
      document.getElementById("login").style.display = "flex";
      document.getElementById("signup").style.display = "flex";
    } else {
      document.getElementById("login").style.display = "none";
      document.getElementById("signup").style.display = "none";
    }
  });
}

buttonhider();

var path = window.location.pathname;
var page = path.split("/");

if (signupbuttons) {
  signupbuttons.forEach((signupbutton) => {
    signupbutton.addEventListener("click", signup);
  });
}
if (loginbuttons) {
  loginbuttons.forEach((loginbutton) => {
    loginbutton.addEventListener("click", login);
  });
}

if (securityContinue) {
  securityContinue.addEventListener("click", endofsignin);
}

if (resendbutton) {
  resendbutton.addEventListener("click", () =>
    verificationCodeSender("emailform")
  );
}

function closewindow() {
  overlays.forEach((overlay) => {
    overlay.style.display = "none";
  });
}

function closer() {
  closeoverlays.forEach((closeoverlay) => {
    closeoverlay.addEventListener("click", closewindow);
  });
}

function signup() {
  closewindow();
  resetFormInDiv(overlays[0].id);
  overlays[0].style.display = "flex";
  document.getElementById("signuplogin").addEventListener("click", login);
  closer();
}

function login() {
  document.getElementById("toconfirm").disabled = true;
  closewindow();
  resetFormInDiv(overlays[1].id);
  overlays[1].style.display = "flex";
  closer();
  document
    .getElementById("toconfirm")
    .addEventListener("click", confirmaccount);
  document
    .getElementById("forgotpassword")
    .addEventListener("click", iforgotpassword);
}

document.querySelectorAll("form").forEach((form) => {
  form.addEventListener("submit", function (event) {
    if (
      form.id === "securitypasswordform" ||
      form.id === "logoutForm" ||
      form.id === "loginForm" ||
      form.id === "signupmailform"
    ) {
      return;
    }
    event.preventDefault();
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('loginForm');
  form.addEventListener('submit', function (event) {
      const formData = new FormData(form);
      event.preventDefault();
      fetch('/login/', {
          method: 'POST',
          body: formData,
          headers: {
              'X-CSRFToken': csrfToken
          }
      })
          .then(response => response.json())
          .catch(error => {
              console.error('error', error);
          });
  });
});

function resetFormInDiv(divId) {
  let div = document.getElementById(divId);
  if (div) {
    let form = div.querySelector("form");
    if (form) {
      form.reset();
    }
  }
}

// verification login fields

if (passwordfield && usernamefield) {
  usernamefield.addEventListener("change", testbuttons);
  passwordfield.addEventListener("change", testbuttons);
}
function testbuttons() {
  test = false;
  for (i = 1; i <= testedusers.length - 1; i++) {
    if (testedusers[i].username == usernamelogin.value) {
      confirmedemail.innerText = testedusers[i].email;
      poster.value = testedusers[i].email;
      confirmedphone.innerText = testedusers[i].phone;
      test = true;
      break;
    }
  }
  if (test && !passwordfield.value == "") {
    document.getElementById("toconfirm").disabled = false;
  }
}

// verification forgot password fields

if (forgotmailarea) {
  forgotmailarea.addEventListener("change", testmailfields);
}
function testmailfields() {
  test = false;
  for (i = 1; i <= testedusers.length - 1; i++) {
    if (testedusers[i].email == forgotmailarea.value) {
      confirmedemail.innerText = testedusers[i].email;
      document.getElementById("verifyemailaddress").textContent =
        forgotmailarea.value;
      test = true;
      break;
    }
  }
  if (test) {
    document.getElementById("forgotnext").disabled = false;
  }
}

function confirmaccount() {
  buttoncontinue.disabled = true;
  closewindow();
  resetFormInDiv(overlays[2].id);
  document
    .getElementById("confirmContinue")
    .addEventListener("click", security);
  overlays[2].style.display = "flex";
  closer();
}

// send email

function verificationCodeSender(form) {
  if (document.getElementById("getcodebyphone").checked) {
    mailto.innerText = testedusers[i].phone;
  } else {
    mailto.innerText = testedusers[i].email;
  }
  var formElement = document.getElementById(form);
  if (!(formElement instanceof HTMLFormElement)) {
    console.error("The selected element is not an HTMLFormElement.");
    return;
  }
  var csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  var formData = new FormData(formElement);
  fetch("/email_verification/", {
    method: "POST",
    body: formData,
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": csrfToken,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status == "success") {
        Swal.fire({
          title: "Info",
          text: "A verification  code has been sent to your email",
          icon: "info",
          confirmButtonText: "Ok",
        });
        return;
      } else {
        Swal.fire({
          title: "Info",
          text: "Check email or phone field",
          icon: "info",
          confirmButtonText: "Ok",
        });
      }
    })
    .catch((error) => {
      Swal.fire({
        title: "Error",
        text: "An error occured",
        icon: "info",
        confirmButtonText: "Ok",
      });
    });
}

function security() {
  verificationCodeSender("emailform");
  closewindow();
  resetFormInDiv(overlays[3].id);
  start = 1;
  overlays[3].style.display = "flex";
  document.getElementById("input1").focus();
  closer();
}

// verify mail get verifycation code

async function fetchVerificationCode() {
  try {
    const response = await fetch("/get-verification-code/", {
      method: "GET",
      headers: {
        Authorization: "bvmVNBMBMHB24512vbnmmm45vbgfhvn53VGBHJbjghj275fgcgvnf",
        "Content-Type": "application/json",
      },
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    if (data.verification_code) {
      return data.verification_code;
    } else {
      Swal.fire({
        title: "Invalid Code!",
        text: "Verification code is not found",
        icon: "error",
        confirmButtonText: "Ok",
      });
      return null;
    }
  } catch (error) {
    Swal.fire({
      title: "Error",
      text: "An error occured",
      icon: "error",
      confirmButtonText: "Ok",
    });
    return null;
  }
}

//endofsignin
function endofsignin() {
  closer();
}

function iforgotpassword() {
  closewindow();
  resetFormInDiv(overlays[4].id);
  overlays[4].style.display = "flex";
  document.getElementById("forgotnext").addEventListener("click", forgotnext);
  closer();
}

function forgotnext() {
  verificationCodeSender("forgotmailform");
  resetFormInDiv(overlays[5].id);
  overlays[5].style.display = "flex";
  start = 7;
  document
    .getElementById("forgotVerifyNext")
    .addEventListener("click", verifypass);
  globalemail = forgotmailarea.value;
  document.getElementById("input7").focus();
  closer();
}

function verifypass() {
  closewindow();
  resetFormInDiv(overlays[6].id);
  overlays[6].style.display = "flex";
  document.getElementById("NewPasswordNext").disabled = true;
  document
    .getElementById("NewPasswordNext")
    .addEventListener("click", createpass);
  closer();
}

let passes = document.querySelectorAll(".pass");
let next = document.getElementById("forgotnext");
let characterverifies = document.querySelectorAll(".characterverify");
let verifycode = [];

if (characterverifies) {
  characterverifies.forEach((characterverify) => {
    characterverify.addEventListener("change", changetype);
  });
}

function changetype(e) {
  e.target.type = "password";
}

function moveToNext(previousFieldId, current, nextFieldId) {
  if (!current.value == "") {
    document.getElementById(nextFieldId).focus();
  } else {
    document.getElementById(previousFieldId).focus();
  }
}

function createpass() {
  closewindow();
  overlays[7].style.display = "flex";
  closer();
}

function textviewer(e) {
  e.target.parentElement.nextElementSibling.nextElementSibling.type = "text";
}
function passwordviewer(e) {
  e.target.parentElement.nextElementSibling.nextElementSibling.type =
    "password";
}

let pause = document.getElementById("pausebutton");
let play = document.getElementById("playbutton");
let video = document.getElementById("myvideo");

if (play && pause) {
  play.addEventListener("click", () => {
    play.style.display = "none";
    pause.style.display = "flex";
    video.play();
  });
  pause.addEventListener("click", () => {
    video.pause();
    pause.style.display = "none";
    play.style.display = "flex";
  });
}

//checkboxes

document.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
  checkbox.addEventListener("change", () => {
    document
      .querySelectorAll('input[type="checkbox"]')
      .forEach((otherCheckbox) => {
        if (otherCheckbox !== checkbox) {
          otherCheckbox.checked = false;
        }
      });
  });
});

//add to cart
let wishlist = ["basic"];
let addtocart = document.querySelector("#addtocart");
if (addtocart) {
  addtocart.addEventListener("click", checkcart);
}

function checkcart() {
  if (wishlist) {
    document.querySelector(".red").style.display = "block";
  }
}

document.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
  checkbox.addEventListener("change", () => {
    document
      .querySelectorAll('input[type="checkbox"]')
      .forEach((otherCheckbox) => {
        if (otherCheckbox !== checkbox) {
          otherCheckbox.checked = false;
        }
        if (checkbox.checked) {
          buttoncontinue.disabled = false;
        } else {
          buttoncontinue.disabled = true;
        }
      });
  });
});

//verifycharacter tester

let start;
document.querySelectorAll(".characterverify").forEach((char) => {
  char.addEventListener("change", function () {
    verifier(start);
  });
});

function verifier(start) {
  let counter = 0;
  for (i = start; i <= start + 5; i++) {
    if (document.getElementById(`input${i}`.value)) {
      counter++;
    }
  }
  if (counter === 6) {
    let verifycharacters = "";
    document.querySelectorAll(".characterverify input").forEach((character) => {
      verifycharacters += character.value;
    });
    let globalCode;
    async function main() {
      globalCode = await fetchVerificationCode();
      if (globalCode == verifycharacters) {
        document.getElementById("securityContinue").disabled = false;
        document.getElementById("forgotVerifyNext").disabled = false;
      } else {
        Swal.fire({
          title: "Invalid Code!",
          text: "Verification code is invalid",
          icon: "error",
          confirmButtonText: "Ok",
        });
      }
    }
    main();
  }
}

// password controller

if (pass) {
  pass.forEach((passwordzone) => {
    passwordzone.addEventListener("change", activator);
  });
}

function activator() {
  if (
    document.getElementById("id_new_password1").value &&
    document.getElementById("id_new_password2").value
  ) {
    if (
      document.getElementById("id_new_password1").value ===
      document.getElementById("id_new_password2").value
    ) {
      document.getElementById("NewPasswordNext").disabled = false;
      changer();
    } else {
      Swal.fire({
        title: "Passwords",
        text: "Passwords is not same",
        icon: "error",
        confirmButtonText: "Ok",
      });
    }
  }
}

function changer() {
  const passwordChangeForm = document.getElementById("passwordchange");
  if (passwordChangeForm) {
    passwordChangeForm.addEventListener("submit", function (event) {
      event.preventDefault();
      const newPassword1 = document.getElementById("id_new_password1").value;
      const newPassword2 = document.getElementById("id_new_password2").value;
      const csrfToken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
      ).value;
      email = globalemail;

      fetch("/password-change/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({
          new_password1: newPassword1,
          new_password2: newPassword2,
          email: email,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === "success") {
            overlays[7].style.display = "flex";
          } else if (data.status === "error") {
            Swal.fire({
              title: "Error",
              text: data.message,
              icon: "error",
              confirmButtonText: "Ok",
            });
          }
        })
        .catch((error) => console.error("Error:", error));
    });
  }
  if (document.getElementById("successContinue")) {
    this.addEventListener("click", () => {
      overlays[7].style.display = "none";
    });
  }
}

// profiles
let profilicon = document.querySelector(".profiles");
if (profilicon) {
  profilicon.addEventListener("click", toggledrop);
}

function toggledrop() {
  let profileContents = document.querySelector(".profilecontents");
  if (profileContents) {
    if (profileContents.classList.contains("showed")) {
      profileContents.classList.remove("showed");
      setTimeout(() => {
        profileContents.style.display = "none";
      }, 300);
    } else {
      profileContents.style.display = "flex";
      setTimeout(() => {
        profileContents.classList.add("showed");
      }, 10);

      setTimeout(() => {
        if (profileContents.classList.contains("showed")) {
          profileContents.classList.remove("showed");
          setTimeout(() => {
            profileContents.style.display = "none";
          }, 300);
        }
      }, 3000);
    }
  }
}

let updater = document.getElementById("profileUpdater");
let changebutton = document.getElementById("changephoto");

if (updater && changephoto) {
  changebutton.addEventListener("click", changeprofilephoto);
}

function changeprofilephoto() {
  updater.style.display = "flex";
}

document.addEventListener("DOMContentLoaded", function () {
  let profileForm = document.getElementById("profilePictureForm");
  let profileUpdater = document.getElementById("profileUpdater");
  closer();
  if (profileForm) {
    profileForm.addEventListener("submit", function (event) {
      event.preventDefault();
      let formData = new FormData(profileForm);
      fetch("/update-profile-picture/", {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": document.querySelector(
            'input[name="csrfmiddlewaretoken"]'
          ).value,
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            if (data.new_picture_url) {
              document.getElementById("profilepictureimage").src =
                data.new_picture_url;
              profileUpdater.style.display = "none";
              Swal.fire({
                title: "Profile picture",
                text: "Profile picture updated successfully!",
                icon: "success",
                confirmButtonText: "Ok",
              });
            }
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          Swal.fire({
            title: "Error",
            text: "An error occurred. Please try again.",
            icon: "error",
            confirmButtonText: "Ok",
          });
        });
    });
  }
});

let contactus = document.querySelectorAll(".contactus");

if (contactus) {
  contactus.forEach((cont) => {
    if (cont instanceof Element) {
      cont.addEventListener("click", testers);
    }
  });
}

function testers(e) {
  console.log(isLoggedIn);
  if (!isLoggedIn) {
    login();
    return;
  } else {
    e.target.href='/contact/'
  }
}
