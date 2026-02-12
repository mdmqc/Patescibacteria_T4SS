# The Type IV Secretion System of Patescibacteria is homologous to the bacterial monoderm conjugation machinery

This study used a comprehensive bioinformatics approach to investigate the diversity and distribution of T4SS within the Patescibacteria lineage. 

The Patescibacteria proteomes from NCBI RefSeq212 database used in the analysis are collected in the folder [data](data). The T4SS components were detected using Hidden Markow Model (HMM) profiles of the protein components of the eight phylogenetic classes of T4SS (available at https://github.com/macsy-models/CONJScan/tree/main/profiles) and Pfam HMM profiles TrbC/VirB2 (PF04956.1) and T4SS_pilin (PF18895.3).

This repository contains:
- The [data](data) used and generated in the study:
    - Patescibacteria proteomes from NCBI RefSeq212 database
    - Multiple sequence alignment of VirB4 homologs used in the phylogenetic reconstruction
    - VirB4 phylogenetic tree file
    - Matrix of patristic distances calculated from the VirB4 phylogenetic tree
    - Custom HMM profiles generated from the Patescibacteria proteome (CPR profiles)
- Python script to parse `hmmscan --domtblout` results 
- Python script to parse the matrix of patristic distances calculated from the VirB4 phylogenetic tree of Patescibacteria 

For detailed information on the methods used and other supplementary material, please find the online supplementary material [Microbial Genomics](https://www.microbiologyresearch.org/content/journal/mgen/10.1099/mgen.0.001409).

# Citation
If you find this work useful, please consider citing us:

Quiñonero-Coronel MDM, Cabello-Yeves PJ, Haro-Moreno JM, Rodriguez-Valera F, Garcillán-Barcia MP. The type IV secretion system of Patescibacteria is homologous to the bacterial monoderm conjugation machinery. Microb Genom. 2025 May;11(5):001409. doi: 10.1099/mgen.0.001409. PMID: 40408144; PMCID: PMC12102498.

```
@article{quinonero2025type,
  title={The type IV secretion system of Patescibacteria is homologous to the bacterial monoderm conjugation machinery},
  author={Qui{\~n}onero-Coronel, Mar{\'\i}a del Mar and Cabello-Yeves, Pedro J and Haro-Moreno, Jose M and Rodriguez-Valera, Francisco and Garcill{\'a}n-Barcia, M Pilar},
  journal={Microbial Genomics},
  volume={11},
  number={5},
  pages={001409},
  year={2025},
  publisher={Microbiology Society}
}
```