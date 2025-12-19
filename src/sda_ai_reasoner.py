import pandas as pd

def sda_ai_agent(file_path):
    # Load the data we generated in Stage 1
    df = pd.read_csv(file_path)
    
    # Filter only the failures (Peak G > 140)
    failures = df[df['Result'] == 'FAIL']
    
    print(f"--- AI Agent Analysis: {len(failures)} Mechanical Failures Detected ---")
    
    for index, row in failures.iterrows():
        # This is where the "Agent Logic" happens
        print(f"\n[Test ID {row['Test_ID']}] Impact Axis: {row['Impact_Axis']} | G-Force: {row['Peak_G']}")
        
        if row['Impact_Axis'] == 'X':
            print("AI Recommendation: Lateral shock exceeded limit. EC: Strengthen side-wall ribs.")
        elif row['Impact_Axis'] == 'Y':
            print("AI Recommendation: Vertical drop impact high. EC: Increase damping pad thickness by 0.2mm.")
        else:
            print("AI Recommendation: Z-axis torsion detected. EC: Add 2 extra screws to the D-shell.")

if __name__ == "__main__":
    sda_ai_agent('sda_test_results.csv')