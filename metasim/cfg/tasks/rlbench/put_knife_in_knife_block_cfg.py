from metasim.cfg.objects import RigidObjCfg
from metasim.constants import PhysicStateType
from metasim.utils import configclass
from metasim.cfg.checkers import DetectedChecker, RelativeBboxDetector

from .rlbench_task_cfg import RLBenchTaskCfg

_OBJECTS = [
    RigidObjCfg(
        name="chopping_board_visual",
        usd_path="roboverse_data/assets/rlbench/put_knife_in_knife_block/chopping_board_visual/usd/chopping_board_visual.usd",
        physics=PhysicStateType.RIGIDBODY,
    ),
    RigidObjCfg(
        name="knife_block_visual",
        usd_path="roboverse_data/assets/rlbench/put_knife_in_knife_block/knife_block_visual/usd/knife_block_visual.usd",
        physics=PhysicStateType.GEOM,
    ),
    RigidObjCfg(
        name="knife_visual",
        usd_path="roboverse_data/assets/rlbench/put_knife_in_knife_block/knife_visual/usd/knife_visual.usd",
        physics=PhysicStateType.RIGIDBODY,
    ),
]


@configclass
class PutKnifeInKnifeBlockCfg(RLBenchTaskCfg):
    episode_length = 200
    traj_filepath = "roboverse_data/trajs/rlbench/put_knife_in_knife_block/v2"
    objects = _OBJECTS
    checker = DetectedChecker(
        obj_name="knife_visual",
        detector=RelativeBboxDetector(
            base_obj_name="knife_block_visual",
            relative_pos=[0.0, 0.0, 0.07185],
            relative_quat=[1.0, 0.0, 0.0, 0.0],
            checker_lower=[-0.08, -0.08, -0.11],
            checker_upper=[0.08, 0.08, 0.05],
            debug_vis=True
        ),
    )


@configclass
class PutKnifeOnChoppingBoardCfg(RLBenchTaskCfg):
    episode_length = 200
    traj_filepath = "roboverse_data/trajs/rlbench/put_knife_on_chopping_board/v2"
    objects = _OBJECTS
    # TODO: add checker
