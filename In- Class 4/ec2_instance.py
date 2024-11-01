# Names : Rohith Yerragunta, Sandeep Dulam
# Group - 12
# date : 1st NOV, 2024
# Sandeep Dulam git link : https://github.com/sandeepdulam19/scripting-cosc1104
# Rohith Yerragunta git link: https://github.com/rohithYerraguntA/scripting-1104/tree/main

#importing json and regular expression libraries
import json
import re

# function for getting the user inputs
def get_input(input_data):

    while True:
        try:
            Value = input(input_data)
            # return the integer value ot float('inf') for no limit
            return int(Value) if Value else float('inf')
        except ValueError:
            print("invalid input. Please enter a valid integer.")

# loading and return the JSON data as a list of dictionaries
def load_instances(filename):

    with open(filename) as file:
        return json.load(file)
    
# instance data parsing to extract values
def instance_data(instance):

    # Extract the number of vCPUs and memory
    vcpu_count = int(re.search(r'(\d+)', instance['vcpu']).group(1))
    memory_size = int(re.search(r'(\d+)', instance['memory']).group(1))
    
    return {
        "name": instance['name'],
        "vcpu": vcpu_count,
        "memory": memory_size,
        "storage": instance['storage'],
        "bandwidth": instance['bandwidth'],
        "availability": instance['availability']
    }

# filtering ec2 instances based on user defined cpu and memory requirements
def filter_instances(instances, min_cpu, max_cpu, min_memory, max_memory):

    return [
        instance_data(instance) for instance in instances
        if min_cpu <= instance_data(instance)['vcpu'] <= max_cpu and min_memory <= instance_data(instance)['memory'] <= max_memory
    ]

#for displaying the filtered list of instances
def display_instances(instances):
    if not instances:
        print("no instances found matching your criteria")
    else:
        print("\n Available EC2 Instances: ")
        for instance in instances:
            print(f"{instance['name']}: {instance['vcpu']} vcpus, {instance['memory']} GiB, " f"{instance['storage']}, {instance ['bandwidth']}, {instance['availability']}")

# main function to run the program
def main():

    # get user input for cpu requirements
    min_cpu = get_input("Minimum CPU Cores: ")
    max_cpu = get_input("Maximum CPU cores (or press enter for no limit): ")

    #get user input for memory requirements
    min_memory = get_input("Minimum memory in GiB: ")
    max_memory = get_input("Maximum memory in GiB (or press enter for no limit): ")

    #load ec2 instance data from json file
    instances = load_instances('ec2_instance_types.json')

    #filter instances based on user defined requirements
    filtered_instances = filter_instances(instances, min_cpu, max_cpu, min_memory, max_memory)

    display_instances(filtered_instances)


if __name__ == "__main__":
    main()

