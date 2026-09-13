# Tripo operations

Use the current official API documentation for the selected version:
[image preparation](https://developers.tripo3d.ai/en/docs/generation-image-to-image),
[3D generation](https://developers.tripo3d.ai/en/docs/generation-image-to-model/standard),
[upload](https://developers.tripo3d.ai/en/docs/files),
[rig check](https://developers.tripo3d.ai/en/docs/animations-rig-check),
[rig](https://developers.tripo3d.ai/en/docs/animations-rig),
[tasks](https://developers.tripo3d.ai/en/docs/task-query).
CosMMD's adapter consistently uses v3. Do not mix v2 `type/model_version/file` payloads
with v3 `input/model` endpoints.

A good path is original photo upload → image-to-image (`model: banana_pro`,
`template: t_pose`, default `size: 2K`, `aspect_ratio: 1:1`) → poll/download the
`output.generated_image_url` as `t_pose.png` → compare with original → upload the
reviewed T pose → image-to-model → poll/download source → rig-check → humanoid rig
→ poll/download rigged GLB. Use `cosmmd prepare`, then `cosmmd generate` with the
prepared PNG. Read the [full guide](https://github.com/CyclopsRay/CosMMD/blob/main/docs/photo-to-tpose.md).

The old v2 model name is `gemini_3_pro_image_preview` under `model_version`; do not
pass that name into the v3 `model` field. Do not use text-to-image when the photo
must condition the result. Both stages use the same Tripo key; no second image-service
credential is required. Review the prepared face, hands, costume asymmetry and shoes.
Keep original/prepared hashes, prompt and image task ID in private provenance records.
Existing T-pose references can skip this preparation task. API rigging does not establish MMD readiness.
Preserve task IDs before proceeding and immediately store downloaded source assets locally.
Do not send API Authorization headers to CDN download hosts or log signed URLs.

The original Studio asset returned 404 when queried through the API. That does not
prove every Studio model is inaccessible. Inspect what the user has; use an authorized
manual export/re-upload when needed. Studio/API credits and identifiers must not be
assumed interchangeable.

A timed-out POST may have created a paid task. Use the local journal and provider
console to recover its ID. Do not create another task to see whether the first one
worked. Retry bounded reads separately from mutations; honor existing cost authorization.
Do not expose provider account IDs or responses in a public case study.
