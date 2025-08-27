import argparse
import json
import os
from pathlib import Path
from omni.isaac.lab.app import AppLauncher

parser = argparse.ArgumentParser()
parser.add_argument("--usd_path", type=str, required=True)
parser.add_argument("--json_path", type=str, default="knowledge/assets/rlbench/objects.json")
AppLauncher.add_app_launcher_args(parser)
args = parser.parse_args()
args.headless = True
app_launcher = AppLauncher(args)
simulation_app = app_launcher.app

###########################################################
import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.assets import Articulation, ArticulationCfg


obj = Articulation(
    ArticulationCfg(
        prim_path="/World/test",
        spawn=sim_utils.UsdFileCfg(usd_path=args.usd_path),
        actuators={},
    ),
)
sim_cfg = sim_utils.SimulationCfg(dt=0.01, device="cpu")
sim = sim_utils.SimulationContext(sim_cfg)
sim.reset()


usd_key = os.path.splitext(os.path.basename(args.usd_path))[0]

entry = {}
entry["joint_names"] = obj.joint_names

limits = obj.root_physx_view.get_dof_limits().squeeze(0).tolist()
# map each joint to [min, max]
entry["joint_limits"] = {
    jn: [jl[0], jl[1]] for jn, jl in zip(obj.joint_names, limits)
}

print("Joint names:")
print("=" * 100)
print(obj.joint_names)
print("=" * 100)
joint_limits = obj.root_physx_view.get_dof_limits().squeeze(0).tolist()
# joint_qpos = obj.root_physx_view.get_dof_positions()
# print(joint_qpos)
# print(obj.root_physx_view.get_dof_position_targets())
for joint_name, joint_limit in zip(obj.joint_names, joint_limits):
    print(f"{joint_name}: ({joint_limit[0]:.4f}, {joint_limit[1]:.4f})")

print("=" * 100)
print("Body names:")
print(obj.body_names)
print("=" * 100)

json_path = Path(args.json_path)


if json_path.exists():
    try:
        with json_path.open("r") as f:
            db = json.load(f)
        if not isinstance(db, dict):
            print(f"[WARN] {json_path} was not a dict. Replacing with empty dict.")
            db = {}
    except json.JSONDecodeError:
        print(f"[WARN] {json_path} was invalid JSON. Replacing with empty dict.")
        db = {}
else:
    db = {}

# Insert only if the key is new
if usd_key in db:
    print(f"[SKIP] Key '{usd_key}' already exists in {json_path}. Not modifying file.")
else:
    db[usd_key] = entry
    with json_path.open("w") as f:
        json.dump(db, f, indent=2)
    print(f"[OK] Added '{usd_key}' to {json_path}")




