import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

OUTPUT1 = "Minimal_distance_inter_intraclass_VirB4_Patescibacteria.tsv"
OUTPUT_FILE = "Figure3.{ext}"
OUTPUT_EXTS = ["png", "svg", "pdf"]

# PATRISTIC DISTANCE MATRIX
file1 = "Patristic_distances_VirB4_phylogeny.csv"
# Table with taxonomy info
file2 = "TableS1.csv"


# Read patristic distance matrix
matriz_dist = pd.read_csv(file1, sep=",", index_col=0)
list_virb4 = (matriz_dist.index.values)

df_tax = pd.read_csv(file2, sep=",")
list_genomes = df_tax["Genome"].to_list()

# Process patristic distance matrix:
# For each VirB4, find the closest homolog (minimal patristic distance) from 
# the same class (intraclass) and different class (interclass)
list_dicc = []
for virb4 in list_virb4:
    intraclass = 0
    interclass = 0
    # obtain assembly accession
    assembly = virb4.split("|")[0]
    # if it is not a Patescibacteria genome, continue
    if assembly not in list_genomes:
        continue
    # obtain corresponding class taxonomy
    tax_class = df_tax[df_tax["Genome"]==assembly]["Class"].to_list()[0]
    ### SEARCH MINIMAL DISTANCES ###
    s = matriz_dist[virb4]
    # sort according to patristic distances in the tree
    s_sorted = s.sort_values(ascending=True)
    # iterate until find the closest homolog 
    for index, value in s_sorted.items():
        if index == virb4:
            continue
        # obtain genome from target VirB4
        target_assembly = index.split("|")[0]
        # if the VirB4 is not found in a Patescibacteria genome, continue
        if target_assembly not in list_genomes:
            continue
        # obtain taxonomy class of target VirB4 homolog
        target_class = df_tax[df_tax["Genome"]==target_assembly]["Class"].to_list()[0]
        # if they belong to the same taxonomy class
        if tax_class == target_class:
            # select only the closest homolog
            if intraclass == 0:
                list_dicc.append({
                    "VirB4_query" : virb4,
                    "Phylum_query" : tax_class,
                    "VirB4_target" : index,
                    "Phylum_target" : target_class,
                    "Minimal_Distance" : value,
                    "Type" : "Intraclass"
                })
                intraclass+=1
            else:
                continue
        elif tax_class !=target_class:
            # select only the closest homolog
            if interclass==0:
                list_dicc.append({
                    "VirB4_query" : virb4,
                    "Phylum_query" : tax_class,
                    "VirB4_target" : index,
                    "Phylum_target" : target_class,
                    "Minimal_Distance" : value,
                    "Type" : "Interclass"
                })
                interclass+=1
            else:
                continue
        
        # if the minimal distances for intraclass and interclass are selected, pass to the next VirB4 homolog
        if interclass==1 and intraclass==1:
            break


df_dist = pd.DataFrame(list_dicc)
df_dist.to_csv(OUTPUT1, sep=",", index=False)


##### CDF REPRESENTATION #####
sns.set(style="white", color_codes=True)
a4_dims = (8, 6)
fig, ax= plt.subplots(figsize=a4_dims)

# custom colors for Interclass and Intraclass distances
dicc_color = {"Intraclass" : "#e41a1c", "Interclass" : "#377eb8"} 
g = sns.ecdfplot(data=df_dist, x="Minimal_Distance", hue="Type", linewidth=2.5, palette=dicc_color)
ax.set_xlabel("Patristic Distance", fontsize=14)
ax.set_ylabel("CDF", fontsize=14)
plt.setp(ax.get_legend().get_texts(), fontsize="16") # for legend text
g.legend_.set_title(None) # remove legend text
g.legend_.set_bbox_to_anchor((1, 0.2), transform=ax.transAxes) # custom legend position
g.legend_.set_frame_on(True)  
g.tick_params(labelsize=14)
sns.despine()
plt.tight_layout()
for ext in OUTPUT_EXTS:
    plt.savefig(OUTPUT_FILE.format(ext), dpi=500, format=ext);
