# digimeister-website

The Digimeister studio site: one static page, no build step. `public/` is the site root.

- `public/index.html`: the page. The logo SVGs are inlined from `digimeister-brand/` as they are; never edit their paths.
- `public/style.css`: site styles. Colours and type come from `public/brand-tokens.css` (a copy of `digimeister-brand/tokens/brand-tokens.css`).
- `public/fonts/`: self-hosted Rubik and Inter (SIL Open Font License).
- Favicons, touch icon, manifest and share image sit at the root of `public/`, as `digimeister-brand/HANDOFF.md` asks.
- `public/media/moonrangers/`: the gameplay video and stills, copied from playmoonrangers.com and re-encoded
  (video: H.264, 30 fps, no audio, CRF 28, faststart; stills: 1600 and 800 wide). They don't update with that site.

## Placeholders to replace

- **Team portraits:** replace each `span.person__portrait` (the initials) with `<img class="person__portrait" src="team/name.jpg" alt="" width="160" height="160">`.

## Run it locally

```
cd public && python3 -m http.server 8000
```

The brand rules (colours, contrast, logo use) are in `digimeister-brand/HANDOFF.md`.
