# Local sources and deployment-ready packages

Read this for local exports, existing upload packages, route migration, or deployment preparation. Preparing a package and publishing a website are separate actions.

## Establish the source and destination

Identify the authoritative source project, preview/build output, deployment root, mount path, and requested archive. Use the existing build or packaging workflow when available. Edit the source and regenerate derived files rather than fixing only an exported copy that the next build will overwrite.

If the exported HTML is the only available source, treat that as the explicit working source instead of inventing an unavailable upstream project. Do not force an HTML export onto a site that needs a framework build or server runtime; preserve its actual deployment requirements.

Honor the chosen host and local workflow. Installing or discovering a website plugin is not permission to switch hosting. Do not ask again about a confirmed root-versus-subdirectory choice. If that choice is still ambiguous and affects existing content, inspect the project before asking.

## Verify the intended route

Test at the intended mount path, including direct navigation and a reload of the relevant deep link. Check image, stylesheet, script, font, video, poster, report, and downloadable-document URLs, including dynamically constructed references.

Choose relative URLs or a framework base-path setting according to the project; do not blindly rewrite every URL. Root-relative paths can accidentally target the host's other site, while nested routes may need a framework's routing behavior. Check anchors and generated download links as well as initial page load.

Preserve existing redirects, headers, functions, and server/worker configuration. Resolve collisions with an existing route before replacing it. Test through a local server when file URLs cannot exercise module loading, fetches, clipboard APIs, or video seeking reliably.

## Distinguish a complete deployment from an addition

| Deliverable | Meaning and handoff |
| --- | --- |
| Complete deployment | Contains the final deployable site, including existing routes that must remain available. Use the established build and publishing process. |
| Incremental addition | Contains only the new or updated subtree. Label it as an addition and explain where it must be merged into the complete deployment. |

For snapshot-style static hosting, uploading an addition alone can replace the visible deployment with only those files. Inspect the target platform's current behavior instead of assuming an upload appends to the existing site. If the existing site's full source/output is unavailable, provide the addition and merge instructions; do not claim that existing pages have already been preserved in a complete package.

An archive must have the intended directory structure, with no accidental extra wrapper directory. A subdirectory addition normally retains that named subtree. Do not invent a new domain, production branch, or build command when the current project already defines them.

## Build a clean, current package

- Include required runtime resources and applicable asset licenses, including files referenced from scripts or configuration. Exclude unused older videos, temporary previews, development dependencies, secrets, and hosting account metadata. Keep original assets in the source project unless their deletion was requested.
- Use the existing packaging script or build pipeline. Avoid adding a bespoke exporter for a one-off task unless it materially improves reliability; framework-specific runtime dependencies may not be discoverable with a simple HTML-link scan.
- When an active handoff package already exists, rebuild it after the final authorized edit. Check for stale files in the staging directory; do not blindly copy over it and assume removed references disappear. Clean only verified generated-output paths, preserving unrelated files.
- Check current platform constraints relevant to the deliverable, such as per-file size, upload format, route behavior, and build mode. Do not encode volatile service limits into this reusable skill.
- Inspect the archive's entries, test its integrity, and compare its contents with the final intended output using a manifest, hashes, or equivalent verification. Check that the latest HTML, scripts, poster, and video are the versions being delivered.

## Validate and hand off

Verify relevant local paths and representative page behavior at the mount path. For video, include media loading and seeking checks when affected. Confirm image/font loading, navigation, copy/download interactions, and changed labels in proportion to the work. An HTTP 200 or a successful build alone does not prove the page displays or behaves correctly.

Report the source or output location, the checks actually performed, the package link, and whether it is complete or incremental. State whether deployment occurred. For an addition, explain the merge step needed to retain existing content. If authorized publication is part of the task, use the established deployment path and verify the deployed result; otherwise finish with the local handoff without creating a hosted copy.
