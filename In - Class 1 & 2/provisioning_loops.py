# Names : Rohith Yerragunta, Sandeep Dulam
# Group - 12
# date : 27th Sep, 2024
# Sandeep Dulam git link : https://github.com/sandeepdulam19/scripting-cosc1104
# Rohith Yerragunta git link: https://github.com/rohithYerraguntA/scripting-1104/tree/main
'''
Description: This code allows user to provision resources for multiple times and also checks if the entered value
is either a valid input.
'''

# Total number of CPU cores and amount of memory available in GB
cpu_cores_max = 16
memory_max = 500

# utilized resources 
cpu_cores_utilized = 0
memory_utilized = 0.0

# allocated and pending resources list
resources_allocated = []
requests_pending = []
 
# loop to take inputs and to check the limits of the resources
while True:    
    username = input("enter your username: ")
    requested_cpu_cores = int(input("enter number of cpu cores required (1 - 16): "))
    requested_memory = float(input("enter amount of memory (1 - 500): "))
    
    if requested_cpu_cores > 0 and requested_memory > 0 and requested_cpu_cores <= cpu_cores_max and requested_memory <= memory_max :
        cpu_cores_left = cpu_cores_max - cpu_cores_utilized
        memory_left = memory_max - memory_utilized
        
        # loop for allocating resources
        if requested_cpu_cores <= cpu_cores_left and requested_memory <= memory_left:
            resources_allocated.append({"user":username, "cpu_cores":requested_cpu_cores, "memory":requested_memory})
            cpu_cores_utilized += requested_cpu_cores
            memory_utilized += requested_memory
       
        else:
            requests_pending.append({"username":username, "cpu_cores":requested_cpu_cores, "memory":requested_memory})
    else:
        print("enter a valid number within limit ")     
        
# asking the user if they want to continue provisioning              
    additional_request = input("do you want to make another request? (yes/no): ").lower()
    if additional_request != "yes":
        break
    
# final list of allocated and pending resources
print("\nallocated resources:")
for resource in resources_allocated:
    print(f"username:{resource['user']}, cpu cores:{resource['cpu_cores']}, Memory:{resource['memory']} GB")

print("\nPending Requests:")
for request in requests_pending:
    print(f"username:{request['username']}, cpu cores:{request['cpu_cores']}, Memory:{request['memory']} GB")
   
    
    
    