
If there is data in toy-data folder, there is no need to download data.

## 1. Set up env

```
sh ./recipe/setup.sh
```
##### Notes  1. Due to weiredness of Numba, a specific python version (3.7) is needed: #SEE: https://github.com/numba/numba/issues/5156
##### Notes  2. DynAnom is a weighted version of DynamicPPE  


## 2. Run the method (all experiments)
```
sh ./recipe/run.sh
```

## 3. Output figure/results:
Once get all results in ``` ./output ```
All figures in the paper were painted in:
```
./src/precision-recall.py
```
The figures/results should be reproduced. Cheers! 


## The output corresponding path
baseline-darpa: 
```
./out/dataset_darpa-initSS_256-timeStep_60/
DynAnomPy-alpha_1.50e-01-epsilon_1.00e-02-track_mode_all-dim-1024-top_index_100-push_threshold-1.00e-04-make_directed_graph_False-make_multi_graph-True_precision_recall_score
```
khop1-darpa:
``` 
./out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_khop/
DynAnomPy-alpha_1.50e-01-epsilon_1.00e-02-track_mode_all-dim-1024-top_index_100-push_threshold-1.00e-04-make_directed_graph_False-make_multi_graph_True-hop_k_1-strategy_mean_precision_recall_score
```
khop2-darpa: 
```
./out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_khop/
DynAnomPy-alpha_1.50e-01-epsilon_1.00e-02-track_mode_all-dim-1024-top_index_100-push_threshold-1.00e-04-make_directed_graph_False-make_multi_graph_True-hop_k_2-strategy_mean_precision_recall_score
```
khop3-darpa: 
```
./out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_khop/
DynAnomPy-alpha_1.50e-01-epsilon_1.00e-02-track_mode_all-dim-1024-top_index_100-push_threshold-1.00e-04-make_directed_graph_False-make_multi_graph_True-hop_k_3-strategy_mean_precision_recall_score
```
1-hop TC-darpa:
```
./out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_triangle/
DynAnomPy-alpha_1.50e-01-epsilon_1.00e-02-track_mode_all-dim-1024-top_index_100-push_threshold-1.00e-04-make_directed_graph_False-make_multi_graph_True-hop_k_1-strategy_mean_precision_recall_score
```
Hybrid TC-darpa:
```
./out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_strong-all/
DynAnomPy-alpha_1.50e-01-epsilon_1.00e-02-track_mode_all-dim-1024-top_index_100-push_threshold-1.00e-04-make_directed_graph_False-make_multi_graph_True-hop_k_1-strategy_mean_precision_recall_score
```