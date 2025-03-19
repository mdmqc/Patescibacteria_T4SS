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

For detailed information on the methods used and other supplementary material, please find a preprint version on [BioRxiv](https://doi.org/10.1101/2025.01.22.634366).

# Citation
If you find this work useful, please consider citing us:

Quinonero-Coronel, M. D. M., Cabello-Yeves, P. J., Haro-Moreno, J. M., Rodriguez-Valera, F., & Garcillan-Barcia, M. P. (2025). The Type IV Secretion System of Patescibacteria is homologous to the bacterial monoderm conjugation machinery. bioRxiv, 2025-01.

```
@article{quinonero2025type,
  title={The Type IV Secretion System of Patescibacteria is homologous to the bacterial monoderm conjugation machinery},
  author={Quinonero-Coronel, Maria del Mar and Cabello-Yeves, Pedro J and Haro-Moreno, Jose M and Rodriguez-Valera, Francisco and Garcillan-Barcia, M Pilar},
  journal={bioRxiv},
  pages={2025--01},
  year={2025},
  publisher={Cold Spring Harbor Laboratory}
}
```