# Rigging and retargeting decisions

## Preserve the actual character

Keep a pristine high-resolution source. A lower-resolution proxy can provide weights,
but do not deliver its simplified hands/shoes as an unnoticed visual replacement.
Use weight transfer and compare equal-scale, equal-pose, equal-light images. Verify
unchanged external vertex coordinates and UVs where that is the intent.

Inspect finger gaps through topology and multiple viewpoints. If fingers already
exist, fit four points per finger and create three bones; keep thumb indexing distinct.
Bind skin locally, retain cuff ornaments with the wrist, blend joints, and smooth over
mesh connectivity. Test open hands, a fist and isolated finger curls. Neighbor tips
must not move just because another finger is bent.

For fused leg interiors, isolate the actual connection, preserve external faces/UVs,
and fill only newly exposed or genuinely missing surfaces. Check material attributes
on new faces. Do not rebuild complete boots or shoes just to separate legs. A dressed
surface can have no real upper thigh under the garment; add that region locally when
needed and disclose it. Inspect the seam in oblique and lifted-leg views.

## Anatomical calibration

Find shoulders, elbows, wrists, hips, knees, ankles and toe pivots in the mesh. Validate
parenting and twist helpers. Left/right is anatomical, independent of the camera.
Sleeve weights should follow the elbow/wrist correctly; skirt weights must not be
pulled down by calf or thigh influence.

MMD rotations assume a rest basis. Calibrate the neutral T/A pose on a copy and bake
the corresponding mesh deformation and bone rest pose together. Bone-name mapping
alone is insufficient. Scale motion translations using the model's chosen unit scale.
Do not copy a third-party reference model's full skeleton data into the public repo.

## Knees and reach

Choose the actual bend axis/sign. For the fitted case, a one-axis hinge with a 150°
upper bend limit and 25° preferred bend was more stable than the tested pole setup.
A 10° seed did not solve every pose. These numbers need re-evaluation per character.
Check whether VMD identity rotations overwrite the seed. Preserve genuine animation
and IK-off sections; do not indiscriminately delete knee rotation tracks.

Validate the opposite leg remains stationary during a one-leg test. Distinguish raw
ankle-target error from error caused by a target beyond leg length or the minimum
reach imposed by bend limits. Inspect all frames for non-finite transforms and reversed
knees. Test floor clearance using deformed shoe vertices, not only foot bones.

## Hair, clothes, and deliverables

Hair/skirt masks based only on color or height are case-specific approximations. They
can mix hair with sleeves and pull skirts through thighs. Use geometry/UV/material
cues and review difficult poses. Light baked bone follow-through is acceptable when
requested, but is not cloth or strand simulation. Preserve unresolved defects in the
handoff notes instead of silently rebuilding another part of the character.
