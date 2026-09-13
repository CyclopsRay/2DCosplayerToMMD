<div align="center">

# 2DCosplayerToMMD

### One photo. Nano Banana Pro T pose. A dancing 3D character.
### 把“原图 → Nano Banana Pro T pose → 3D → MMD”变成可复用的技能。

<img src="https://raw.githubusercontent.com/CyclopsRay/CosMMD/main/docs/media/hero.gif?v=photo-tpose-2" width="1440" alt="CosMMD original photo, prepared T pose and twelve-second dance demonstration">

**The agent skill behind [CosMMD](https://github.com/CyclopsRay/CosMMD).**

[Read the skill](SKILL.md) · [Get the code](https://github.com/CyclopsRay/CosMMD) · [中文](#中文)

</div>

Give the agent **one original character photo and access to a Tripo API key**.
The skill first prepares a T-pose image with Nano Banana Pro through Tripo API,
then uses that reviewed image for 3D generation. It guides source-preserving modeling, anatomical rig repair, articulated
fingers, licensed MMD motion import, render diagnosis, and verified delivery in Blender.
A separately licensed motion is required for the dance. Complex models still need
agent or human calibration; this is not a universal one-click rigging service.

The lessons are concrete: inspect before cutting, preserve the original hand and
shoe surfaces, fit the actual elbow and knee, account for the MMD rest pose, and
check every rendered frame. A black shoe patch can be a render-state failure—not
a reason to rebuild the shoe.

## Install

Clone this repository into your agent's skill directory. For Codex:

```sh
git clone https://github.com/CyclopsRay/2DCosplayerToMMD.git   ~/.codex/skills/2d-cosplayer-to-mmd
```

Restart or refresh the agent's skill discovery if needed. Install the companion
[CosMMD toolkit](https://github.com/CyclopsRay/CosMMD) for executable helpers.
The skill is automatically discoverable and can also be invoked explicitly:

```text
Use $2d-cosplayer-to-mmd to prepare a T-pose image from my original photo using
Nano Banana Pro through Tripo API, then turn that image into a faithful Blender
character and a 12-second MMD dance. Preserve the original hands,
shoes and outfit; use the motion I am licensed to use.
```

Provide credentials through local environment/secure storage, not inside a committed
prompt. The skill does not contain an API key, source model, motion file or baked action.

## What's inside

| Resource | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Core decisions, stage gates and output requirements |
| [Tripo operations](references/tripo.md) | Photo → Nano Banana Pro T pose → 3D, Studio/API boundaries and task recovery |
| [Rigging](references/rigging.md) | Source preservation, actual anatomy, fingers, knee IK and rest pose |
| [Rendering](references/rendering.md) | Black-artifact diagnosis, frame isolation and complete QA |
| [Publication](references/publication.md) | Copyright, credentials, audited media and honest presentation |

The showcased character has 104 rig bones and 30 finger bones. The companion README
shows a full 12-second rendered dance. Its [provenance](https://github.com/CyclopsRay/CosMMD/blob/main/docs/reproducibility.md)
explains the reused Studio source, manual calibration and remaining hair/garment limits.
The executable API adapter is contract-tested, not a fresh paid end-to-end benchmark.

**Star [CosMMD](https://github.com/CyclopsRay/CosMMD) to follow the project; star this
skill if the workflow helps your agent build better characters.**

## 中文

只需一张原始角色照片和 Tripo API 密钥。技能先引导 agent 通过 Tripo API 中的
Nano Banana Pro 生成 T pose 图片，对照原图检查后再用 T pose 生成 3D，随后完成原型保留、
骨骼校准、手指绑定、MMD 动作导入、逐帧渲染检查和交付。舞蹈动作需要另行取得许可；
复杂角色仍需要校准，并非所有图片都能全自动完成。

T pose 是中间产物，不需要你额外提供；已有合适 T pose 时也可以跳过预处理。
它记录了这次真实流程中最重要的经验：左右腿必须按身体定义，肘膝要落在真实关节位置；
手指存在时直接绑定，手、鞋和衣服不要随意重建；T pose 与 MMD 初始姿势需要校准；
视频必须逐帧检查，黑块可能来自渲染状态，不能直接归因于模型缺面。

安装命令见上方。用 `$2d-cosplayer-to-mmd` 调用技能；配合
[CosMMD 工具仓库](https://github.com/CyclopsRay/CosMMD) 运行代码。
[流程细节与踩坑记录](https://github.com/CyclopsRay/CosMMD/blob/main/docs/pitfalls.md)
持续维护，欢迎提交可复现的改进。

## Credits and license

Skill instructions: MIT. The externally embedded showcase is excluded from that
license. Motion: [つん](https://www.nicovideo.jp/watch/sm28422307), choreography:
[足太ぺんた](https://www.nicovideo.jp/watch/sm27753880), original song:
[TOKOTOKO / 西沢さんP](https://www.nicovideo.jp/watch/sm27529228).
[Full media policy](https://github.com/CyclopsRay/CosMMD/blob/main/docs/credits.md).
No model, VMD, audio or animated Blender scene is redistributed here.
