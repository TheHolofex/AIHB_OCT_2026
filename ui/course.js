/* Local reading preferences are navigation conveniences, never learning evidence. */
(() => {
  'use strict';
  const one = (selector, root = document) => root.querySelector(selector);
  const all = (selector, root = document) => [...root.querySelectorAll(selector)];
  const main = one('#main');
  const data = JSON.parse(one('#rf-page-data').textContent);
  const root = new URL(data.root, location.href);
  const key = `reformation-ui:v1:${root.pathname}`;
  const pages = new Map(data.pages.map(page => [page.path, page]));
  const modules = new Map(data.modules.map(module => [module.id, module]));
  const modalSupported = typeof HTMLDialogElement !== 'undefined' && typeof HTMLDialogElement.prototype.showModal === 'function';
  const plainClick = event => event.button === 0 && !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey;
  const decode = hash => { try { return decodeURIComponent(hash.slice(1)); } catch { return null; } };
  const urlFor = (path, anchor = '') => new URL(path + (anchor ? `#${encodeURIComponent(anchor)}` : ''), root).href;
  const blankState = () => ({version: 1, theme: 'system', view: 'guided', last: null, positions: {}});
  const targets = page => pages.has(page) ? data.resume[page] || [] : [];
  let state = blankState();
  let storageAvailable = true;
  let storageAnnounced = false;
  let printing = false;

  function storageFailure() {
    storageAvailable = false;
    if (!storageAnnounced) {
      one('#rf-state-status').textContent = 'Your place could not be saved on this device.';
      storageAnnounced = true;
    }
  }
  function save() {
    if (!storageAvailable) return;
    try { localStorage.setItem(key, JSON.stringify(state)); } catch { storageFailure(); }
  }
  function load() {
    let raw;
    try { raw = localStorage.getItem(key); } catch { storageFailure(); return; }
    let value;
    try { value = JSON.parse(raw); } catch { return; }
    if (!value || value.version !== 1) return;
    if (['system', 'dark', 'sand'].includes(value.theme)) state.theme = value.theme;
    if (['guided', 'read'].includes(value.view)) state.view = value.view;
    const last = value.last;
    if (last && pages.has(last.page) && ['lab', 'setup'].includes(pages.get(last.page).kind)) {
      state.last = {page: last.page, anchor: targets(last.page).some(item => item.id === last.anchor) ? last.anchor : ''};
    }
    if (value.positions && typeof value.positions === 'object') {
      for (const [page, anchor] of Object.entries(value.positions)) {
        if (targets(page).some(item => item.id === anchor && !item.optional) &&
            (page !== data.page || one('.rf-step > h2[id="' + anchor + '"]'))) state.positions[page] = anchor;
      }
    }
  }
  function remember(anchor, core) {
    if (printing || !targets(data.page).some(item => item.id === anchor)) return;
    if (core) state.positions[data.page] = anchor;
    state.last = {page: data.page, anchor};
    save();
  }
  function applyTheme() {
    if (state.theme === 'system') document.documentElement.removeAttribute('data-sc-theme');
    else document.documentElement.dataset.scTheme = state.theme;
    all('[data-theme]').forEach(select => { select.value = state.theme; });
  }
  function initTheme() {
    applyTheme();
    all('[data-theme]').forEach(select => {
      select.addEventListener('change', () => { state.theme = select.value; applyTheme(); save(); });
      select.closest('.rf-appearance').hidden = false;
    });
  }
  function resumeRecord() {
    if (!state.last) return null;
    const page = pages.get(state.last.page);
    const section = targets(page.path).find(item => item.id === state.last.anchor);
    return {page, section, module: modules.get(page.moduleId)};
  }
  function renderHomeResume() {
    const primary = one('#rf-home-primary');
    if (!primary) return;
    const resume = resumeRecord();
    const setup = one('#rf-home-setup');
    const note = one('#rf-resume-note');
    if (!resume) {
      primary.textContent = 'Start with setup';
      primary.href = urlFor(data.modules[0].overview);
      setup.hidden = note.hidden = true;
      return;
    }
    primary.textContent = `Continue · ${resume.module.caseName}`;
    primary.href = urlFor(resume.page.path, resume.section?.id);
    note.textContent = `${resume.section?.title || resume.page.title} · Last opened on this device`;
    setup.hidden = note.hidden = false;
  }
  function initReset() {
    all('[data-reset-place]').forEach(button => {
      button.addEventListener('click', () => {
        if (!confirm('Reset saved place for this course on this device?')) return;
        state.last = null;
        state.positions = {};
        save();
        renderHomeResume();
      });
      button.hidden = false;
    });
  }

  // Removing [hidden] prepares a native dialog; only showModal makes it visible.
  function dialogController(dialog, fallback = false) {
    let trigger;
    function restoreFocus() {
      const destination = trigger?.getClientRects().length ? trigger : one('.rf-brand');
      destination?.focus({preventScroll: true});
    }
    function close() {
      if (modalSupported) dialog.close();
      else { dialog.hidden = true; delete dialog.dataset.inFlow; restoreFocus(); }
    }
    all('[data-dialog-close]', dialog).forEach(button => button.addEventListener('click', close));
    dialog.addEventListener('close', restoreFocus);
    dialog.addEventListener('click', event => {
      if (event.target !== dialog) return;
      const box = dialog.getBoundingClientRect();
      if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) close();
    });
    dialog.addEventListener('keydown', event => {
      if (event.key === 'Escape') { event.preventDefault(); close(); }
    });
    if (modalSupported) dialog.hidden = false;
    else if (fallback) dialog.setAttribute('role', 'region');
    return {
      close,
      open(source) {
        if (!dialog.open && !dialog.hasAttribute('data-in-flow')) trigger = source || document.activeElement;
        if (modalSupported) { if (!dialog.open) dialog.showModal(); }
        else if (fallback) { dialog.dataset.inFlow = ''; dialog.hidden = false; }
      }
    };
  }
  function initCourse() {
    if (!modalSupported) return;
    const trigger = one('[data-course-open]');
    const dialog = one('#rf-course-dialog');
    const controller = dialogController(dialog);
    trigger.addEventListener('click', () => controller.open(trigger));
    all('a', dialog).forEach(link => link.addEventListener('click', event => { if (plainClick(event)) controller.close(); }));
    trigger.hidden = false;
    one('.rf-course-fallback').hidden = true;
  }
  function initCopy() {
    all('pre[data-command]').forEach(pre => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'sc-btn rf-btn sc-btn--secondary rf-copy';
      button.textContent = 'Copy command';
      button.addEventListener('click', async () => {
        const status = one('#copy-status');
        try {
          await navigator.clipboard.writeText(one('code', pre).textContent);
          status.textContent = 'Command copied.';
        } catch { status.textContent = 'Copy failed. Select the command text and copy it manually.'; }
      });
      pre.before(button);
    });
  }
  function initFigures() {
    if (!modalSupported) return;
    const dialog = one('#rf-figure-dialog');
    const controller = dialogController(dialog);
    all('[data-figure-open]').forEach(link => link.addEventListener('click', event => {
      if (!plainClick(event)) return;
      const source = one('img', link.closest('.rf-figure'));
      const image = document.createElement('img');
      image.src = link.href;
      image.alt = source.alt;
      image.width = Number(source.getAttribute('width'));
      image.height = Number(source.getAttribute('height'));
      one('.rf-figure-scroll', dialog).replaceChildren(image);
      event.preventDefault();
      controller.open(link);
    }));
  }

  function initSearch() {
    const dialog = one('#rf-search-dialog');
    const trigger = one('[data-search-open]');
    const input = one('#rf-search-input');
    const results = one('#rf-search-results');
    const status = one('#rf-search-status');
    const recovery = one('.rf-search-recovery');
    const controller = dialogController(dialog, true);
    let index = null;
    let request = null;
    function find() {
      const query = input.value.toLowerCase().trim().replace(/\s+/g, ' ');
      if (!query) {
        const list = data.modules.map(module => ({path: module.overview, title: module.caseName, context: `${module.id} · Overview`, anchor: '', excerpt: ''}));
        const resume = resumeRecord();
        if (resume) list.unshift({path: resume.page.path, anchor: resume.section?.id || '', title: `Continue · ${resume.module.caseName}`, context: resume.section?.title || resume.page.title, excerpt: 'Last opened on this device'});
        return list;
      }
      const tokens = query.split(' ');
      const list = [];
      for (const page of index.pages) {
        if (!pages.has(page.path)) continue;
        for (const section of page.sections) {
          const title = section.title || page.title;
          const headings = `${page.title} ${title}`.toLowerCase();
          const prose = section.text || '';
          const haystack = `${headings} ${prose.toLowerCase()}`;
          if (!tokens.every(token => haystack.includes(token))) continue;
          const lower = title.toLowerCase();
          const rank = lower === query || page.title.toLowerCase() === query ? 0 :
            lower.startsWith(query) || page.title.toLowerCase().startsWith(query) ? 1 : tokens.every(token => headings.includes(token)) ? 2 : 3;
          const matches = tokens.map(token => prose.toLowerCase().indexOf(token)).filter(at => at >= 0);
          const start = matches.length ? Math.max(0, Math.min(...matches) - 45) : 0;
          const excerpt = (start ? '…' : '') + prose.slice(start, start + 180) + (prose.length > start + 180 ? '…' : '');
          const module = modules.get(page.moduleId);
          list.push({path: page.path, anchor: section.id, title, rank, order: list.length,
            context: `${module ? `${module.id} · ${module.caseName} · ` : ''}${page.title}${section.optional ? ' · Optional stretch' : ''}`, excerpt});
        }
      }
      return list.sort((a, b) => a.rank - b.rank || a.order - b.order).slice(0, 20);
    }
    function render() {
      if (!index) return;
      const found = find();
      results.replaceChildren();
      status.textContent = found.length ? `${found.length} results` : 'No matches.';
      for (const item of found) {
        const li = document.createElement('li');
        const link = document.createElement('a');
        link.href = urlFor(item.path, item.anchor);
        for (const [className, content] of [['rf-search-meta', item.context], ['rf-search-title', item.title], ['rf-search-excerpt', item.excerpt]]) {
          if (!content) continue;
          const span = document.createElement('span');
          span.className = className;
          span.textContent = content;
          link.append(span);
        }
        link.addEventListener('click', event => { if (plainClick(event)) controller.close(); });
        li.append(link);
        results.append(li);
      }
    }
    async function loadIndex(retry = false) {
      if (retry) request = null;
      if (!request) {
        status.textContent = 'Loading search…';
        recovery.hidden = true;
        request = fetch(new URL('assets/search-index.json', root), {credentials: 'same-origin'}).then(response => {
          if (!response.ok) throw new Error('Search unavailable');
          return response.json();
        }).then(value => {
          if (value.version !== 1 || !Array.isArray(value.pages)) throw new Error('Invalid search index');
          return value;
        });
      }
      try { index = await request; recovery.hidden = true; render(); }
      catch { index = null; results.replaceChildren(); status.textContent = 'Search unavailable. Retry or use the Course map.'; recovery.hidden = false; }
    }
    function open(source) { controller.open(source); input.focus(); input.select(); loadIndex(); }
    trigger.addEventListener('click', () => open(trigger));
    input.addEventListener('input', render);
    one('[data-search-retry]').addEventListener('click', () => loadIndex(true));
    document.addEventListener('keydown', event => {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k' && !event.target.closest('input, textarea, select, [contenteditable]:not([contenteditable="false"])')) {
        event.preventDefault(); open(document.activeElement === document.body ? trigger : document.activeElement);
      }
    });
    dialog.addEventListener('keydown', event => {
      if (!['ArrowDown', 'ArrowUp'].includes(event.key)) return;
      const links = all('a', results);
      const at = links.indexOf(document.activeElement);
      if (!links.length || (event.target !== input && at < 0)) return;
      event.preventDefault();
      if (at === 0 && event.key === 'ArrowUp') input.focus();
      else links[at < 0 ? 0 : (at + (event.key === 'ArrowDown' ? 1 : -1) + links.length) % links.length].focus();
    });
    trigger.hidden = false;
  }

  function revealDetails(target) {
    for (let node = target; node && node !== main; node = node.parentElement) if (node.tagName === 'DETAILS') node.open = true;
  }
  function placeTarget(target, focus) {
    requestAnimationFrame(() => {
      if (!target.isConnected) return;
      target.scrollIntoView({block: 'start'});
      if (focus) {
        const control = one(':scope > .rf-step-toggle', target) || (target.tagName === 'DETAILS' ? one(':scope > summary', target) : target);
        if (!control.matches('button, a, summary')) control.setAttribute('tabindex', '-1');
        control.focus({preventScroll: true});
      }
    });
  }
  function initReader() {
    const controls = one('#rf-reader-controls');
    const sections = all('.rf-step, .rf-context', main).map(section => {
      const heading = one(':scope > h2', section);
      const body = one(':scope > .rf-step-body, :scope > .rf-context-body', section);
      return {section, heading, body, id: heading.id, title: heading.textContent, nodes: [...heading.childNodes], core: section.classList.contains('rf-step'), open: false};
    });
    const steps = sections.filter(item => item.core);
    if (!steps.length) { history.scrollRestoration = 'auto'; return null; }
    const byId = new Map(sections.map(item => [item.id, item]));
    let selected = steps[0].id;
    let targetId = selected;
    let detailSnapshot = null;
    let locationSeen = '';
    const details = () => all('details', main);
    function display() {
      const read = state.view === 'read';
      document.body.dataset.view = state.view;
      history.scrollRestoration = read ? 'auto' : 'manual';
      for (const item of sections) {
        if (read) item.heading.replaceChildren(...item.nodes);
        else {
          item.button.replaceChildren(...item.nodes, item.cue);
          item.heading.replaceChildren(item.button);
        }
        const open = read || item.open;
        item.body.hidden = !open;
        item.button.setAttribute('aria-expanded', String(open));
        item.cue.textContent = open ? '▾' : '▸';
        item.section.toggleAttribute('data-selected', item.core && item.id === selected);
      }
      all('[data-view-choice]', controls).forEach(button => button.setAttribute('aria-pressed', String(button.dataset.viewChoice === state.view)));
      all('.rf-step-actions', main).forEach(nav => { nav.hidden = read; });
      const target = document.getElementById(targetId);
      const optional = target?.closest('.rf-stretch, .rf-optional');
      all('#rf-outline a').forEach(link => {
        const anchor = decode(new URL(link.href).hash);
        const linkTarget = document.getElementById(anchor);
        const current = optional ? !!linkTarget?.closest('.rf-stretch, .rf-optional') : anchor === (target?.closest('.rf-context') ? target.closest('.rf-context').dataset.contextId : selected);
        if (current) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }
    function select(id, {scroll = false, focus = false, record = false} = {}) {
      const target = document.getElementById(id);
      if (!target) return;
      targetId = id;
      const owner = target.closest('.rf-step, .rf-context');
      const item = owner && byId.get(owner.dataset.stepId || owner.dataset.contextId);
      if (item?.core) {
        selected = item.id;
        steps.forEach(step => { step.open = step === item; });
        if (record) remember(item.id, true);
      } else if (item) item.open = true;
      else if (record && target.closest('.rf-stretch, .rf-optional')) remember(id, false);
      display();
      revealDetails(target);
      if (scroll) placeTarget(target, focus);
    }
    function historyState(anchor) { return {...history.state, rfReader: {page: data.page, anchor}}; }
    function navigate(id) {
      if (decode(location.hash) !== id) {
        const method = id === targetId ? 'replaceState' : 'pushState';
        history[method](historyState(id), '', '#' + encodeURIComponent(id));
      }
      locationSeen = location.href;
      select(id, {scroll: true, focus: true, record: true});
    }
    function fromLocation(initial) {
      const hasHash = location.hash.length > 1;
      const fragment = decode(location.hash);
      const explicit = hasHash && fragment && document.getElementById(fragment);
      const entry = history.state?.rfReader;
      const saved = !hasHash && (initial ? state.positions[data.page] : entry?.page === data.page ? entry.anchor : null);
      const id = explicit ? fragment : saved && byId.get(saved)?.core ? saved : steps[0].id;
      steps.forEach(item => { item.open = item.id === selected; });
      select(id, {scroll: !!explicit || !!saved || !initial});
      if (initial) history.replaceState(historyState(id), '', location.href);
      locationSeen = location.href;
    }
    try {
      for (const item of sections) {
        item.button = document.createElement('button');
        item.button.type = 'button';
        item.button.className = 'rf-step-toggle';
        item.button.setAttribute('aria-controls', item.body.id);
        item.cue = document.createElement('span');
        item.cue.className = 'rf-disclosure-cue';
        item.cue.setAttribute('aria-hidden', 'true');
        item.button.addEventListener('click', () => {
          if (!item.core) { item.open = !item.open; display(); return; }
          const close = selected === item.id && item.open;
          navigate(item.id);
          if (close) { item.open = false; display(); }
        });
      }
      steps.forEach((item, index) => {
        const nav = document.createElement('nav');
        nav.className = 'rf-step-actions';
        nav.setAttribute('aria-label', 'Adjacent sections');
        for (const [label, neighbor] of [['Previous', steps[index - 1]], ['Next', steps[index + 1]]]) {
          if (!neighbor) continue;
          const link = document.createElement('a');
          link.href = '#' + neighbor.id;
          link.textContent = `${label}: ${neighbor.title}`;
          nav.append(link);
        }
        item.body.append(nav);
      });
      fromLocation(true);
      function setView(view, persist) {
        if (view === 'read') {
          if (!detailSnapshot) detailSnapshot = details().map(detail => [detail, detail.open]);
          details().forEach(detail => { detail.open = true; });
        } else if (detailSnapshot) {
          detailSnapshot.forEach(([detail, open]) => { detail.open = open; });
          detailSnapshot = null;
          revealDetails(document.getElementById(targetId));
        }
        state.view = view;
        display();
        if (persist) save();
      }
      setView(state.view, false);
      all('[data-view-choice]', controls).forEach(button => button.addEventListener('click', () => setView(button.dataset.viewChoice, true)));
      function placeControls() {
        const slot = one(matchMedia('(min-width: 1280px)').matches ? '.rf-reader-desktop-slot' : '.rf-reader-mobile-slot');
        if (controls.parentElement !== slot) slot.append(controls);
      }
      placeControls();
      addEventListener('resize', placeControls);
      controls.hidden = false;
      document.addEventListener('click', event => {
        const link = event.target.closest('a[href]');
        if (!link || !plainClick(event) || link.target || link.hasAttribute('download')) return;
        const url = new URL(link.href);
        if (url.origin !== location.origin || url.pathname !== location.pathname || url.search !== location.search) return;
        const id = decode(url.hash);
        if (!id || id === 'main' || !document.getElementById(id)) return;
        event.preventDefault();
        navigate(id);
      });
      all('.rf-stretch > summary', main).forEach(summary => summary.addEventListener('click', event => {
        if (!plainClick(event)) return;
        const detail = summary.parentElement;
        event.preventDefault();
        if (detail.open) detail.open = false;
        else navigate(detail.id);
      }));
      function locationChanged() { if (locationSeen !== location.href) fromLocation(false); }
      addEventListener('hashchange', locationChanged);
      addEventListener('popstate', locationChanged);
      return {select};
    } catch (error) {
      sections.forEach(item => { item.heading.replaceChildren(...item.nodes); item.body.hidden = false; item.section.removeAttribute('data-selected'); });
      all('.rf-step-actions', main).forEach(nav => nav.remove());
      controls.hidden = true;
      delete document.body.dataset.view;
      history.scrollRestoration = 'auto';
      console.warn('Guided reading unavailable; the full document remains open.', error);
      return null;
    }
  }
  function initPrint() {
    let snapshot;
    addEventListener('beforeprint', () => {
      if (snapshot) return;
      printing = true;
      snapshot = {
        details: all('details', main).map(detail => [detail, detail.open]),
        bodies: all('.rf-step-body, .rf-context-body', main).map(body => [body, body.hidden]),
        buttons: all('.rf-step-toggle', main).map(button => [button, button.getAttribute('aria-expanded')])
      };
      snapshot.details.forEach(([detail]) => { detail.open = true; });
      snapshot.bodies.forEach(([body]) => { body.hidden = false; });
      snapshot.buttons.forEach(([button]) => button.setAttribute('aria-expanded', 'true'));
    });
    addEventListener('afterprint', () => {
      if (!snapshot) return;
      snapshot.details.forEach(([detail, open]) => { detail.open = open; });
      snapshot.bodies.forEach(([body, hidden]) => { body.hidden = hidden; });
      snapshot.buttons.forEach(([button, expanded]) => button.setAttribute('aria-expanded', expanded));
      snapshot = null;
      printing = false;
    });
  }
  function independently(initialize) {
    try { initialize(); } catch (error) { console.warn('A reading control is unavailable; ordinary course links remain usable.', error); }
  }
  load();
  [initTheme, initCopy, initCourse, initFigures, initSearch, initReset, renderHomeResume, initPrint].forEach(independently);
  const reader = initReader();
  one('.sc-skip-link').addEventListener('click', () => main.focus({preventScroll: true}));
  if (!reader) {
    const target = document.getElementById(decode(location.hash));
    if (target) { revealDetails(target); placeTarget(target, false); }
    addEventListener('hashchange', () => {
      const changed = document.getElementById(decode(location.hash));
      if (changed) { revealDetails(changed); placeTarget(changed, false); }
    });
  }
})();
