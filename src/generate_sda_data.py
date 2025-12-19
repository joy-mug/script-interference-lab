import pandas as pd
import numpy as np
import os

def generate_drop_data(num_tests=100):
    np.random.seed(42) # Keeps results consistent
    
    # Simulate data for 100 drops
    data = {
        'Test_ID': range(1, num_tests + 1),
        'Drop_Height_cm': np.random.choice([76, 100, 120], num_tests),
        'Impact_Axis': np.random.choice(['X', 'Y', 'Z'], num_tests),
        'Peak_G': np.random.normal(120, 15, num_tests).round(2), # Normal distribution around 120G
        'Temperature_C': np.random.uniform(20, 25, num_tests).round(1),
        'Result': ''
    }

    df = pd.DataFrame(data)

    # Logic: If Peak G > 140, it's a "FAILURE" (Mechanical damage)
    df['Result'] = np.where(df['Peak_G'] > 140, 'FAIL', 'PASS')
    
    # Save to CSV for the AI Agent to read later
    df.to_csv('sda_test_results.csv', index=False)
    print("✅ Stage 1 Complete: 'sda_test_results.csv' created with 100 test samples.")
    print(df.head()) # Show first 5 rows

if __name__ == "__main__":
    generate_drop_data()