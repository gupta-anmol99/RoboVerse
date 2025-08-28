# Roboverse V2E Patch
This documentation contains the patches for Roboverse for V2E Benchmark. 

## 🚀 Getting Started
- To download Roboverse, please refer to the original [documentation](https://roboverse.wiki/metasim/#).
- Roboverse team provides basic tutorials for getting started [tutorials](https://roboverse.wiki/metasim/get_started/quick_start/0_static_scene)

## 🛠️ Get Started
### 💾 Dataset
- The dataset is available on [huggingface](https://huggingface.co/datasets/RoboVerseOrg/roboverse_data). 
- This dataset contains assets, robots, scenes and trajs. 
- Assets are sorted by the dataset they were taken from and contain object assets. For example, the assests for rlbench contains obejct wise assets for every task. Most of the assets are in [usd](https://openusd.org/release/index.html) format.
- Trajs contains robot trajectories for tasks. The trajectores are sorted by the datasets and are stored in pkl.gz format.

**Note:** The data set is hosted on huggingface and doesn't need downloading seperately. `/metasim/utils/hf_util.py` contains scripts that downloads the data on the run, if required.

### 🚩 Tasks
The tasks in roboverse are based on configuration files. These cfg files are contained in `/metasim/cfg/tasks`. 
Config file for every task looks something like this-

```
@configclass
class CloseBoxCfg(RLBenchTaskCfg):
    episode_length = 250
    objects = [
        ArticulationObjCfg(
            name="box_base",
            fix_base_link=True,
            usd_path="metasim/data/quick_start/assets/rlbench/close_box/box_base/usd/box_base.usd",
            urdf_path="metasim/data/quick_start/assets/rlbench/close_box/box_base/urdf/box_base_unique.urdf",
            mjcf_path="metasim/data/quick_start/assets/rlbench/close_box/box_base/mjcf/box_base_unique.mjcf",
        ),
    ]
    traj_filepath = "metasim/data/quick_start/trajs/rlbench/close_box/v2"
    checker = JointPosChecker(
        obj_name="box_base",
        joint_name="box_joint",
        mode="le",
        radian_threshold=-14 / 180 * math.pi,
    )
```
- `@configclass` is a wrapper around  dataclass. It adds some checks for removing the mutable data strucutre problem.
- `TaskCfg` In example it uses RLBenchTaskCfg. This encodes the a lot of parameters of the task, including but not limited to, task type, episode length, objects,  etc.
- `objects` define all the objects present in the scene. You need to give the file path for atleast one fo the format. 
- `traj_filepath` If replaying a trajectory, this field contains the location of pkl.gz file containing the trajectories.
- `checker` This defines the **success** condition for the task. Put the name of the usd file for the object for example for CloseFridge task, check the name of the asset of fridge object. To get the joint name, use the `/scripts/print_usd_joint_names.py`. This script provides the joint names as well as their joint limits. There are two modes, "le" and "ge" that corresponds to less than and greater than or equal to. Finally radian_threshold defines the threshold for le and ge. Note that radian_threshold is valid for both revolute and prismatic joints. There are other checkers that are present in `/metasim/cfg/checkers/checkers.py`

### Checkers and Detectors
Checkers are contained in `/metasim/cfg/checkers/checkers.py` and detectors are in `/metasim/cfg/checkers/detectors.py`.

#### Checkers
- JointPosChecker: Checks if the `joint name` of the `object name` has positions of (less than or greater than) the threshold.
- JointPosShiftChecker: Checks if the `joint name` of the `object name` was moved more than a threshold.
- RotationShiftChecker: Checks if the `object name` was rotated more than a threshold around a given axis.
- PositionShiftChecker: CHecks if the `object name` was moved more than distance in meters in a gived axis.
- DetectedChecker: Check if the detectors specified has its conditioned fulfilled.

#### Detectors
- RelativeBboxDetector: Checks if the object is inside a bounding box. It takes a base_obj_name relative to which we define the bounding box using two opposide vertices, `checker_lower` and `checker_above`.

## Notes
1. For retargeting a demo, use retarget_demo_debugged.py instead of the original script. 

## TODOs

### 📍Roadmap
- Select 6 tasks common in rlbench and [RH20T](https://rh20t.github.io/static/RH20T_paper_compressed.pdf). ✅
- Go through bbox cheker and detected checker ✅
- Retargeting to different arms ✅ (sawyer)
- Make a composite checker for multi joints : **Next**
- Document thier joint names and limits. ✅
- Verify all 6 tasks.
- Need to work on bbox detector for multi settings.


### Updates
- For relative position based task, for eg. stack cubes, we need to use a detector which can be found in `/metasim/cfg/checkers/detectors.py`.
- Tasks names: Open a box, Close Drawer, Close microwave, Pick up cup, Press 3 buttons, Put knife in the block
- For tasks involving rigid bodies, for example, pick up cup or put knife in the block, we need to run the `sim/RoboVerse/scripts/clean_usd.py` script. This script adds the collision API to the obejcts. Note that, original version of this file has a minor error in `main()` which we have rectified in this patch. To clean just run: `python scripts/clean_usd.py --tasks PickUpCup`
- Added a hacky solution for bbox debug visualizer. Still, bbox checker doesn't work for multi env setting.

### Tasks List
- Open/Close a box: ✅
- Open/Close Drawer: ✅
- Open/Close microwave: ✅
- Pick up cup: ✅
- Press 3 buttons: **Need composite checker**
- Put knife in the block ✅ (Does not work for multi env)

