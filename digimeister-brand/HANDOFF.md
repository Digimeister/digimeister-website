# Digimeister brand: website handoff

The final logo system for building the Digimeister website. Everything here comes from the master geometry. Use the files as they are and never redraw or edit the paths.

## 1. The logo in one paragraph

The mark is **two handheld consoles joined by a cable**: Ink bodies, Paper screens, a Signal-yellow cable and plugs. The two consoles always appear as a **pair**. Never crop, isolate or animate one console on its own, and that includes the favicon and app icon. The wordmark **DIGIMEISTER** is set in **Rubik 800**, uppercase.

## 2. Colours

| Token | Hex | Use |
|---|---|---|
| Ink | `#15171A` | logo bodies, text, primary buttons, dark surfaces |
| Paper | `#F6F5F2` | page background, logo screens, text on dark |
| Signal | `#FFC01E` | cable and plugs, accents, underlines, focus rings, fills behind Ink text |
| Surface | `#FBFAF8` | cards and header on Paper |
| Line | `#DDDBD5` | borders |
| Muted | `#6B6E73` | secondary text on Paper (4.7:1) |
| Muted on dark | `#A9ACB2` | secondary text on Ink (7.9:1) |
| Signal text | `#8A6A12` | only if gold *text* is needed on Paper (4.6:1) |
| Port Blue (optional) | `#4789FF` / text `#2563D9` | links or UI blue if needed. Not part of the logo |

**Contrast rules.** Signal is 1.5:1 on Paper, so **never use Signal as text or thin lines on light backgrounds**. Use it as a fill (Ink text on Signal is 11:1), an underline, or text on Ink. For an active nav item, use Ink text with a 2 px Signal underline.

Ready-made tokens: `tokens/brand-tokens.css` (CSS custom properties) and `tokens/brand-tokens.json`.

## 3. Type

- **Rubik 800**: wordmark and headings. **Rubik 500**: uppercase slogans and labels (tracking 0.22em).
- **Inter 400/500/600**: body, navigation, UI. Nav style: 12 px, 600, uppercase, tracking 0.12em.
- Load both: `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Rubik:wght@500;800&family=Inter:wght@400;500;600&display=swap">`

## 4. Which file where

| Need | File |
|---|---|
| Site header / footer logo (inline) | `web/lockups/digimeister-lockup-horizontal-small.svg` (36 px header, 32 px footer) |
| Large hero / about-page lockup | `web/lockups/digimeister-lockup-horizontal.svg` |
| Stacked (splash, end cards) | `web/lockups/digimeister-lockup-stacked.svg` |
| Mark without wordmark, themable | `logo/svg/web/digimeister-mark-live.svg` (≥ 48 px), `…-mark-small-live.svg` (20–47 px) |
| Mark as a plain image (`<img>`) | `logo/svg/mark/*.svg` (≥ 48 px), `logo/svg/mark-small/*.svg` (20–47 px) |
| Favicon, touch icon, PWA | `web/icons/*`: see section 6 |
| Social share image | `web/icons/og-image.png` (1200×630), `og-image-dark.png` |
| Rasters | `logo/png/…` |
| Working example | `web/reference.html`: header, hero, Signal band, footer, wired to the tokens |

**Important: the lockups use live text.** The `web/lockups/*.svg` files set DIGIMEISTER as `<text>` in Rubik 800. They render correctly only when the SVG is **inlined in the HTML** of a page that loads Rubik. Used as `<img src>` or a CSS background, the font won't load and the browser falls back. Outlined lockup files will follow once the Rubik font file is supplied. Until then, inline the SVGs. The mark-only files have no text and work anywhere.

## 5. Theming the inline SVGs

The live SVGs use classes driven by three CSS variables: `--ink`, `--paper` and `--cable`.

```html
<style>
  .dm-logo .ink{fill:var(--ink)} .dm-logo .pap{fill:var(--paper)}
  .dm-logo .paps{stroke:var(--paper)} .dm-logo .inks{stroke:var(--ink)}
  .dm-logo .cab{stroke:var(--cable)} .dm-logo .cabf{fill:var(--cable)}
</style>
<a href="/" aria-label="Digimeister home">
  <svg class="dm-logo" viewBox="…from the file…" style="height:36px;width:auto">…paste the file's inner markup…</svg>
</a>
```

- **Light (default):** `--ink:#15171A; --paper:#F6F5F2; --cable:#FFC01E`
- **Dark surface** (`.dm-dark` in the tokens): swap ink and paper. The cable stays Signal.
- **On a Signal field** (`.dm-on-signal`): `--ink:#15171A; --paper:#FFC01E; --cable:#15171A`. The cable turns Ink so it doesn't vanish.
- When inlining several SVGs on one page, drop the `<style>` block inside each file and keep one copy of the class rules in the page CSS, as in `reference.html`.
- Never recolour parts individually, add gradients, shadows or outlines, rotate, stretch, or animate the consoles apart.

## 6. Favicons and app icons

Put the contents of `web/icons/` at the site root:

```html
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#F6F5F2">
<meta property="og:image" content="/og-image.png">
```

`favicon.svg` follows the browser's light or dark setting by itself. The icon is the pair, pulled together to fill a square.

## 7. Size and space rules

- **Clear space:** keep 10% of the mark's width (52 of its 520 units) free on all sides. On a 36 px-tall header lockup that is about 7.5 px, so a normal header padding covers it.
- **Small build:** the files marked `small` have heavier details for small sizes. Use them below 48 px tall for the mark and below 96 px for the icon. Below 48 px, wordmark tracking goes to 0.05em (already set in the small lockup).
- **Minimums:** mark 20 px · horizontal lockup 24 px tall · stacked lockup 84 px tall · icon 16 px. Below 20 px, use the icon.
- On photos or busy backgrounds, put the logo on a solid Paper, Ink or Signal panel.

## 8. Not decided here

The tagline, contact details and page copy in the design boards and `reference.html` are placeholders. Get the real copy from the client. Layout, page structure and imagery are up to the website design.
