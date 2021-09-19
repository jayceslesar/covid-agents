class Cell:
    def __init__(self, row: int, column: int, sim_params: dict, Agent=None):
        """Initialize a cell class

        Args:
            row (int): row of cell
            column (int): column of cell
            Agent ([Agent], optional): Some cells have an Agent. Defaults to None.
            width (float): width of cell
            height (float): height of cell

        """

        # not all cells have Agents
        if Agent is not None:
            self.agent = Agent
            self.production_rate = self.agent.production_rate
        else:
            self.agent = None
            self.production_rate = None

        self.row = row
        self.column = column
        self.color = (255, 255, 255)
        self.concentration = 0
        self.width = sim_params['CELL_WIDTH']  # in meters
        self.height = sim_params['CELL_HEIGHT']  # in meters
        if self.agent == None:
            self.volume = self.width**2*self.height
        else:
            self.volume = self.width**2*self.height - self.agent.volume

        self.real_diffusivity = sim_params["DIFFUSIVITY"]
        self.micro_current_factor = sim_params["MICRO_CURRENT_FACTOR"]
        self.diffusivity = self.micro_current_factor*self.real_diffusivity
        self.color_upper_limit = sim_params["COLOR_UPPER_LIMIT"]

        self.sink = False
        self.source = False
        self.acr = 0

    def get_color(self):
        """Represent the color of the cell by the concentration inside."""
        if self.concentration < 0:
            print("concentration is less than 0!!!!! at", self.row, self.column)
        if self.concentration < (self.color_upper_limit / 2):
            green = 255
            blue = 255
            decrease_factor = 255/(self.color_upper_limit / 2)
            red = 255 - decrease_factor * self.concentration
            color = (red, green, blue)
        else:
            red = 0
            blue = 255
            decrease_factor = 255/(self.color_upper_limit / 2)
            green = 255 - decrease_factor * (self.concentration - (self.color_upper_limit / 2))
            if green >= 0:
                color = (red, green, blue)
            else:
                color = (0, 0, 255)
        return color

    def add_concentration(self, aerosol_mass):
        self.concentration = self.concentration + aerosol_mass/self.volume
        if self.sink:
            self.concentration = 0

    def __str__(self):
        if self.agent is not None:
            return str(self.agent)
        else:
            return 'E'
