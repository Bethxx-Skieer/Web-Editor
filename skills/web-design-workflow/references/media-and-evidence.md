# Media integration and readable evidence

Read this when a website task touches images, QR codes, recordings, or explanatory video. Embedding an existing asset does not itself request new asset production.

## Route to the appropriate owner

Keep the site's visual contract and the existing media project. When actual image generation/editing or video production is requested, use the available owning skill and tool instructions. For video creation or editing, read the available HyperFrames entry point first; honor an explicitly chosen framework and an established Remotion project, using the relevant Remotion skills for that work. Do not migrate a composition solely because another engine is available.

A request to fix a player concerns the player. A request to make a video more explanatory concerns its composition and pacing. Do not substitute extra webpage control panels for an improved video, or rerender an unchanged video to fix a page layout issue.

## Preserve useful image information

- Decide whether an image is decoration, illustration, or evidence before choosing its crop. Preserve the full relevant area of tutorial screenshots, report figures, and QR codes. Decorative photography can be cropped when that serves the composition.
- Preserve aspect ratio and inspect actual rendered text sizes. A complete screenshot shrunk beyond readability is not a successful integration; offer a readable detail or full-size view when needed.
- Reuse confirmed logos and supplied evidence. Generated imagery may explain a concept, but must not impersonate a real screenshot, product result, or customer outcome.
- Follow the user's transparency request without introducing an opaque image rectangle through the asset, wrapper, or export. Inspect the actual file as well as CSS; a white patch may be baked into the bitmap.
- Avoid captions that only announce the existence of an illustration. Retain useful source context and descriptive alt text even when the user removes a visible decorative caption.

## Keep QR codes functional

Use the original QR asset as data, not as a prompt for a generated approximation. Keep its modules, aspect ratio, edge definition, and necessary clear area intact. Prefer a separate image layer in the page or composition so artwork and resizing cannot redraw it.

Scale the code to a comfortable visual size alongside the call to action. Verify it at the actual display/export size with a decoder or an actual scan when available, and compare the decoded destination with the source. Check both visual fit and scan reliability: transparent backgrounds or matching colors must still provide sufficient contrast and an unobstructed clear area. If the requested background treatment makes scanning unreliable, use the smallest compatible adjustment and explain the tradeoff rather than hiding the problem. Do not claim a scan test that was not performed.

## Use a normal player for a normal tutorial

Default to native video controls with inline playback unless the task establishes a need for custom playback UI. Avoid extra chapter dashboards, speed bars, overlays, autoplay loops, or competing controls just to make the page look richer.

Verify play/pause, seeking, native speed options where supported, and fullscreen behavior in the target browser. Check that overlays do not intercept interaction and that layout changes or rerenders do not repeatedly reset playback. Use the actual media URL and metadata to check load failures. Seekability may depend on the served media and HTTP range support; inspect those before adding custom controls. Provide an actionable load-error message without pretending to know an unverified cause.

Do not add a custom speed selector solely because one browser lacks a native speed menu. If speed control is a requirement and the target browser cannot provide it, choose the smallest functional addition consistent with the user's preference.

## Improve the recording itself when requested

Build the explanation around the viewer's goal, the real operation, its critical detail, and the observable result. This is an editing guide, not a fixed four-scene template. Identify the evidence the viewer must be able to inspect before choosing effects.

- Introduce the business or user objective before mechanical inputs such as a batch of questions.
- Preserve the actual order of prerequisite actions when it explains success: opening the relevant app, checking sign-in, starting a new operation, supplying input, waiting for completion, and collecting the output.
- Keep decisive UI visible at the right time. Examples include the actual copy control, a citation entry, its expanded list, a save confirmation, or the exported field corresponding to the action.
- Use the original footage's stable framing as the baseline. Zoom only to reveal a necessary detail, preserve orientation, and allow time to read it. Avoid continuous scale pumping, abrupt reframing, and repeated transitions that interrupt an operation.
- Cut or accelerate genuine waiting where it aids comprehension, without implying instant execution. Keep relevant cursor actions and text inspection readable. Preserve natural motion through meaningful actions; do not mask stutter with more effects.
- Let annotations, diagrams, captions, or transitions explain a relationship or draw attention to evidence. Match the site's visual language without covering controls or regenerating product UI.
- If a frozen detail, reconstruction, or test input is used, make its role clear. Do not present a different test question as proof of the claimed business result.

Inspect the exported video, not only storyboard frames or the composition preview. Review transitions, the reported problem interval, key UI actions, text readability, duration, and successful playback. Also verify that the page references the intended final video and matching poster.

## Remove obsolete promises consistently

When the user cancels a video, remove its affected placeholder, “recording coming soon” status, FAQ promise, and related handoff instructions. Keep a useful static explanation when it already serves the page. Update durations, posters, and descriptions when the video changes. Preserve original media files unless deletion is separately requested; package cleanup and source deletion are different operations.
