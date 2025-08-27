from metasim.cfg.objects import RigidObjCfg
from metasim.constants import PhysicStateType
from metasim.utils import configclass
from metasim.cfg.checkers.checkers import PositionShiftChecker

from .rlbench_task_cfg import RLBenchTaskCfg


@configclass
class PickUpCupCfg(RLBenchTaskCfg):
    episode_length = 200
    traj_filepath = "roboverse_data/trajs/rlbench/pick_up_cup/v2"
    objects = [
        RigidObjCfg(
            name="cup1_visual",
            usd_path="roboverse_data/assets/rlbench/pick_up_cup/cup1_visual/usd/cup1_visual.usd",
            physics=PhysicStateType.XFORM,
        ),
        RigidObjCfg(
            name="cup2_visual",
            usd_path="roboverse_data/assets/rlbench/pick_up_cup/cup2_visual/usd/cup2_visual.usd",
            physics=PhysicStateType.RIGIDBODY,
        ),
    ]
    checker = PositionShiftChecker(
        obj_name="cup1_visual",
        distance=0.2,
        axis="z",
    )
