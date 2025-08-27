from metasim.cfg.objects import ArticulationObjCfg
from metasim.utils import configclass
import math 
from metasim.cfg.checkers import JointPosChecker

from .rlbench_task_cfg import RLBenchTaskCfg

_OBJECTS = [
    ArticulationObjCfg(
        name="drawer_frame",
        usd_path="roboverse_data/assets/rlbench/close_drawer/drawer_frame/usd/drawer_frame.usd",
    ),
]


@configclass
class CloseDrawerCfg(RLBenchTaskCfg):
    episode_length = 200
    traj_filepath = "roboverse_data/trajs/rlbench/close_drawer/v2"
    objects = _OBJECTS
    checker = JointPosChecker(
        obj_name="drawer_frame",
        joint_name="drawer_joint_bottom",
        mode="le",
        radian_threshold=0.01
    )



@configclass
class OpenDrawerCfg(RLBenchTaskCfg):
    episode_length = 200
    traj_filepath = "roboverse_data/trajs/rlbench/open_drawer/v2"
    objects = _OBJECTS
    checker = JointPosChecker(
        obj_name="drawer_frame",
        joint_name="drawer_joint_bottom",
        mode="ge",
        radian_threshold=0.1
    )
