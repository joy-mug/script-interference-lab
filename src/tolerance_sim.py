import numpy as np
import matplotlib.pyplot as plt

def simulate_assembly(iterations=100000):
    # Laptop Heatsink Assembly Simulation
    # Nominal dimensions + Standard Deviation (manufacturing noise)
    chassis_pocket = np.random.normal(50.0, 0.02, iterations)  # 50mm +/- 0.02
    heatsink_width = np.random.normal(49.8, 0.05, iterations)  # 49.8mm +/- 0.05
    
    # Interference occurs if heatsink > chassis pocket
    clearance = chassis_pocket - heatsink_width
    failures = np.sum(clearance < 0)
    
    yield_rate = ((iterations - failures) / iterations) * 100
    return clearance, yield_rate

# Run the test
results, score = simulate_assembly()
print(f"Predicted Production Yield: {score:.2f}%")

# Create a professional plot for your portfolio
plt.hist(results, bins=100, color='green', alpha=0.7)
plt.axvline(x=0, color='red', linestyle='--')
plt.title("Clearance Distribution: Heatsink to Chassis")
plt.xlabel("Clearance (mm)")
plt.ylabel("Units")
plt.show()