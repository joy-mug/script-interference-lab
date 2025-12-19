import pandas as pd
import matplotlib.pyplot as plt
import os

def visualize_sda(file_name):
    # Setup paths
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "..", "data", file_name)
    
    # Load data
    df = pd.read_csv(file_path)
    
    # Create a Scatter Plot: Drop Height vs Peak G
    plt.figure(figsize=(10, 6))
    
    # Color code: Pass = Green, Fail = Red
    colors = {'PASS': 'green', 'FAIL': 'red'}
    
    plt.scatter(df['Drop_Height_cm'], df['Peak_G'], 
                c=df['Result'].map(colors), alpha=0.6, edgecolors='w', s=100)
    
    plt.axhline(y=140, color='r', linestyle='--', label='Failure Threshold (140G)')
    plt.title('NVIDIA Portfolio: SDA Drop Test Analysis', fontsize=14)
    plt.xlabel('Drop Height (cm)', fontsize=12)
    plt.ylabel('Peak Impact (G-force)', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    
    # Save the chart to the data folder
    save_path = os.path.join(base_path, "..", "data", "sda_chart.png")
    plt.savefig(save_path)
    print(f"✅ Chart generated and saved to: {save_path}")
    plt.show()

if __name__ == "__main__":
    visualize_sda('sda_test_results.csv')