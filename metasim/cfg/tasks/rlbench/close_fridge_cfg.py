from metasim.cfg.objects import ArticulationObjCfg
from metasim.utils import configclass
from metasim.cfg.checkers import JointPosChecker
import math

from .rlbench_task_cfg import RLBenchTaskCfg

_OBJECTS = [
    ArticulationObjCfg(
        name="fridge_base",
        usd_path="roboverse_data/assets/rlbench/close_fridge/fridge_base/usd/fridge_base.usd",
    ),
]


@configclass
class CloseFridgeCfg(RLBenchTaskCfg):
    episode_length = 200
    traj_filepath = "roboverse_data/trajs/rlbench/close_fridge/v2"
    objects = _OBJECTS
    # TODO: add checker
    checker = JointPosChecker(
        obj_name="fridge_base",
        joint_name="top_joint",
        mode="le",
        radian_threshold=5 / 180 * math.pi,
    )


@configclass
class OpenFridgeCfg(RLBenchTaskCfg):
    episode_length = 200
    traj_filepath = "roboverse_data/trajs/rlbench/open_fridge/v2"
    objects = _OBJECTS
    # TODO: add checker
