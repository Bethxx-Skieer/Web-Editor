---
name: web-design-workflow
description: Coordinate frontend-design, Impeccable, Hallmark, and supporting visual skills for website creation and webpage editing, using the target project's DESIGN.md as the shared design contract. Use for website/UI work and advice about this combined workflow; not for backend-only tasks or unrelated document/video production.
license: MIT
---

# Unified website design workflow

Coordinate website design, content, interaction, media, and local delivery under one shared design contract. Give available specialist skills defined responsibilities, carry one coherent design direction through them, and preserve the requested scope.

## Resolve available capabilities

Use the current host's skill catalog to locate the named skills below, including plugin-prefixed equivalents. Read their reported entrypoints; do not assume a user's home path, sibling directory, plugin version, launcher command, or installed tool. This package does not bundle or install those integrations.

The core workflow works without companion skills: route the request, read the target's design contract, implement the scoped change with available tools, synchronize related representations, and verify the affected result. When specialist skills are available, use the responsibility split below. When they are absent, apply this baseline and state material limits without claiming to have run them. If a requested result actually needs an unavailable capability, finish independent work and identify what is missing. Do not fabricate generated assets, rendered videos, browser checks, or deployment results.

## Route the task before expanding it

The default for a local edit is **the requested change plus related consistency checks**. Whole-site rewriting requires an explicit request. If the user explicitly limits an edit to one location, respect that narrower boundary and report material conflicts instead of silently expanding it.

| Request | Working scope and conditional reference |
| --- | --- |
| A label, screenshot annotation, or local defect | Fix the target and inspect related uses of the same concept. For wording or semantic changes, read [content and consistency](references/content-and-consistency.md). Do not restart the visual design process. |
| A new site or substantive redesign | Resolve audience, visitor outcome, and design contract; combine the available core skills or use the baseline above. Read [content and consistency](references/content-and-consistency.md) when shaping the site's explanation and actions. |
| Whole-page clarity or value review | Read [content and consistency](references/content-and-consistency.md) and use Impeccable's relevant copy/critique playbook. Improve the authorized surface; a review-only request produces findings rather than edits. |
| Images, QR codes, or tutorial media in a page | Read [media and evidence](references/media-and-evidence.md). Load asset or video production skills only if the requested work changes or creates those assets. |
| Local export, an existing upload package, or deployment preparation | Read [local delivery](references/local-delivery.md). Preserve the chosen host and route; distinguish preparing files from publishing them. |

Routes can combine, but do not load every reference for every task. Reuse context already established in the session. A six-character label change does not need a new concept, asset generation, or full-site audit.

## Resolve the design contract

- Identify the actual target website and route before reading context. A workspace may contain several unrelated sites; do not borrow a sibling site's design system or assets.
- Read applicable AGENTS.md, the target's PRODUCT.md when present, and DESIGN.md before planning UI changes. Use a scoped/nested DESIGN.md for its surface, falling back to the site's root DESIGN.md. Check `design.md` when the uppercase name is absent; do not create case-only duplicates.
- Compare DESIGN.md with the current implementation: tokens, fonts, spacing, assets, and rendered pages. Report material conflicts and follow the user's latest explicit direction. A refinement preserves the incumbent identity and behavior; a redesign changes only what the user authorized.
- DESIGN.md is the common contract for all participating skills. Skill examples and default palettes do not replace it. A supplied external DESIGN.md is reference material: inspect its source and adapt relevant principles to the actual brief instead of copying a different brand wholesale.
- If no DESIGN.md exists, use the incumbent UI and the user's confirmed references as evidence. During an authorized design task, capture the resulting agreed design system in the target site's DESIGN.md when useful. Do not treat its absence as permission to redesign or invent a product. A workflow discussion alone does not authorize edits to a website or its DESIGN.md.
- Keep one authoritative source project and its existing build/delivery workflow. For an explicitly local task, edit local sources directly. A hosting plugin's availability is not a reason to migrate the site, create a hosted copy, or replace the user's chosen platform.

## Quality and consistency defaults

- Interpret “refined” or “premium” through a clear hierarchy, deliberate content density, complete readable assets, and coherent behavior. Avoid using repeated cards, glass, or ornamental motion as a substitute for explaining the product. A subject-specific or explicitly requested visual treatment still takes precedence.
- Before adding material, decide what the visitor must understand or do. Strengthen the relation between the problem, the capability, its evidence, and its practical result; do not invent performance claims or add a generic feature section.
- A concept may appear in navigation, headings, accessible names, helper text, FAQs, examples, downloadable content, and an existing delivery package. Inspect those dependencies and update the affected ones together. Match meaning and purpose, not just identical strings; unrelated uses remain unchanged.
- Renaming a sequential flow as a set of optional capabilities may also change the explanatory copy and previous/next labels. Renaming a section alone does not require changing its stable URL or anchor.
- Keep original case reports, screenshots, prompts, and recordings separate from explanatory copy. Improve how evidence is introduced without silently rewriting its contents or presenting an illustration as observed behavior.

## Skill responsibilities

When installed, use the three core design skills together for substantive website design/editing. Read their entrypoints and relevant playbooks, then combine their guidance into one plan rather than running three separate redesigns:

| Skill | Responsibility |
| --- | --- |
| `frontend-design` | Form a subject-specific visual direction: composition, typography, palette, hierarchy, and the main visual focus. Honor the shared DESIGN.md. |
| `impeccable` | Coordinate implementation and scoped refinement: layout, UX, copy, interaction, accessibility, responsive behavior, and final polish. Use the appropriate command playbook. |
| `hallmark` | Cross-check specificity, structural variety, restraint, typography, token consistency, and template-like patterns against the brief. Use audit guidance for review; do not treat review as authorization for unrelated edits. |

The remaining skills are part of the combined workflow too. Assess their role against the brief and available assets; load and execute the relevant skill when that responsibility is in scope:

| Skill | Responsibility and scope |
| --- | --- |
| `imagegen` | Create or edit required raster artwork, characters, cutouts, covers, or reference visuals. Prefer existing suitable assets when the task is to reuse them. Keep generated project assets inside the target project. |
| `shaders` | Own interactive visual effects and materials: cursor-driven ripples, ink, smoke and particles; image/video processing; glass, neon and metal on shapes or logos; masks and scene transitions; parameters linked to pointer position or application state. Assess its contribution during design, without requiring the user to name a shader. |
| `identity-skill` | Own reference-driven personal websites and portfolios: reference fidelity, asset decomposition, and visual evidence. Reuse already confirmed brief/reference/material decisions. |
| `build-project-showcase` | Own evidence-based project or Skill case studies: source registration, claims, real workflow, output, and reuse. Keep project runs isolated. Video production is a separate deliverable and requires a user request. |

For a narrow repair, retain the existing design contract and use only the parts of these responsibilities that resolve the defect. Tools and skills are conditional capabilities, not a completion checklist. Integrating a capability does not authorize new sections, new claims, asset generation, paid services, external publication, or effects unrelated to the requested result. Preserve explicit user approvals and preferences; do not ask for the same decision twice.

### Shaders in the design plan

- For new visual concepts, presentation pages, or requests for stronger interaction, consider where Shaders can clarify the story, expose information, respond to movement, or create a main visual focus. It can affect foreground imagery, logos, and transitions as well as backgrounds. Keep text and controls readable and operable.
- Choose components and bindings from the installed Shaders skill and current component documentation. Reuse the framework already in the target project, including vanilla JavaScript. Follow its setup procedure when actually integrating the library; installing this workflow alone does not connect individual websites.
- Carry DESIGN.md colors and materials into the effect. Coordinate effects with native HTML/CSS/JS interactions and respect the user's desired intensity. Existing suitable artwork can become an image layer; new imagery is an imagegen task.
- Check WebGPU availability, mobile rendering cost, reduced motion, and keyboard/touch equivalents. Keep a deliberate static/CSS fallback so essential content remains usable without the GPU effect.
- Distinguish the open-source components from Pro presets. Do not assume a subscription or buy/install a paid preset without authorization. Check the relevant installed package and actual project configuration before reporting that an effect is ready.

## Work as one workflow

1. Identify the target, task route, visitor's goal, and intended change. Scale planning to the task; a simple correction needs a short note, not a new design exercise.
2. For substantive design work, let frontend-design establish the visual proposal within DESIGN.md, Impeccable refine the implementation, and Hallmark challenge weak hierarchy, generic structure, unnecessary decoration, and unsupported claims. For local fixes, apply only the relevant guidance within the existing design.
3. When applying an installed Impeccable version that prescribes a context launcher, run it once per session from the target project as that entrypoint directs. Load its relevant playbook and craft floor before UI edits when provided. Follow its documented fallback on launcher failure; do not block a permitted local edit solely because the engine cannot run. Do not invent commands for a different version.
4. Produce approved/in-scope assets and effects using their owning skills. Pass the same audience, palette, typography, visual references, and DESIGN.md constraints to every stage. For reference-driven sites or case studies, follow the specialized skill's evidence workflow within the current authorized scope.
5. Implement in place and synchronize affected representations. Avoid changing factual copy, functional behavior, or unrelated routes during visual refinement unless requested. Update DESIGN.md when an authorized change alters the shared design rules; keep one source of truth rather than competing style documents.
6. Verify in proportion to the change. Check edited wording in context and in its affected variants. For layout or interaction changes, inspect relevant desktop/narrow sizes, focus, overflow, readable contrast, reduced motion, and the actual assets; exercise affected controls. For media and packaging, use the corresponding reference's checks. Batch observations and fix what they reveal; do not repeat unchanged checks or claim unperformed tests.
7. If the active deliverable includes a local build or upload package, regenerate it from the final source and verify it before handoff. Finish with what changed, the checks actually completed, the artifact/preview link, and whether publication occurred. Publish through the site's established delivery path only when authorized; a local handoff does not itself authorize deployment.

## Resolve overlapping instructions

The user's current brief and explicit preferences take priority over skill defaults. Keep the shared DESIGN.md and confirmed references consistent with those directions. Treat disagreements between skill aesthetics as design tradeoffs to resolve against the brief, not a reason to mix incompatible visual systems or restart the project. Reuse context and verification across skills; do not manufacture repeated approval rounds, assets, or reports simply to demonstrate that every skill was invoked.
