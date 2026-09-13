# Parts, local generation and face alignment

Use when choosing between an existing character, a segmented asset and independent
regional generation, or diagnosing facial texture misalignment. The maintained
[CosMMD investigation](https://github.com/CyclopsRay/CosMMD/blob/main/docs/part-pipeline.md)
records the inspected example, primary sources and proposed interfaces. Its new
provider adapters and cloth stages are not implemented CLI commands.

- Preserve a whole-character reference for proportions, rest pose and material
  comparison. Prefer semantic parts in that common space and one fitted skeleton.
  Distinguish raw cropping from editing dedicated regional reference images using
  the same T pose. Both need explicit 3D proportion, pose and attachment constraints;
  image conditioning alone does not ensure assembly. Test one real joint first.
- For regional references, define target landmarks, attachment frames/cross-sections
  and overlapping context before generation. Keep annotated inspection images separate
  from clean model inputs. Recheck landmarks after editing; a crop transform need not
  remain valid after generative changes. Resolve the actual image-model ID before calls.
- Assemble with similarity transforms, then deform only connection bands while
  protecting faces, prints, hands and shoes. Bridge continuous skin where appropriate;
  retain clothing/hair layers and legitimate overlaps. Check seam geometry, materials
  and skinning under motion. Define a target rest skeleton early, but fit final skinning
  after assembly; do not independently auto-rig fragments into incompatible rest poses.
- Export the actual asset and inspect UVs, materials, transform hierarchy and topology.
  A web exploded view need not be baked into the file. A newly segmented asset need
  not have the same vertices as the old source. Compare after alignment before
  claiming damage or preservation; changed hashes alone do not measure visible loss.
- Reuse a tested skeleton and motion only after fitting the new surface. Changed
  topology invalidates vertex-index weight copies and deformation bindings. Transfer
  through aligned, semantically restricted correspondence and validate limbs again.
- Treat appearance regions, garment structure and physics proxies separately.
  Sock color bands should not automatically become independent cloth rings. Multiple
  visible skirt parts may share one continuous proxy while retaining their own UVs.
  Open boundaries may be legitimate; splitting cannot create hidden body or lining.
- For doubled facial features, compare the same static mesh/camera with original
  materials, a clay override and base-color-only emission. If texture and geometry
  disagree before rigging, repair their alignment first. Compare each to the reviewed
  T pose; choose local UV/reprojection, geometry fitting or retexturing accordingly.
  Check side views and seams. Disabling lighting only hides some symptoms.
- Tripo exposes geometry-prioritized texturing and part selection; verify current
  official contracts and output geometry before a bounded trial. Its direct
  `generate_parts` option conflicts with textured/PBR generation, so do not silently
  add it to the existing payload. Task spending and ambiguous retries follow the
  existing [Tripo operations](tripo.md) guidance.
- Test a face and one garment region against the current dance before wholesale
  migration. Save source versions, mappings, assumptions and comparison renders
  privately. Publish only verified capabilities and explicitly reviewed assets.
