Reference_voltage = float(input("Enter Reference Voltage: "))
Highest_Value = float(input("Enter Highest value: "))
Step_size = Reference_voltage / Highest_Value
ADC_value = float(input("Enter ADC value: "))
Voltage = ADC_value * Step_size
print(f"{Voltage:.2f} V")
