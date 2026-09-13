---
name: 2d-cosplayer-to-mmd
description: Turn one full-body character or cosplay image into an appearance-preserving Tripo/Blender character with an articulated rig and licensed MMD motion. Use for single-image character-to-MMD work, rig repair, retargeting, render diagnosis, or packaging the resulting workflow. Works with the CosMMD toolkit; geometry-specific calibration is agent-guided.
---

# 2D Cosplayer to MMD

Create an editable, recognizably faithful 3D character and a verified dance clip from
one character image. Use [CosMMD](https://github.com/CyclopsRay/CosMMD) for deterministic
API, inspection, rig, rendering and publication helpers. This is an agent-guided
workflow, not a guarantee of one-click success on arbitrary images.

## Inputs and scope

- One full-body image, ideally a clear T/A pose with hands and shoes visible. Do not
  require a second face image or multiview set unless the user changes the task.
- A Tripo API key through local environment/credential storage; never repeat it in
  output, scripts, screenshots, repository files or saved command examples.
- A locally available motion with applicable permission. The motion is an external
  reusable asset, not character evidence extracted from the image.
- Blender and a compatible, separately installed MMD Tools for VMD import. Final
  native Blender scenes should be validated without that add-on where practical.

Honor existing choices, permissions and spending limits. Reuse available author
permission within its scope. Do not buy credits, automatically regenerate repeatedly,
substitute another paid service, or publish assets merely because a key is available.

## Work in explicit stages

1. **Preserve and generate/reuse.** Create a private run directory outside tracked
   source. Keep original image/source GLB unchanged. Inspect existing Studio exports
   if requested; a Studio ID is not necessarily an API task ID. Use checkpointed tasks,
   download successful outputs promptly, and stop ambiguous POST retries.
   Read [Tripo operations](references/tripo.md) for API/version/resume decisions.
2. **Inspect the original surface.** Examine front, side and oblique views, connected
   topology, UVs, materials, real finger gaps, actual shoe shape and hidden anatomy.
   Do not infer fused fingers from one view or low-resolution proxies.
3. **Preserve identity while rigging.** Transfer weights onto the original surface.
   Fit joints to anatomy, directly bind existing fingers, preserve cuff ornaments,
   and change geometry only where a verified fused/missing region requires it.
   Read [rigging decisions](references/rigging.md) before modifying limbs or topology.
4. **Calibrate and import.** Match MMD neutral rest axes before importing relative
   rotations. Map bones and scale explicitly. Use the user's licensed VMD. Check IK
   toggles, knee seeds, finger channels and full animation range after import.
5. **Validate motion.** Test independent limbs and fingers, all-frame finite bone
   transforms, hinge direction, weights, drivers and reach-aware IK. Inspect deformed
   shoes against the floor, camera framing, crouches, lifts, turns and hair/skirt behavior.
6. **Render and verify.** Start with small renders. Use independent fresh Blender
   processes per frame for the known failure-prone pipeline; keep PNG masters and
   resumable progress. Read [render checks](references/rendering.md). Scan every frame,
   review contact sheets and decode/play the actual final file. Do not call a file
   complete just because it exists and reports the expected resolution/frame count.
7. **Deliver.** Show the actual result and links to the editable rig/dance/video with
   remaining limitations and credits. Publish only when requested. Read
   [publication boundaries](references/publication.md) before any public release.

## Essential invariants

- Anatomical left/right belongs to the character, not the camera view. Verify each
  leg's weights and target independently; do not solve it by guessing a name swap.
- Existing hand/foot/costume geometry and UVs are the visual ground truth. Reconstruction
  is a local repair option after evidence, not the default cure for poor auto-rigging.
- An image-derived clothed surface may lack hidden thighs/body. Splitting cannot
  recover absent geometry. Identify what exists before capping or adding surfaces.
- Neutral-pose calibration changes mesh and rest bones together on a copy. Renaming
  bones alone does not fix T-pose versus MMD arm orientation.
- Preferred knee bend, hinge sign, cut planes, finger landmarks and hair/skirt masks
  are model-specific. The example's 25° bend and coordinates are not universal constants.
- Hair/skirt bone following is not cloth physics. A Blender MMD animation is not a
  verified PMX export. Say what was actually implemented.
- Black character silhouettes or shoe patches may be rendering-state artifacts.
  Compare raw PNGs, then rerender the same model/settings from a freshly loaded scene
  before modifying geometry. State uncertainty about the underlying engine subsystem.

## Use the toolkit

The companion repository documents installation and actual commands. Its `generate`
command is a no-cost plan until `--execute`; task journals prevent blind resubmission.
`inspect` reports source topology/bones. `blender/rig_ops.py` provides reusable
appearance-preserving operations. `recipes/reference_character/` contains the fitted
case, which must be adapted for another character. `render`, `qa` and `cosmmd.gif`
produce and inspect real renders. `audit` scans staged content and history.

Do not claim the whole pipeline has been rerun if only offline tests or existing
Studio exports were used. Record the source path, provider route, software versions,
manual calibration and evidence for the delivered result in local reports.
