# Taxonomic Data Analysis

This repository contains a Python script to analyze taxonomic data, produce summary statistics, and create visualizations. The script is containerized using Docker.

## Prerequisites

- Install Docker on your system.

## Dataset Format

The input dataset (`taxonomic_data.csv`) must contain the following columns:
- `species`: The species name.
- `phylum`: The taxonomic phylum.
- `count`: The species count.

Example:

```csv
species,phylum,count
SpeciesA,Firmicutes,120
SpeciesB,Firmicutes,80
SpeciesC,Bacteroidetes,200
```
## Output Directory

All output files will be saved in the `output` directory. Ensure this directory exists in your project structure or is mounted in the Docker container.

### Example Output Files

1. `output/phylum_summary.csv`: Summary statistics of species counts.
2. `output/phylum_species_count.png`: Bar chart visualization of total species count per phylum.
3. `output/phylum_species_proportion.png`: A pie chart showing the proportional distribution of species counts.
4. `output/summary_report.txt`: A plain-text summary report, including; total species count across all phyla and a detailed table of species counts for each phylum.
