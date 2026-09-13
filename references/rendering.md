# Render diagnosis and delivery

The reference pipeline produced a correctly encoded 12-second MP4 but rendered the
character as a black silhouette at video frames 41–56. Background/floor stayed lit.
The same defect existed in PNG masters. Inner-shoe and thigh patches were also pure
black. Freshly reloading the identical scene and using the original settings fixed
both without modifying geometry. The exact internal renderer cause was not isolated.

Use `--python-exit-code 1` for background scripts so Python failures stop the pipeline. Verify that the expected artifact was actually written. Blender uses its own Python; add-on dependencies may need an explicit local path.

Use this sequence to distinguish failures:

1. Locate the exact video frame/time range. Check all frames, not only four snapshots.
2. Compare decoded frames with PNG masters. If masters already contain the defect,
   changing the encoder is not the repair.
3. Rerender the same frame/model/settings after a fresh scene load. Only then vary CPU/GPU,
   persistent data, motion blur or denoising, one factor at a time when needed.
4. If the fresh result is correct, regenerate affected output through an isolated render
   path. Do not change shoes, normals or textures merely because a black patch resembles a hole.
5. Keep motion and its timestamps intact; do not delete bad frames or replace them with
   neighboring poses to hide the failure.

CosMMD defaults to a fresh Blender process per frame, persistent data off and CPU
 denoising. This trades startup time for isolation. Keep checkpoints and PNG masters;
resume only when the scene/settings signature matches. Use a few small render checks
before a long run. Honor the user's requested monitoring interval; do not create a
scheduled monitor unless monitoring or follow-up is requested.

Output QA: exact dimensions, frame count, frame range, effective fps and duration;
full contact sheets; numerical black-frame/silhouette flags; visual hands/shoes/face/
hair/skirt review; and actual encoded playback/decoded checks. Heuristics can flag
legitimate dark costumes, and cannot prove all visuals are correct.

Already graded PNGs should not receive AgX again in VSE. Use Standard/None/exposure 0
for assembly. Preserve source 30 fps motion; a GIF can sample every second frame and
use a 60/70 ms duration pattern to represent 15 fps without shortening the clip.
Do not describe silent GIFs as synchronized music videos or claim facial/cloth features
that are absent. Display the actual local artifact and clearly label remaining issues.
