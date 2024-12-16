# Taxonomic Data Analysis

This repository contains a Python script to analyze taxonomic data, produce summary statistics, and create visualizations. The script is containerized using Docker.

---

## Prerequisites

- Install Docker on your system.

---

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
---

## Output Directory

All output files will be saved in the `output` directory. Ensure this directory exists in your project structure or is mounted in the Docker container.

### Example Output Files

1. `output/phylum_summary.csv`: Summary statistics of species counts.
2. `output/phylum_species_count.png`: Bar chart visualization of total species count per phylum.
3. `output/phylum_species_proportion.png`: A pie chart showing the proportional distribution of species counts.
4. `output/summary_report.txt`: A plain-text summary report, including; total species count across all phyla and a detailed table of species counts for each phylum.

---

## Instructions to Run the Script

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/conorcremin93/Taxonomic_Analysis.git
cd Taxonomic_Analysis
```
---

### Step 2: Prepare the Dataset

Ensure your dataset (`taxonomic_data.csv`) is in the data directory. If the data directory does not exist, create it:

```bash
mkdir data
cp /path/to/taxonomic_data.csv data/
```
---

### Step 3: Create the Output Directory

Create an `output` directory if it doesn’t already exist:

```bash
mkdir output
```
---

### Step 4: Build the Docker Image

Build the Docker image:

```bash
docker build -t taxonomic_analysis .
```
---

### Step 5: Run the Docker Container

Run the container with the following command, replacing paths as needed for your system:

On Windows:
```bash
docker run --rm -v "C:/path/to/Taxonomic_Analysis/data:/app/data" -v "C:/path/to/Taxonomic_Analysis/output:/app/output" taxonomic_analysis
```
On Linux or MacOS:
```bash
docker run --rm -v "$(pwd)/data:/app/data" -v "$(pwd)/output:/app/output" taxonomic_analysis
```
---

### Step 6: After the script runs successfully, check the output directory for the output files:

These files provide summary statistics, visualizations, and a text report of the analysis.