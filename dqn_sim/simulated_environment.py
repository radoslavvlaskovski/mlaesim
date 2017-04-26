

class Simulation:

    def __init__(self, life_data, observation_length):

        self.life_data = life_data
        self.current_timestep = 0
        self.current_cpu_status = self.life_data[0]
        self.life_time = len(life_data)
        self.n = observation_length
        self.current_observation = life_data[self.current_timestep: self.current_timestep + self.n]


    def start_next_timestep(self):

        if self.current_timestep < self.life_time:
            self.current_timestep += 1
            self.current_cpu_status = self.life_data[self.current_timestep]
            self.current_observation = self.life_data[self.current_timestep: self.current_timestep + self.n]


    def get_current_observation(self):

        return self.current_observation

    def get_current_cpu_status(self):

        return self.current_cpu_status

    ## TODO
    def plot_data(self):
        return