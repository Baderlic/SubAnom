import os
os.listdir()
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



plt.rcParams['font.sans-serif'] = ['roman']
plt.rcParams['axes.unicode_minus'] = False
local_out_dir = '../out'


#read darpa results
# darpa_khop1 = pd.read_csv('out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_khop/khop1.csv')
# darpa_khop2 = pd.read_csv("out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_khop/khop2.csv")
# darpa_khop3 = pd.read_csv("out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_khop/khop3.csv")
# darpa_strong_all = pd.read_csv("out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_strong-all/strong-all.csv")
# darpa_triangle = pd.read_csv("out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_triangle/triangle.csv")
# darpa_baseline = pd.read_csv("out/dataset_darpa-initSS_256-timeStep_60/baseline.csv")

#if these two not applicable, use the other two
darpa_khop1 = pd.read_csv('out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_khop/DynAnomPy-alpha_1.50e-01-epsilon_1.00e-02-track_mode_all-dim-1024-top_index_100-push_threshold-1.00e-04-make_directed_graph_False-make_multi_graph_True-hop_k_1-strategy_mean_precision_recall_score.csv')
darpa_khop2 = pd.read_csv("out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_khop/DynAnomPy-alpha_1.50e-01-epsilon_1.00e-02-track_mode_all-dim-1024-top_index_100-push_threshold-1.00e-04-make_directed_graph_False-make_multi_graph_True-hop_k_2-strategy_mean_precision_recall_score.csv")
# darpa_khop1 = pd.read_csv('out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_khop/khop1.csv')
# darpa_khop2 = pd.read_csv("out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_khop/khop2.csv")

darpa_khop3 = pd.read_csv("out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_khop/DynAnomPy-alpha_1.50e-01-epsilon_1.00e-02-track_mode_all-dim-1024-top_index_100-push_threshold-1.00e-04-make_directed_graph_False-make_multi_graph_True-hop_k_3-strategy_mean_precision_recall_score.csv")
darpa_strong_all = pd.read_csv("out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_strong-all/DynAnomPy-alpha_1.50e-01-epsilon_1.00e-02-track_mode_all-dim-1024-top_index_100-push_threshold-1.00e-04-make_directed_graph_False-make_multi_graph_True-hop_k_3-strategy_mean_precision_recall_score.csv")
darpa_triangle = pd.read_csv("out/dataset_darpa-initSS_256-timeStep_60_subgraph_pattern_triangle/DynAnomPy-alpha_1.50e-01-epsilon_1.00e-02-track_mode_all-dim-1024-top_index_100-push_threshold-1.00e-04-make_directed_graph_False-make_multi_graph_True-hop_k_1-strategy_mean_precision_recall_score.csv")
darpa_baseline = pd.read_csv("out/dataset_darpa-initSS_256-timeStep_60/DynAnomPy-alpha_1.50e-01-epsilon_1.00e-02-track_mode_all-dim-1024-top_index_100-push_threshold-1.00e-04-make_directed_graph_False-make_multi_graph-True_precision_recall_score.csv")

#Precision-Recall Curves to compare subgraph strategies

#figure1
baseline_1 = darpa_baseline.loc[darpa_baseline["anomaly_score"]=="DynAnomScore(l1-mean)"]
khop1_1 = darpa_khop1.loc[darpa_khop1["anomaly_score"]=="DynAnomSubgraphScore(l1-sum)"]
khop2_1 = darpa_khop2.loc[darpa_khop2["anomaly_score"]=="DynAnomSubgraphScore(l1-max)"]
khop3_1 = darpa_khop3.loc[darpa_khop3["anomaly_score"]=="DynAnomSubgraphScore(l1-median)"]
triangle_1 = darpa_triangle.loc[darpa_triangle["anomaly_score"]=="DynAnomSubgraphScore(l1-sum)"]
strong_1 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l1-sum)"]

x = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]

fig, ax1 = plt.subplots(figsize=(6.4, 4.8))
plt.xlabel("Recall", fontsize = 25)
plt.ylabel("Precision", fontsize = 25)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
ax1.plot(baseline_1["recall"].tolist(), baseline_1["precision"].tolist(), color="black", alpha=0.5, linestyle="-",linewidth=3, marker='*')
ax1.plot(khop1_1["recall"].tolist(), khop1_1["precision"].tolist(), color="green", alpha=0.5,linestyle='--',linewidth=3,marker='*')
ax1.plot(khop2_1["recall"].tolist(), khop2_1["precision"].tolist(), color='blue',alpha=0.5,linestyle='-.',linewidth=3,marker='*')
ax1.plot(khop3_1["recall"].tolist(), khop3_1["precision"].tolist(), color='orange',alpha=0.5,linestyle=':',linewidth=3,marker='*')
ax1.plot(triangle_1["recall"].tolist(), triangle_1["precision"].tolist(), color='purple',alpha=0.5,linestyle='-.',linewidth=3,marker='o')
ax1.plot(strong_1["recall"].tolist(), strong_1["precision"].tolist(), color='red',alpha=0.5,linestyle='-',linewidth=3,marker='o')
ax1.legend(['SubAnom', 'SubAnom(1-hop)', 'SubAnom(2-hop)', 'SubAnom(3-hop)', 'SubAnom(1-hop TC)', 'SubAnom(Hybrid TC)'], loc="upper right", fontsize = "x-large")  # set labels of lines
plt.grid()
#leg = ax1.legend(loc='center right', bbox_to_anchor=(1.0, 0.5), prop={'size': 15}) #set the legends
plt.savefig("SubAnom-l1.pdf",bbox_inches='tight', pad_inches=0, format='pdf')

#figure 2
baseline_2 = darpa_baseline.loc[darpa_baseline["anomaly_score"]=="DynAnomScore(l2-mean)"]
khop1_2 = darpa_khop1.loc[darpa_khop1["anomaly_score"]=="DynAnomSubgraphScore(l2-sum)"]
khop2_2 = darpa_khop2.loc[darpa_khop2["anomaly_score"]=="DynAnomSubgraphScore(l2-sum)"]
khop3_2 = darpa_khop3.loc[darpa_khop3["anomaly_score"]=="DynAnomSubgraphScore(l2-sum)"]
triangle_2 = darpa_triangle.loc[darpa_triangle["anomaly_score"]=="DynAnomSubgraphScore(l2-sum)"]
strong_2 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l2-median)"]

fig, ax2 = plt.subplots(figsize = (6.4, 4.8))
plt.xlabel("Recall", fontsize = 25)
#plt.ylabel("Precision", fontsize = 25)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
ax2.plot(baseline_2["recall"].tolist(), baseline_2["precision"].tolist(), color="black", alpha=0.5, linestyle="-",linewidth=3, marker='*')
ax2.plot(khop1_2["recall"].tolist(), khop1_2["precision"].tolist(), color="green", alpha=0.5,linestyle='--',linewidth=3,marker='*')
ax2.plot(khop2_2["recall"].tolist(), khop2_2["precision"].tolist(), color='blue',alpha=0.5,linestyle='-.',linewidth=3,marker='*')
ax2.plot(khop3_2["recall"].tolist(), khop3_2["precision"].tolist(), color='orange',alpha=0.5,linestyle=':',linewidth=3,marker='*')
ax2.plot(triangle_2["recall"].tolist(), triangle_2["precision"].tolist(), color='purple',alpha=0.5,linestyle='-.',linewidth=3,marker='o')
ax2.plot(strong_2["recall"].tolist(), strong_2["precision"].tolist(), color='red',alpha=0.5,linestyle='-',linewidth=3,marker='o')
ax2.legend(['SubAnom', 'SubAnom(1-hop)', 'SubAnom(2-hop)', 'SubAnom(3-hop)', 'SubAnom(1-hop TC)', 'SubAnom(Hybrid TC)'], loc="upper right", fontsize = "x-large")  # 设置折线名称
plt.grid()
plt.savefig("SubAnom-l2.pdf", bbox_inches='tight', pad_inches=0, format='pdf')

#figure3
baseline_3 = darpa_baseline.loc[darpa_baseline["anomaly_score"]=="DynAnomScore(l1-mean-ppe)"]
khop1_3 = darpa_khop1.loc[darpa_khop1["anomaly_score"]=="DynAnomSubgraphScore(l1-sum-ppe)"]
khop2_3 = darpa_khop2.loc[darpa_khop2["anomaly_score"]=="DynAnomSubgraphScore(l1-min-ppe)"]
khop3_3 = darpa_khop3.loc[darpa_khop3["anomaly_score"]=="DynAnomSubgraphScore(l1-median-ppe)"]
triangle_3 = darpa_triangle.loc[darpa_triangle["anomaly_score"]=="DynAnomSubgraphScore(l2-sum-ppe)"]
strong_3 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l2-sum-ppe)"]

fig, ax3 = plt.subplots(figsize = (6.4, 4.8))
plt.xlabel("Recall", fontsize=25)
#plt.ylabel("Precision", fontsize=25)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
ax3.plot(baseline_3["recall"].tolist(), baseline_3["precision"].tolist(), color="black", alpha=0.5, linestyle="-",linewidth=3, marker='*')
ax3.plot(khop1_3["recall"].tolist(), khop1_3["precision"].tolist(), color="green", alpha=0.5,linestyle='--',linewidth=3,marker='*')
ax3.plot(khop2_3["recall"].tolist(), khop2_3["precision"].tolist(), color='blue',alpha=0.5,linestyle='-.',linewidth=3,marker='*')
ax3.plot(khop3_3["recall"].tolist(), khop3_3["precision"].tolist(), color='orange',alpha=0.5,linestyle=':',linewidth=3,marker='*')
ax3.plot(triangle_3["recall"].tolist(), triangle_3["precision"].tolist(), color='purple',alpha=0.5,linestyle='-.',linewidth=3,marker='o')
ax3.plot(strong_3["recall"].tolist(), strong_3["precision"].tolist(), color='red',alpha=0.5,linestyle='-',linewidth=3,marker='o')
ax3.legend(['DynPPE', 'SubAnom(1-hop)', 'SubAnom(2-hop)', 'SubAnom(3-hop)', 'SubAnom(1-hop TC)', 'SubAnom(Hybrid TC)'], loc="lower right", fontsize = "x-large")  # 设置折线名称
plt.grid()
plt.savefig("DynPPE-l1.pdf", bbox_inches='tight', pad_inches=0, format='pdf')

#figure4
baseline_4 = darpa_baseline.loc[darpa_baseline["anomaly_score"]=="DynAnomScore(l2-mean-ppe)"]
khop1_4 = darpa_khop1.loc[darpa_khop1["anomaly_score"]=="DynAnomSubgraphScore(l2-sum-ppe)"]
khop2_4 = darpa_khop2.loc[darpa_khop2["anomaly_score"]=="DynAnomSubgraphScore(l2-min-ppe)"]
khop3_4 = darpa_khop3.loc[darpa_khop3["anomaly_score"]=="DynAnomSubgraphScore(l2-median-ppe)"]
triangle_4 = darpa_triangle.loc[darpa_triangle["anomaly_score"]=="DynAnomSubgraphScore(l2-sum-ppe)"]
strong_4 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l2-sum-ppe)"]

fig, ax4 = plt.subplots(figsize = (6.4, 4.8))
plt.xlabel("Recall", fontsize=25)
#plt.ylabel("Precision", fontsize=25)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
ax4.plot(baseline_4["recall"].tolist(), baseline_4["precision"].tolist(), color="black", alpha=0.5, linestyle="-",linewidth=3, marker='*')
ax4.plot(khop1_4["recall"].tolist(), khop1_4["precision"].tolist(), color="green", alpha=0.5,linestyle='--',linewidth=3,marker='*')
ax4.plot(khop2_4["recall"].tolist(), khop2_4["precision"].tolist(), color='blue',alpha=0.5,linestyle='-.',linewidth=3,marker='*')
ax4.plot(khop3_4["recall"].tolist(), khop3_4["precision"].tolist(), color='orange',alpha=0.5,linestyle=':',linewidth=3,marker='*')
ax4.plot(triangle_4["recall"].tolist(), triangle_4["precision"].tolist(), color='purple',alpha=0.5,linestyle='-.',linewidth=3,marker='o')
ax4.plot(strong_4["recall"].tolist(), strong_4["precision"].tolist(), color='red',alpha=0.5,linestyle='-',linewidth=3,marker='o')
ax4.legend(['DynPPE', 'SubAnom(1-hop)', 'SubAnom(2-hop)', 'SubAnom(3-hop)', 'SubAnom(1-hop TC)', 'SubAnom(Hybrid TC)'], loc="lower right", fontsize = "x-large")  # 设置折线名称
plt.grid()
plt.savefig("DynPPE-l2.pdf", bbox_inches='tight', pad_inches=0, format='pdf')

# baseline_5 = enron_baseline.loc[enron_baseline["anomaly_score"]=="DynAnomScore(l1-mean)"]
# khop1_5 = enron_khop1.loc[enron_khop1["anomaly_score"]=="DynAnomSubgraphScore(l1-min)"]
# khop2_5 = enron_khop2.loc[enron_khop2["anomaly_score"]=="DynAnomSubgraphScore(l1-min)"]
# khop3_5 = enron_khop3.loc[enron_khop3["anomaly_score"]=="DynAnomSubgraphScore(l1-min)"]
# triangle_5 = enron_triangle.loc[enron_triangle["anomaly_score"]=="DynAnomSubgraphScore(l1-min)"]
# strong_5 = enron_strong_all.loc[enron_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l1-min)"]
#
# x = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]
# plt.xlabel("Recall")
# plt.ylabel("Precision")
# plt.plot(baseline_5["recall"].tolist(), baseline_5["precision"].tolist(), color="purple", alpha=0.5, linestyle="-",linewidth=3, marker='o')
# plt.plot(khop1_5["recall"].tolist(), khop1_5["precision"].tolist(), color="green", alpha=0.5,linestyle='-',linewidth=3,marker='o')
# plt.plot(khop2_5["recall"].tolist(), khop2_5["precision"].tolist(), color='blue',alpha=0.5,linestyle='-',linewidth=3,marker='o')
# plt.plot(khop3_5["recall"].tolist(), khop3_5["precision"].tolist(), color='orange',alpha=0.5,linestyle='-',linewidth=3,marker='o')
# plt.plot(triangle_5["recall"].tolist(), triangle_5["precision"].tolist(), color='red',alpha=0.5,linestyle='-',linewidth=3,marker='o')
# plt.plot(strong_5["recall"].tolist(), strong_5["precision"].tolist(), color='black',alpha=0.5,linestyle='-',linewidth=3,marker='o')
# plt.legend(['基线', '1跳', '2跳', '3跳', '1跳强', '复合'])  # 设置折线名称
# plt.show()

#Precision-Recall Curves to compare functions
#figure5: best subgraph aggregating function
sum_1 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l1-sum)"]
median_1 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l1-median)"]
min_1 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l1-min)"]
max_1 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l1-max)"]
mean_1 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l1-mean)"]

fig, ax5 = plt.subplots(figsize = (6.4, 4.8))
plt.xlabel("Recall", fontsize = 20)
plt.ylabel("Precision", fontsize=20)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
ax5.plot(baseline_1["recall"].tolist(), baseline_1["precision"].tolist(), color="black", alpha=0.5, linestyle="-",linewidth=3, marker='o')
ax5.plot(sum_1["recall"].tolist(), sum_1["precision"].tolist(), color="green", alpha=0.5,linestyle='--',linewidth=3,marker='o')
ax5.plot(median_1["recall"].tolist(), median_1["precision"].tolist(), color='blue',alpha=0.5,linestyle='-.',linewidth=3,marker='o')
ax5.plot(min_1["recall"].tolist(), min_1["precision"].tolist(), color='red',alpha=0.5,linestyle=':',linewidth=3,marker='o')
ax5.plot(max_1["recall"].tolist(), max_1["precision"].tolist(), color='purple',alpha=0.5,linestyle='-',linewidth=3,marker='o')
ax5.plot(mean_1["recall"].tolist(), mean_1["precision"].tolist(), color='cyan',alpha=0.5,linestyle='--',linewidth=3,marker='o')
ax5.legend([r'SubAnom-$\ell_1$',r'Sum-$\ell_1$', r'Median-$\ell_1$', r'Min-$\ell_1$', r'Max-$\ell_1$', r'Mean-$\ell_1$'], loc="upper right", fontsize = "x-large")  # 设置折线名称

plt.grid()
plt.savefig("agg_l1.pdf", bbox_inches='tight', pad_inches=0, format='pdf')


#figure6
sum_2 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l2-sum)"]
median_2 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l2-median)"]
min_2 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l2-min)"]
max_2 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l2-max)"]
mean_2 = darpa_strong_all.loc[darpa_strong_all["anomaly_score"]=="DynAnomSubgraphScore(l2-mean)"]


fig, ax6 = plt.subplots(figsize = (6.4, 4.8))
plt.xlabel("Recall", fontsize = 20)
#plt.ylabel("Precision", fontsize=25)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
ax6.plot(baseline_2["recall"].tolist(), baseline_2["precision"].tolist(), color="black", alpha=0.5, linestyle="-",linewidth=3, marker='o')
ax6.plot(sum_2["recall"].tolist(), sum_2["precision"].tolist(), color="green", alpha=0.5,linestyle='--',linewidth=3,marker='o')
ax6.plot(median_2["recall"].tolist(), median_2["precision"].tolist(), color='blue',alpha=0.5,linestyle='-.',linewidth=3,marker='o')
ax6.plot(min_2["recall"].tolist(), min_2["precision"].tolist(), color='red',alpha=0.5,linestyle=':',linewidth=3,marker='o')
ax6.plot(max_2["recall"].tolist(), max_2["precision"].tolist(), color='purple',alpha=0.5,linestyle='-',linewidth=3,marker='o')
ax6.plot(mean_2["recall"].tolist(), mean_2["precision"].tolist(), color='cyan',alpha=0.5,linestyle='--',linewidth=3,marker='o')
ax6.legend([r'SubAnom-$\ell_2$', r'Sum-$\ell_2$', r'Median-$\ell_2$', r'Min-$\ell_2$', r'Max-$\ell_1$', r'Mean-$\ell_1$'], loc="upper right", fontsize = "x-large")
plt.grid()
plt.savefig("agg_l2.pdf", bbox_inches='tight', pad_inches=0, format='pdf')

# figure 7: Compare L1 and L2 given the best subgraph aggregating functions
fig, ax7 = plt.subplots(figsize = (6.4, 4.8))
plt.xlabel("Recall", fontsize = 20)
plt.ylabel("Precision", fontsize=20)
ax7.plot(sum_1["recall"].tolist(), sum_1["precision"].tolist(), color="lime", alpha=0.5,linestyle='-',linewidth=3,marker='o')
ax7.plot(sum_2["recall"].tolist(), sum_2["precision"].tolist(), color="darkgreen", alpha=0.5,linestyle='--',linewidth=3,marker='o')
ax7.plot(median_1["recall"].tolist(), median_1["precision"].tolist(), color="violet", alpha=0.5,linestyle='-.',linewidth=3,marker='*')
ax7.plot(median_2["recall"].tolist(), median_2["precision"].tolist(), color="purple", alpha=0.5,linestyle=':',linewidth=3,marker='*')
ax7.legend([r'Sum-$\ell_1$', r'Sum-$\ell_2$', r'Median-$\ell_1$', r'Median-$\ell_2$'], loc="upper right", fontsize = "x-large")
plt.grid()
plt.savefig("score_function.pdf", bbox_inches='tight', pad_inches=0, format='pdf')

plt.show()
