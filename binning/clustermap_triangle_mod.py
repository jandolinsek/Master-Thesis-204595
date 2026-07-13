# this script is a modification of the clustermap_triangle.py script, 
# https://github.com/bluenote-1577/skani/blob/main/scripts/clustermap_triangle.py 

import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable

import sys
sys.setrecursionlimit(100000)
from scipy.cluster import hierarchy
import scipy
import os

file = sys.argv[1]
threshold = sys.argv[2]
skani_dir = sys.argv[3]

if 'mash' in file:
    print("ANI matrix obtained from Mash detected.")
if 'fastani' in file:
    print("ANI matrix obtained from FastANI detected.")

# Extract ANI values
counter = 0
items = 0
labels = []
condensed = []
matrix = []
all_labels = set()
delim = '\t'
#delim = ','
for line in open(file, 'r'):
    if counter == 0:
        #print(line)
        spl = line.split(delim)
        if len(spl) > 2:
            items = len(spl)
        else:
            items = int(line.split(delim)[-1])
        #print(items)
        matrix = [[] for x in range(items)]
        counter += 1
        continue
    if delim in line:
        spl = line.split(delim);
    else:
        spl = line.split();
    #print(spl[0].split('/')[-1])
    labels.append(spl[0].split('/')[-1])
    endpoints = range(1,counter)
    for i in endpoints:
        if 'mash' in file:
            matrix[i-1].append(100 - 100 * float(spl[i]))
        elif 'fastani' in file:
            matrix[i-1].append(float(spl[i]))
        else:
            if float(spl[i]) <= 1:
                matrix[i-1].append(float(spl[i]) * 100)
            else:
                matrix[i-1].append(float(spl[i]))
    counter += 1

for vec in matrix:
    for score in vec:
        condensed.append(100 - score)


#Z = hierarchy.linkage(condensed, 'single')
#Z = hierarchy.linkage(condensed, 'complete')
Z = hierarchy.linkage(condensed, 'average')
square_mat = scipy.spatial.distance.squareform(condensed)

# Get the reordering from the dendrogram
dendrogram_order = hierarchy.dendrogram(Z, no_plot=True)['leaves']
re = [labels[x] for x in dendrogram_order]
re2 = []

for el in re:
    if el[0:30].startswith('bin'):
        re2.append(el[0:30]) 
    else:
        re2.append(el[0:30].split('.')[0])

# Reorder the matrix according to the dendrogram
reordered_mat = square_mat[dendrogram_order, :][:, dendrogram_order]
reordered_mat_inv = 100 - reordered_mat

# Extract cluster assignments if nclusters or threshold is specified
clust_threshold = 1

if clust_threshold is not None:
    clusters = hierarchy.fcluster(Z, clust_threshold, criterion='distance')
    cluster_method = f"threshold={clust_threshold}"
    
cluster_file = os.path.join(skani_dir, 'clusters.txt')
clustered_bins = dict()
for i in range(1,max(clusters)+1):
    clustered_bins[i]=list()

with open(cluster_file, 'w') as f:
    for i, label in enumerate(labels):
        f.write(f'{label}\t{clusters[i]}\n')
        clustered_bins[clusters[i]].append(label)

# Set the colormap
cmap = plt.cm.plasma

# Create Figure and GridSpec (2 rows, 1 column)
fig = plt.figure(figsize=(10, 12))
gs = fig.add_gridspec(2, 1, height_ratios=[1, 6], hspace=0.001)

ax_dendro = fig.add_subplot(gs[0, 0])
ax_heatmap = fig.add_subplot(gs[1, 0])

# Heatmap
im = ax_heatmap.imshow(reordered_mat_inv, cmap=cmap, vmin=threshold, vmax=100, aspect='equal')
    
# Set ticks and labels
yticks = np.arange(len(labels))
ax_heatmap.set_yticks(yticks)
ax_heatmap.set_xticklabels([])
ax_heatmap.set_yticklabels(re2, fontsize=10)

# Split the axes for proportioned colorbar
divider = make_axes_locatable(ax_heatmap)
cbar_ax = divider.append_axes("right", size="5%", pad=0.1)
plt.colorbar(im, cax=cbar_ax)
cbar_ax.set_ylabel('ANI (%)', rotation=270)

# Dendrogram (top)
dendro = hierarchy.dendrogram(Z, ax=ax_dendro, no_labels=True, color_threshold=0)
ax_dendro.axis('off')

# Split the axes 
divider2 = make_axes_locatable(ax_dendro)
ax_spacer = divider2.append_axes("right", size="5%", pad=0.1)
ax_spacer.axis('off')

# Save the figure to a file instead of displaying
output_file = os.path.join(skani_dir, 'clustermap_output.png')
plt.savefig(output_file, dpi=600, bbox_inches='tight')
print(f"Clustermap saved to: {output_file}")

