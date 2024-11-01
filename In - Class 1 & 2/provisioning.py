# Names : Rohith Yerragunta, Sandeep Dulam
# Group - 12
# date : 27th Sep, 2024
# Sandeep Dulam git link : https://github.com/sandeepdulam19/scripting-cosc1104
# Rohith Yerragunta git link: https://github.com/rohithYerraguntA/scripting-1104/tree/main
'''
Description: This python script determines cloud resource provisioning system.
This allows the user to request for cloud resources and the program will
check if requested are accessible according to availability.
'''

# Total number of CPU cores and amount of memory available in GB
CPU_cores_available = 16
memory_available = 500

# User input
required_CPU_cores = int(input('Enter the number of required CPU cores (1 - 16): '))
required_memory = float(input("enter the required memory (1 - 16): "))

# if condition for checking limits
if required_CPU_cores > 0 and required_memory > 0 and required_CPU_cores <= CPU_cores_available and required_memory <= memory_available: 

# if condition to allocate resources   
    
    if required_CPU_cores <= CPU_cores_available and required_memory <= memory_available:
        print('resources provisioned successfully')
        cpu_cores_left = CPU_cores_available - required_CPU_cores
        memory_left = memory_available - required_memory
        print(" cpu cores left = ",cpu_cores_left )
        print(" memory left = ", memory_left)
    else:
        print('resources request exceeds capacity. Provisioing failed')
        print(" cpu cores left = ", CPU_cores_available)
        print(" memory left = ", memory_available)

else: 
    print('enter a valid number within limit')
    
    
    

    

