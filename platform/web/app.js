(() => {
  const toggle = document.querySelector('[data-nav-toggle]');
  const nav = document.querySelector('[data-nav]');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    nav.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }));
  }

  const verifyForm = document.querySelector('[data-verify-form]');
  const verifyResult = document.querySelector('[data-verify-result]');
  if (verifyForm && verifyResult) {
    verifyForm.addEventListener('submit', (event) => {
      event.preventDefault();
      const value = String(new FormData(verifyForm).get('trustId') || '').trim();
      verifyResult.hidden = false;
      verifyResult.innerHTML = value
        ? `<strong>Reference mode only.</strong> No live authority or transaction system is connected in this repository prototype. Entered ID: <code>${value.replace(/[<>&"']/g, '')}</code>.`
        : '<strong>Enter a Trust Record ID.</strong> This repository prototype does not query live production systems.';
    });
  }
})();
