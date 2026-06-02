/* content-loader.js — aplica content.json ao DOM via data-key attributes
   Falha silenciosamente se content.json não existir (baked-in HTML permanece visível). */
(function () {
  'use strict';

  var STARS = (function () {
    var s = '';
    for (var i = 0; i < 5; i++) s += '<svg class="ico"><use href="#i-star"></use></svg>';
    return s;
  }());

  function getPath(obj, path) {
    return path.split('.').reduce(function (o, k) {
      return (o !== null && o !== undefined && o[k] !== undefined) ? o[k] : null;
    }, obj);
  }

  function esc(s) {
    return String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function applyKeys(c) {
    document.querySelectorAll('[data-key]').forEach(function (el) {
      var val = getPath(c, el.getAttribute('data-key'));
      if (val === null) return;
      var type = el.getAttribute('data-key-type') || 'text';
      if      (type === 'html') el.innerHTML  = val;
      else if (type === 'src')  el.src        = val;
      else if (type === 'href') el.href       = val;
      else                      el.textContent = val;
      var altKey = el.getAttribute('data-key-alt');
      if (altKey) { var av = getPath(c, altKey); if (av !== null) el.alt = av; }
    });
  }

  function applyContatos(ct) {
    if (!ct) return;
    var phone = ct.whatsapp || '5584994055713';
    window.__NM_PHONE = phone;
    var waMsg = encodeURIComponent('Oi, vim pelo site e quero fazer uma cotação!');
    var waUrl = 'https://wa.me/' + phone + '?text=' + waMsg;
    document.querySelectorAll('[data-contact]').forEach(function (el) { el.href = waUrl; });
    if (ct.email) {
      document.querySelectorAll('a[href^="mailto:"]').forEach(function (el) {
        el.href = 'mailto:' + ct.email;
        if (el.textContent.indexOf('@') !== -1) el.textContent = ct.email;
      });
    }
    if (ct.instagram_url && ct.instagram_url !== '#') {
      document.querySelectorAll('a[aria-label="Instagram"]').forEach(function (el) {
        el.href = ct.instagram_url;
      });
    }
    if (ct.instagram_label) {
      document.querySelectorAll('.nm-footer-cols a').forEach(function (el) {
        if (el.textContent.indexOf('@') !== -1) {
          el.textContent = ct.instagram_label;
          if (ct.instagram_url && ct.instagram_url !== '#') el.href = ct.instagram_url;
        }
      });
    }
  }

  function buildCard(d) {
    var pos = d.imagem_posicao ? ' style="background-position:' + esc(d.imagem_posicao) + '"' : '';
    return '<article class="nm-bento-card"' +
      ' data-bento-bg="' + esc(d.imagem_url) + '"' +
      ' data-bento-title="' + esc(d.titulo) + '"' +
      ' data-bento-badge="' + esc(d.badge) + '"' +
      ' data-bento-text="' + esc(d.texto) + '"' +
      ' aria-label="Ver roteiro ' + esc(d.titulo) + '">' +
      '<div class="nm-bento-card-img" data-bg="' + esc(d.imagem_url) + '"' + pos + '></div>' +
      '<div class="nm-bento-card-info">' +
      '<span class="nm-bento-badge">' + esc(d.badge) + '</span>' +
      '<h3 class="nm-bento-title">' + esc(d.titulo) + '</h3>' +
      '<p class="nm-bento-text">' + esc(d.texto) + '</p>' +
      '</div></article>';
  }

  function applyDestinos(destinos) {
    var bento = document.querySelector('.nm-bento');
    if (!bento) return;
    bento.innerHTML = destinos.map(buildCard).join('');
    /* Registra novos elementos no observer de lazy-load */
    if (window.__nmBgIo) {
      bento.querySelectorAll('[data-bg]').forEach(function (el) {
        window.__nmBgIo.observe(el);
      });
    } else {
      bento.querySelectorAll('[data-bg]').forEach(function (el) {
        el.style.backgroundImage = "url('" + el.dataset.bg + "')";
        el.removeAttribute('data-bg');
      });
    }
    /* Re-inicializa o modal com os novos cards */
    if (typeof window.nmBentoInit === 'function') window.nmBentoInit();
    /* Re-registra no reveal observer */
    if (window.__nmRevealIo) {
      bento.querySelectorAll('.nm-bento-card').forEach(function (el) {
        window.__nmRevealIo.observe(el);
      });
    }
  }

  function buildDepCard(d, hidden) {
    return '<div class="nm-dep-card"' + (hidden ? ' aria-hidden="true"' : '') + '>' +
      '<div class="nm-dep-stars">' + STARS + '</div>' +
      '<p class="nm-dep-card-quote"><em>“' + esc(d.quote) + '”</em></p>' +
      '<div class="nm-dep-card-foot">' +
      '<div class="nm-dep-card-avatar" aria-hidden="true"></div>' +
      '<div><div class="nm-dep-card-name">' + esc(d.nome) + '</div>' +
      '<div class="nm-dep-card-dest">' + esc(d.destino) + '</div></div>' +
      '</div></div>';
  }

  function applyDepoimentos(depoimentos) {
    [1, 2, 3].forEach(function (col) {
      var track = document.querySelector('.nm-dep-track-' + col);
      if (!track) return;
      var cards = depoimentos.filter(function (d) { return d.coluna === col; });
      if (!cards.length) return;
      track.innerHTML =
        cards.map(function (d) { return buildDepCard(d, false); }).join('') +
        cards.map(function (d) { return buildDepCard(d, true); }).join('');
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    fetch('content.json?v=' + Date.now())
      .then(function (r) { if (!r.ok) throw new Error('no content'); return r.json(); })
      .then(function (c) {
        applyKeys(c);
        applyContatos(c.contatos);
        if (c.destinos  && c.destinos.length)  applyDestinos(c.destinos);
        if (c.depoimentos && c.depoimentos.length) applyDepoimentos(c.depoimentos);
      })
      .catch(function () {});
  });
}());
