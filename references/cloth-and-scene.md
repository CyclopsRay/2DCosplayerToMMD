# Cloth, lighting and scene extensions

Read this when the user asks to plan or implement cloth physics, photo-matched
lighting or scene reconstruction. The existing CosMMD showcase has no cloth
simulation. New stages are proposals until implemented and verified.

The maintained contracts, technology choices, milestones and acceptance criteria
live in [CosMMD's technical roadmap](https://github.com/CyclopsRay/CosMMD/blob/main/docs/technical-roadmap.md).
Use its current implementation status; do not invent CLI commands from stage names.
Before choosing an existing segmented asset or generating regions independently,
read [part-pipeline decisions](parts.md). A material boundary is not necessarily a
sewing line, and a visible part is not automatically a simulation-ready garment.

- Keep the original photo for room/camera/light evidence. The generated T pose is
  for character modeling and cannot preserve source-image pixel correspondence.
- Preserve the visible clothing and UVs. A separate simulation proxy can drive it
  through Surface Deform. Inspect actual 3D connectivity before splitting; a 2D
  segmentation mask does not supply missing cloth/body surfaces or sewing patterns.
- Separate visual material settings from dynamics. Start with one garment region;
  retain support for structured skirts and define attachment behavior for decorations.
- Settle body animation and animated colliders before baking cloth. Validate pinning,
  modifier order and absence of double deformation where proxy and skeleton overlap.
- Bake sequentially with validated preroll at motion fps. Fresh-process rendering
  must read a verified persistent cache, not initialize physics at each sampled frame.
  Check random-frame geometry against sequential evaluation. Cache/texture hashes
  need to participate in rendering resume signatures; current signatures are insufficient.
- Establish camera/floor/lighting before a full room. A single photograph supports
  an approximate visible reconstruction; label hidden geometry and scale assumptions.
- Keep optional ML environments outside Blender. Local masks/labels are a valid
  fallback; do not add an unrequested required API service or assume Mac support from CUDA examples.

For a planning request, deliver a plan. For implementation, follow the authorized
scope and update the capability/evidence documentation only after validation.
Retain existing author permission within its scope; physical caches and animated
scenes remain derivative animation assets subject to the publication rules.
