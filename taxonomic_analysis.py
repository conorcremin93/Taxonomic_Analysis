import pandas as pd
import matplotlib.pyplot as plt
import os

# Input and output file paths
INPUT_FILE = os.getenv("INPUT_FILE", "./data/taxonomic_data.csv")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./output/")
OUTPUT_STATS_FILE = os.path.join(OUTPUT_DIR, "phylum_summary.csv")
OUTPUT_PLOT_FILE = os.path.join(OUTPUT_DIR, "phylum_species_count.png")

def analyze_taxonomic_data(input_file, output_stats_file, output_plot_file):
    try:
        # Ensure the output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Load the dataset
        data = pd.read_csv(input_file)

        # Ensure required columns are present
        if 'phylum' not in data.columns or 'count' not in data.columns:
            raise ValueError("Dataset must contain 'phylum' and 'count' columns.")

        # Handle missing or invalid data
        data = data.dropna(subset=['phylum', 'count'])
        data['count'] = pd.to_numeric(data['count'], errors='coerce')
        data = data.dropna(subset=['count'])

        # Group by Phylum and calculate statistics
        summary = data.groupby('phylum')['count'].agg(
            Total_Species_Count='sum',
            Average_Species_Per_Species='mean',
            Standard_Deviation='std'
        ).reset_index()

        # Add a rank column based on Total Species Count
        summary['Rank'] = summary['Total_Species_Count'].rank(ascending=False, method='dense').astype(int)
        summary = summary.sort_values(by='Rank')

        # Calculate total species count
        total_species_count = summary['Total_Species_Count'].sum()
        print(f"Total species count across all phyla: {total_species_count}")

        # Print the summary table to the console
        print("\nSummary Table:")
        print(summary.to_string(index=False))

        # Save the summary table to a CSV file
        summary.to_csv(output_stats_file, index=False)
        print(f"Summary statistics saved to {output_stats_file}")

        # Generate bar chart
        plt.figure(figsize=(10, 6))
        bars = plt.bar(summary['phylum'], summary['Total_Species_Count'], color=['#5DADE2', '#58D68D', '#F5B041', '#AF7AC5'])
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f"{yval}", ha='center', va='bottom', fontsize=10, fontweight='bold')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.xlabel('Phylum', fontsize=12, fontweight='bold')
        plt.ylabel('Total Species Count', fontsize=12, fontweight='bold')
        plt.title('Total Species Count per Phylum', fontsize=14, fontweight='bold')
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.tight_layout()
        plt.savefig(output_plot_file)
        print(f"Bar chart saved to {output_plot_file}")

        # Generate pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(summary['Total_Species_Count'], labels=summary['phylum'], autopct='%1.1f%%',
                startangle=140, colors=['#5DADE2', '#58D68D', '#F5B041', '#AF7AC5'], wedgeprops={'edgecolor': 'white'})
        plt.title('Proportional Distribution of Total Species Count by Phylum', fontsize=14, fontweight='bold')
        plt.tight_layout()
        pie_chart_file = os.path.join(OUTPUT_DIR, "phylum_species_proportion.png")
        plt.savefig(pie_chart_file)
        print(f"Pie chart saved to {pie_chart_file}")

        # Write a summary report to a text file
        report_file = os.path.join(OUTPUT_DIR, "summary_report.txt")
        with open(report_file, 'w') as f:
            f.write("Summary Report: Taxonomic Analysis\n")
            f.write("=" * 40 + "\n\n")
            f.write(f"Total species count across all phyla: {total_species_count}\n\n")
            f.write("Species Count by Phylum:\n")
            f.write(summary.to_string(index=False) + "\n")
        print(f"Summary report saved to {report_file}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    analyze_taxonomic_data(INPUT_FILE, OUTPUT_STATS_FILE, OUTPUT_PLOT_FILE)
