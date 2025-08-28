import gzip
import pickle
import json

with gzip.open("/home/local/ASUAD/agupt374/research_directory/Playground/sims/V2E-Bench/sim/RoboVerse/metasim/data/quick_start/trajs/rlbench/close_box/v2/sawyer_v2.pkl.gz", "rb") as f:
    data = pickle.load(f)

with open("/home/local/ASUAD/agupt374/research_directory/Playground/sims/V2E-Bench/sim/RoboVerse/metasim/data/quick_start/trajs/rlbench/close_box/v2/sawyer_v2.json", "w") as out:
    json.dump(data, out, indent=2)
