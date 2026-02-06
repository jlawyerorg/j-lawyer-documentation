document$.subscribe(function () {
  var PATTERN = /^\{\{[A-Z_0-9]+\}\}$/;

  document.querySelectorAll("td code").forEach(function (code) {
    var text = code.textContent.trim();
    if (!PATTERN.test(text)) return;
    if (code.parentElement.classList.contains("copy-placeholder-wrapper")) return;

    var wrapper = document.createElement("span");
    wrapper.className = "copy-placeholder-wrapper";
    code.parentNode.insertBefore(wrapper, code);
    wrapper.appendChild(code);

    var btn = document.createElement("button");
    btn.className = "copy-placeholder-btn";
    btn.title = "In Zwischenablage kopieren";
    btn.setAttribute("aria-label", "In Zwischenablage kopieren");

    var icon = document.createElement("span");
    icon.className = "copy-placeholder-icon";
    btn.appendChild(icon);

    btn.addEventListener("click", function (e) {
      e.preventDefault();
      navigator.clipboard.writeText(text).then(function () {
        btn.classList.add("copied");
        setTimeout(function () {
          btn.classList.remove("copied");
        }, 1500);
      });
    });

    wrapper.appendChild(btn);
  });
});
