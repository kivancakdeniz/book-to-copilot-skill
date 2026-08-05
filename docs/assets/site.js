if (document.documentElement.lang === "tr") {
  const paletteInputs = document.querySelectorAll('[data-md-component="palette"] input');
  const paletteLabels = document.querySelectorAll('[data-md-component="palette"] label');
  const themeNames = ["Koyu moda geç", "Açık moda geç"];

  paletteInputs.forEach((input, index) => input.setAttribute("aria-label", themeNames[index]));
  paletteLabels.forEach((label, index) => label.setAttribute("title", themeNames[index]));
  document.querySelectorAll(".headerlink").forEach((link) => link.setAttribute("title", "Kalıcı bağlantı"));

  const copyright = document.querySelector(".md-copyright");
  if (copyright) {
    const link = copyright.querySelector("a");
    copyright.replaceChildren(...(link ? [link, " ile oluşturuldu"] : ["Material for MkDocs ile oluşturuldu"]));
  }
}
