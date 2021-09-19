import numpy as np


class Agent:
    def __init__(self, number: int, row: int, col: int, seed: int, production_rate: float, sim_params: dict):
        # np.random.seed(seed)
        """
        Agent constructor

        Args:
            number (int): the ID of the agent
            row (int): row index
            col (int): col index
            seed (int): the seed to use
            masktype (str): type of mask -> None, 'N95', 'cloth', 'double; (assumes double is cloth over surgical)
        """
        self.number = number
        self.row = row
        self.col = col
        # for how much concentration of virus agent is producing at a given time
        self.breathe_volume = sim_params["BREATHE_VOLUME"]
        self.breathe_per_second = sim_params["BREATHE_PER_SECOND"]
        # mask effectiveness
        self.exhale_mask_factor = sim_params["EXHALE_MASK_FACTOR"]
        self.inhale_mask_factor = sim_params["INHALE_MASK_FACTOR"]
        # NOTE: aerosol mass is for found using formula for a sphere
        self.production_rate = (production_rate * self.breathe_volume * self.breathe_per_second*sim_params["AEROSOL_MASS"]) * self.exhale_mask_factor
        self.intake_per_step = self.breathe_per_second * self.breathe_volume * self.inhale_mask_factor

        # tracking variables for run specific decisions
        self.untouched = True
        self.infectious = False
        self.recovered = False
        self.exposed = False
        self.volume = sim_params["AGENT_VOLUME"]

        # counter variables for run specific desicions
        self.total_exposure = 0  # for stat tracking
        self.steps_exposed = 0
        self.steps_infectious = 0

        # TODO: Figure out if we want to keep any of this
        # stats for network
        self.num_infected = 0  # for stat tracking

        # random attributes:
        # the age of an agent
        self.age = np.random.randint(1, 70)

        #  how big of a radius can they infect others in
        self.neighborhood_size = np.random.uniform(0.5, 3)

        # All of these are initialized here but set in Space.py for speed
        # the number of steps the agent remains infective for
        self.INFECTIVE_LENGTH = None

        # the number of steps the agent takes from initial exposure to being infective
        self.INCUBATION_PERIOD = None  # TODO:: guassian 0 to 3 days with tail to 7

        # pre-existing condition float
        if np.random.randint(0, 1):
            self.pre_existing_float = np.random.uniform(0, 1)
        else:
            self.pre_existing_float = 0

        # random probability that someone will be infected :: UNIMPLEMENTED
        self.PROBABILITY_OF_INFECTION = None  # for math later
        self.infectiveness = None  # how likely to infect another

        # network specific class variables
        self.agent_who_exposed_me = None
        self.agent_who_infected_me = None
        self.agents_infected = []
        self.agents_infected_iterations = []
        self.total_infected = 0
        self.iteration_infected = None
        self.iteration_recovered = None

        # UNIMPLEMENTED
        self.tested_since_last_step = None
        self.lag_from_contact_tracing = None
        self.currently_quarantined = False

    def __str__(self):
        if self.infectious:
            return "I"
        if self.recovered:
            return "R"
        if self.exposed:
            return "E"
        if not self.infectious:
            return "O"
        if self.currently_quarantined:
            return "Q"

    def get_color(self):
        if self.infectious:  # red
            return (255, 0, 0)
        if self.recovered:  # dark green
            return (61, 99, 17)
        if self.exposed:  # yellow
            return (250, 247, 36)
        if not self.infectious:  # red
            return (0, 255, 0)
        if self.currently_quarantined:  # purple
            return (147, 112, 219)

    def get_color_string(self):
        if self.infectious:  # red
            return "red"
        if self.recovered:  # dark green
            return "dark_green"
        if self.exposed:  # yellow
            return "yellow"
        if not self.infectious:  # red
            return "green"
        if self.currently_quarantined:  # purple
            return "purple"
