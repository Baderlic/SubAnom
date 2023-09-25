#/bin/bash
source activate base
conda activate DynAnomKDD

#### DARPA Experiments

### Baseline
python -u  ../src/algorithms/SubAnom/exp_DynAnom_graph_level.py -dataset_name darpa -detect_anomaly -track_mode all -top_index 100 -make_multi_graph -dim 1024 -push_threshold 0.0001 -epsilon 1e-2

### SubAnom
## 1-hop
python -u  ../src/algorithms/SubAnom/exp_DynAnom_subgraph_graph_level.py	-dataset_name darpa -detect_anomaly -track_mode all  -top_index 100 -make_multi_graph -dim 1024 -push_threshold 0.0001 -hop_k 1 -subgraph2node_strategy mean -epsilon 1e-2 -subgraph_pattern khop
## 2-hop
python -u  ../src/algorithms/SubAnom/exp_DynAnom_subgraph_graph_level.py	-dataset_name darpa -detect_anomaly -track_mode all  -top_index 100 -make_multi_graph -dim 1024 -push_threshold 0.0001 -hop_k 2 -subgraph2node_strategy mean -epsilon 1e-2 -subgraph_pattern khop
## 3-hop
python -u  ../src/algorithms/SubAnom/exp_DynAnom_subgraph_graph_level.py	-dataset_name darpa -detect_anomaly -track_mode all  -top_index 100 -make_multi_graph -dim 1024 -push_threshold 0.0001 -hop_k 3 -subgraph2node_strategy mean -epsilon 1e-2 -subgraph_pattern khop
## 1-hop TC
python -u  ../src/algorithms/SubAnom/exp_DynAnom_subgraph_graph_level.py	-dataset_name darpa -detect_anomaly -track_mode all  -top_index 100 -make_multi_graph -dim 1024 -push_threshold 0.0001 -hop_k 1 -subgraph2node_strategy mean -epsilon 1e-2 -subgraph_pattern triangle
## Hybrid TC
python -u  ../src/algorithms/SubAnom/exp_DynAnom_subgraph_graph_level.py	-dataset_name darpa -detect_anomaly -track_mode all  -top_index 100 -make_multi_graph -dim 1024 -push_threshold 0.0001 -hop_k 3 -subgraph2node_strategy mean -epsilon 1e-2 -subgraph_pattern strong-all

