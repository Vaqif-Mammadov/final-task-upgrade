var DEOTHEMES = DEOTHEMES || {};

const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

(function ($) {
  "use strict";

  DEOTHEMES.initialize = {
    init: function () {
      DEOTHEMES.initialize.scrollToTop();
      DEOTHEMES.initialize.slickCarousel();
      DEOTHEMES.initialize.navbarSearch();
      DEOTHEMES.initialize.mobileNavigation();
      DEOTHEMES.initialize.lightboxPopup();
      DEOTHEMES.initialize.pricingSwitcher();
      DEOTHEMES.initialize.accordions();
      DEOTHEMES.initialize.tabs();
      DEOTHEMES.initialize.stickySocials();
      DEOTHEMES.initialize.detectBrowserWidth();
      DEOTHEMES.initialize.detectMobile();
      DEOTHEMES.initialize.detectIE();
    },

    preloader: function () {
      $(".loader").fadeOut();
      $(".loader-mask").delay(350).fadeOut("slow");
    },

    triggerResize: function () {
      $window.trigger("resize");
    },

    scrollToTopScroll: function () {
      var scroll = $window.scrollTop();
      if (scroll >= 50) {
        $backToTop.addClass("show");
      } else {
        $backToTop.removeClass("show");
      }
    },

    scrollToTop: function () {
      $backToTop.on("click", function () {
        $("html, body").animate({ scrollTop: 0 }, 1350, "easeInOutQuint");
        return false;
      });
    },

    slickCarousel: function () {
      $(".slick-custom-arrows").each(function (idx, item) {
        var carouselId = "carousel-" + idx;
        this.id = carouselId;

        $(this).slick({
          slide: "#" + carouselId + " .slick-slide",
          appendArrows: "#" + carouselId + " .slick-custom-nav",
          arrows: true,
          nextArrow: "#" + carouselId + " .slick-custom-nav__next",
          prevArrow: "#" + carouselId + " .slick-custom-nav__prev",
          slidesToShow: 1,
          fade: true,
          adaptiveHeight: true,
          cssEase: "linear",
        });
      });

      $(".slick-service-boxes").slick({
        arrows: false,
        dots: true,
        slidesToShow: 3,
        infinite: false,

        responsive: [
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 2,
            },
          },
          {
            breakpoint: 768,
            settings: {
              slidesToShow: 1,
            },
          },
        ],
      });

      $(".slick-service-boxes--1").slick({
        arrows: true,
        dots: false,
        slidesToShow: 3,
        infinite: true,

        responsive: [
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 2,
            },
          },
          {
            breakpoint: 768,
            settings: {
              slidesToShow: 1,
            },
          },
        ],
      });

      $(".slick-team").slick({
        arrows: false,
        dots: true,
        slidesToShow: 3,
        infinite: false,

        responsive: [
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 2,
            },
          },
          {
            breakpoint: 768,
            settings: {
              slidesToShow: 1,
            },
          },
        ],
      });
    },
    stickyNavbar: function () {
      var $navSticky = $(".nav--sticky");

      if ($window.scrollTop() > 190) {
        $navSticky.addClass("sticky navbar-black"); // Qara fon və ağ mətn üçün sinif əlavə olundu
      } else {
        $navSticky.removeClass("sticky navbar-black"); // Sticky sinif çıxarıldı
      }

      if ($window.scrollTop() > 200) {
        $navSticky.addClass("offset");
      } else {
        $navSticky.removeClass("offset");
      }

      if ($window.scrollTop() > 500) {
        $navSticky.addClass("scrolling");
      } else {
        $navSticky.removeClass("scrolling");
      }
    },

    navbarSearch: function () {
      var $navSearchForm = $(".nav__search-form"),
        $navSearchTrigger = $("#nav__search-trigger"),
        $navSearchInput = $("#nav__search-input"),
        $navSearchClose = $("#nav__search-close");

      $navSearchTrigger.on("click", function (e) {
        e.preventDefault();
        $navSearchForm.animate({ opacity: "toggle" }, 500);
        $navSearchInput.focus();
      });

      $navSearchClose.on("click", function (e) {
        e.preventDefault();
        $navSearchForm.animate({ opacity: "toggle" }, 500);
      });

      function closeSearch() {
        $navSearchForm.fadeOut(200);
      }

      $(document.body).on("click", function (e) {
        closeSearch();
      });

      $navSearchInput.add($navSearchTrigger).on("click", function (e) {
        e.stopPropagation();
      });
    },

    mobileNavigation: function () {
      var $navDropdown = $(".nav__dropdown");
      var $navDropdownMenu = $(".nav__dropdown-menu");

      $(".nav__dropdown-trigger").on("click", function () {
        var $this = $(this);
        $this.toggleClass("nav__dropdown-trigger--is-open");
        $this.next($navDropdownMenu).slideToggle();
        $this.attr("aria-expanded", function (index, attr) {
          return attr == "true" ? "false" : "true";
        });
      });

      if ($html.hasClass("mobile")) {
        $body.on("click", function () {
          $navDropdownMenu.addClass("hide-dropdown");
        });

        $navDropdown.on("click", "> a", function (e) {
          e.preventDefault();
        });

        $navDropdown.on("click", function (e) {
          e.stopPropagation();
          $navDropdownMenu.removeClass("hide-dropdown");
        });
      }
    },

    lightboxPopup: function () {
      $(".lightbox-img, .lightbox-video").magnificPopup({
        callbacks: {
          elementParse: function (item) {
            if (item.el.context.className == "lightbox-video") {
              item.type = "iframe";
            } else {
              item.type = "image";
            }
          },
        },
        type: "image",
        closeBtnInside: false,
        gallery: {
          enabled: true,
        },
        image: {
          titleSrc: "title",
          verticalFit: true,
        },
      });

      // Single video lightbox
      $(".single-video-lightbox").magnificPopup({
        type: "iframe",
        closeBtnInside: false,
        tLoading: "Loading image #%curr%...",
      });
    },

    pricingSwitcher: function () {
      var $pricingPrice = $(".pricing__price");
      var $yearly = $(".price-switcher__button-yearly");
      var $monthly = $(".price-switcher__button-monthly");

      $yearly.on("click", function (e) {
        $(this).addClass("price-switcher__button--is-active");
        $(this).siblings().removeClass("price-switcher__button--is-active");
        $pricingPrice.each(function () {
          $(this).text($(this).data("year-price"));
        });
      });

      $monthly.on("click", function () {
        $(this).addClass("price-switcher__button--is-active");
        $(this).siblings().removeClass("price-switcher__button--is-active");
        $pricingPrice.each(function () {
          $(this).text($(this).data("month-price"));
        });
      });
    },

    accordions: function () {
      var $accordion = $(".accordion");
      function toggleChevron(e) {
        $(e.target)
          .prev(".accordion__heading")
          .find("a")
          .toggleClass("accordion--is-open accordion--is-closed");
      }
      $accordion.on("hide.bs.collapse", toggleChevron);
      $accordion.on("show.bs.collapse", toggleChevron);
    },

    tabs: function () {
      $(".tabs__trigger").on("click", function (e) {
        var currentAttrValue = $(this).attr("href");
        $(".tabs__content-trigger " + currentAttrValue)
          .stop()
          .fadeIn(1000)
          .siblings()
          .hide();
        $(this)
          .parent("li")
          .addClass("tabs__item--active")
          .siblings()
          .removeClass("tabs__item--active");
        e.preventDefault();
      });
    },

    stickySocials: function () {
      var $stickyCol = $(".sticky-col");
      if ($stickyCol) {
        $stickyCol.stick_in_parent({
          offset_top: 100,
        });
      }
    },

    containerFullHeight: function () {
      var $fullHeight = $(".full-height");

      if (!minWidth(992)) {
        $fullHeight.height($window.height() - 60);
      } else {
        $fullHeight.height($window.height());
      }
    },

    detectBrowserWidth: function () {
      if (Modernizr.mq("(min-width: 0px)")) {
        // Browsers that support media queries
        minWidth = function (width) {
          return Modernizr.mq("(min-width: " + width + "px)");
        };
      } else {
        // Fallback for browsers that does not support media queries
        minWidth = function (width) {
          return $window.width() >= width;
        };
      }
    },

    detectMobile: function () {
      if (
        /Android|iPhone|iPad|iPod|BlackBerry|Windows Phone/i.test(
          navigator.userAgent || navigator.vendor || window.opera
        )
      ) {
        $html.addClass("mobile");
      } else {
        $html.removeClass("mobile");
      }
    },

    detectIE: function () {
      if (Function("/*@cc_on return document.documentMode===10@*/")()) {
        $html.addClass("ie");
      }
    },
  };

  DEOTHEMES.documentOnReady = {
    init: function () {
      DEOTHEMES.initialize.init();
    },
  };

  DEOTHEMES.windowOnLoad = {
    init: function () {
      DEOTHEMES.initialize.preloader();
      DEOTHEMES.initialize.triggerResize();
    },
  };

  DEOTHEMES.windowOnResize = {
    init: function () {
      DEOTHEMES.initialize.containerFullHeight();
    },
  };

  DEOTHEMES.windowOnScroll = {
    init: function () {
      DEOTHEMES.initialize.scrollToTopScroll();
      DEOTHEMES.initialize.stickyNavbar();
    },
  };

  var $window = $(window),
    $html = $("html"),
    $body = $("body"),
    $backToTop = $("#back-to-top"),
    minWidth;

  $(document).ready(DEOTHEMES.documentOnReady.init);
  $window.on("load", DEOTHEMES.windowOnLoad.init);
  $window.on("resize", DEOTHEMES.windowOnResize.init);
  $window.on("scroll", DEOTHEMES.windowOnScroll.init);
})(jQuery);

let submitbutton = document.querySelector("#submit");

if (submitbutton) {
  submitbutton.addEventListener("click", addcommentfunction);
}

function addcommentfunction(event) {
  // if (!isLoggedIn) {
  //   login();
  //   return;
  // } else {
    const form = document.getElementById("commentform");
    event.preventDefault();
    form.querySelector('input[type="submit"]').disabled = true;
    const formData = {
      name: document.querySelector("#name").value,
      email: document.querySelector("#mail").value,
      url: document.getElementById("url").value,
      comment: document.getElementById("comment").value,
      wp_comment_cookies_consent: document.getElementById(
        "wp-comment-cookies-consent"
      ).checked,
      comment_post_ID: document.getElementById("comment_post_ID").value,
    };
    console.log(formData);
    fetch("/addcomment/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value,
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "success") {
          Swal.fire({
            title: "Info",
            text: "Comment added successfully",
            icon: "info",
            confirmButtonText: "Ok",
          });
          window.location.reload();
          form.reset();
        } else {
          Swal.fire({
            title: "Error",
            text: data.message || "There was an error",
            icon: "error",
            confirmButtonText: "Ok",
          });
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      })
      .finally(() => {
        form.querySelector('input[type="submit"]').disabled = false;
      });
  }
// }

function addReplyFunction(event, comment_id) {
  event.preventDefault();
  const formData = {
    reply_text: document.querySelector(`#reply-text-${comment_id}`).value, // Yalnız reply_text sahəsini yığırıq
  };

  fetch(`/add_reply/${comment_id}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
    },
    body: JSON.stringify(formData),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === "success") {
        window.location.reload();
      } else {
        console.log(data.message || "Error adding reply");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

let submitmessage = document.querySelector("#submit-message");
if (submitmessage) {
  submitmessage.addEventListener("click", usercontactFunction);
}

function usercontactFunction(event) {
  event.preventDefault();
  const formData = {
    name: document.querySelector("#name").value,
    phone: document.getElementById("phone").value,
    note: document.getElementById("message").value,
    yourconsent: document.getElementById("yourconsent").checked,
  };

  fetch(`/usercontact/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify(formData),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === "success") {
        Swal.fire({
          title: "Success",
          text: "Note added successfully",
          icon: "success",
          confirmButtonText: "Ok",
        }).then((result) => {
          window.location.reload();
        });
      } else {
        console.log(data.message || "Error adding note");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

// FAQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQq
let faqform = document.getElementById("contact-form");

if (faqform) {
  faqform.addEventListener("submit", function (event) {
    event.preventDefault();

    const data = {
      full_name: this.querySelector('[name="name"]').value,
      email: this.querySelector('[name="email"]').value,
      phone: this.querySelector('[name="phone"]').value,
      message: this.querySelector('[name="message"]').value,
      form_id: this.id,
    };
    fetch("/faq/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        Swal.fire({
          icon: data.status === "success" ? "success" : "error",
          title: data.status === "success" ? "Success" : "Error",
          text: data.message,
        });
      })
      .catch((error) => {
        console.error("Error:", error);
        Swal.fire({
          icon: "error",
          title: "Error",
          text: "Something went wrong!",
        });
      });
  });
}

// FAQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

// BLOGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG

document.addEventListener("DOMContentLoaded", function () {
  const newsletterForm = document.getElementById("newslettersend");

  if (newsletterForm) {
    newsletterForm.addEventListener("submit", function (event) {
      if (!isLoggedIn) {
        login();
        return;
      } else {
        event.preventDefault();
        const form = document.getElementById("newslettersend");
        const formData = new FormData(form);

        fetch("/send-newsletter/", {
          method: "POST",
          body: formData,
          headers: {
            "X-CSRFToken": csrfToken,
          },
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.success) {
              Swal.fire({
                icon: "success",
                title: "Success!",
                text: data.message,
                confirmButtonText: "OK",
              }).then(() => {
                form.reset();
              });
            } else {
              Swal.fire({
                icon: "error",
                title: "Error!",
                text: data.message,
                confirmButtonText: "OK",
              });
            }
          })
          .catch((error) => {
            console.error("Error:", error);
            Swal.fire({
              icon: "error",
              title: "Error!",
              text: "An unexpected error occurred.",
              confirmButtonText: "OK",
            });
          });
      }
    });
  }
});

let newslist = [];
let news_length = document.querySelector("#list-length");

if (news_length) {
  let news_length_int = parseInt(news_length.textContent);
  let pagination = document.querySelector("#pagination");

  // Hər səhifəyə 5 məqalə bölmək üçün pagination yarat
  let totalPages = Math.ceil(news_length_int / 5); // 5 məqalə bir səhifədə olacaq

  for (let i = 2; i <= totalPages; i++) {
    if (i <= 5) {
      const li = document.createElement("a");
      li.classList.add("page-numbers");
      li.textContent = i;
      li.addEventListener("click", function () {
        sendstartcount(i); // Səhifə nömrəsini funksiyaya ötür
      });
      pagination.appendChild(li);
    }
  }

  // Sağ istiqaməti (next arrow) əlavə et
  const next = document.createElement("a");
  const nextIcon = document.createElement("i");
  next.addEventListener("click", decrease);
  nextIcon.classList.add("fa-solid", "fa-angle-right");
  next.classList.add("next", "page-numbers");
  next.appendChild(nextIcon);
  pagination.appendChild(next);
}

let basepath = "/media/";
let sibling;
let elements = [];
let pageNumber;
let pagenumberdecreaser = document.querySelector("#pagenumberdecreaser");

if (pagenumberdecreaser) {
  pagenumberdecreaser.addEventListener("click", decrease);
}

function decrease() {
  pageNumber = 1;
  pageNumber++;
  sendstartcount(pageNumber);
}

function sendstartcount(pageNumber) {
  pageNumber = pageNumber;
  elements = [];
  let pagination = document.querySelector("#pagination");
  sibling = pagination.childNodes;
  let startcount = (pageNumber - 1) * 5 + 1; // Hər səhifədə 5 məqalə var
  newinstaller(startcount, pageNumber);
  sibling.forEach((element) => {
    if (element.nodeType === 1) {
      elements.push(element);
    }
  });

  elements.forEach((element, index) => {
    if (pageNumber !== index + 1) {
      if (element.nodeType === 1) {
        element.classList.remove("current");
      }
    } else {
      if (element.nodeType === 1) {
        element.classList.add("current");
      }
    }
  });
}

function newinstaller(startcount, pageNumber) {
  const token = "bvmVNBMBMHB24512vbnmmm45vbgfhvn53VGBHJbjghj275fgcgv";

  fetch("/blogjs/", {
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
      if (data.news && Array.isArray(data.news)) {
        newslist = data.news; // Data yenidən əldə edilir
        console.log(newslist);
        let newsDiv = document.querySelector("#news");
        newsDiv.innerHTML = "";

        let endcount = startcount + 4; // Hər səhifədə 5 məqalə
        if (endcount > newslist.length) {
          endcount = newslist.length;
        }

        let single = "/single_posts/";
        let cat = "";

        for (let i = startcount - 1; i < endcount; i++) {
          let category2 = newslist[i].category2;
          if (category2) {
            cat = `<a href="${
              single + newslist[i].id
            }" id="entry__category_2" class="entry__category-item">${category2}</a>`;
          }
          newsDiv.innerHTML +=
            `
            <article>
              <div class="entry__header">
                <a href="${single + newslist[i].id}">
                  <img src="${basepath}${
              newslist[i].image
            }" class="entry__img" alt="">
                </a>
                <div class="entry__category">
                  <a href="${
                    single + newslist[i].id
                  }" id="entry__category_1" class="entry__category-item">${
              newslist[i].category
            }</a>
                  ` +
            cat +
            `
                </div>
              </div>
              <div class="entry__body">
                <h4 class="entry__title">
                  <a href="${single + newslist[i].id}">${newslist[i].title}</a>
                </h4>
                <div class="entry__meta">
                  <span class="entry__meta-item entry__meta-author">
                    <a href="${
                      single + newslist[i].id
                    }"class="entry__meta-author-url">
                      <img src="${basepath}${
              newslist[i].icon
            }" class="entry__meta-author-img" alt="">
                      <span class="entry__meta-author-name">${
                        newslist[i].name_lastname
                      }</span>
                    </a>
                  </span>
                  <span class="entry__meta-item entry__meta-date">${
                    newslist[i].history
                  }</span>
                </div>
                <div class="entry__excerpt">
                  <p>${newslist[i].content.slice(0, 340)}...</p>
                </div>
              </div>
            </article>`;
        }
      } else {
        console.error("Veri bir dizi değil veya boş", data);
      }
    })
    .catch((error) => console.error("Error", error));
}

// İlk səhifəni yüklə
sendstartcount(1);

// BLOGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
