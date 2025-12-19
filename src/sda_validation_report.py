import pandas as pd
import os

def generate_engineering_report(file_name):
    # Path Setup
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "..", "data", file_name)
    
    # Load Data
    df = pd.read_csv(file_path)
    total_tests = len(df)
    fail_count = len(df[df['Result'] == 'FAIL'])
    
    # Principle: Calculate Yield and Failure Rate
    yield_rate = ((total_tests - fail_count) / total_tests) * 100
    
    # Principle: Identify the "Weakest Link" (Which axis fails most?)
    axis_analysis = df[df['Result'] == 'FAIL']['Impact_Axis'].value_counts()
    primary_failure_axis = axis_analysis.idxmax() if not axis_analysis.empty else "None"

    # Generate the Report
    print("========================================")
    print("   NVIDIA MECHANICAL RELIABILITY REPORT ")
    print("========================================")
    print(f"Project: Laptop Chassis Drop Simulation")
    print(f"Total Samples Tested: {total_tests}")
    print(f"Current Yield Rate:   {yield_rate:.1f}%")
    print(f"Failure Axis Trend:   {primary_failure_axis}-Axis")
    print("----------------------------------------")
    
    if yield_rate < 95:
        print("STATUS: ❌ RED (Below Mass Production Target)")
        print(f"ACTION REQUIRED: Implement EC for {primary_failure_axis}-Axis vibration.")
    else:
        print("STATUS: ✅ GREEN (Ready for NPI)")
        
    print("========================================\n")

if __name__ == "__main__":
    generate_engineering_report('sda_test_results.csv')