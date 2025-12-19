print("Python Interference Lab is Online!")

def intercept_test():
    data = "Original Secret Data"
    # Simple simulation of interfering with data
    interfered_data = data.replace("Original", "MODIFIED")
    print(f"Result: {interfered_data}")

intercept_test()