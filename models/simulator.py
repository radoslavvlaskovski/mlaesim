from etc import reader

vm_start_latency = 0


def classifier():
    # Each classification should include also a way to make decisions
    return

def predictor():

    return



def run(data, update_freq = 0, steps_advance = 0, starting_step = 0, start_vm_number = 1):

    current_step = starting_step
    current_vm_number = start_vm_number
    last_step = len(data)

    # Data in the form of time, value, count
    # Split data into classification + prediction

    while(current_step <= last_step):

        # Run what happens at a single time step
        # Check if new VM started

        # If needed reclassify data

        # Predict

        # Make a decision

        current_step += 1


    return