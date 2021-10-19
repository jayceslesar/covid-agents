# Agent Based Covid Model
Created: February 1, 2021 \n
Last Updated: October 13, 2021 \n

Authors: Jayce Slesar, Brandon Lee, and Carter Ward \n
Advisors: Jason H. T. Bates, John P. Hanley, and Vitor Mori \n
Affiliation: University of Vermont. \n

This model was created to simulate the risk of infection to a disease primarily transmitted through aerosols of susceptible individuals in a classroom or office. The model is based on the physics of diffusion and hydraulics and is highly parameterizable allowing for users to tailor simulations.
A heavily paramaterizeable physics simulation to show how aersols spread within enviroments like offices and classrooms

Example output of 3 different simulations (each of these simulations can be recreated using the following json files A: "Jayce add file name"; B: "Jayce add file name"; C: "Jayce add file name") :

![Exaple](assets/blanket.png)

## Parameters: (found in sim_params.json) with units
### IMPORTANT: The self.time_length variable in room.py controls the time step. Keeping it at 1 means that each step is 1 second.

| Parameter | Description | Data Type | Default |
| -------- | -----------| ------------| ------- |
| seed | number to seed the simulation with | integer | 42 |
| rows_people | number of rows in the grid | integer | 5 |
| cols_people | number of columns in the grid | integer | 5 |
| have_teacher | will the simulation have a teacher | boolean (true, false) | true |
| moving_agent | will the simulation have a moving agent | boolean (true, false) | false |
| iterations | the number of steps to run the simulation | integer | 3600 |
| fan_cycles | controls the fan animation, don't need to mess with this | integer | 4 |
| window_height | for controlling the size of a cell in the visual, no need to change | integer (pixels) | 800 |
| window_width | for controlling the size of a cell in the visual, no need to change | integer (pixels) | 800 |
| source_row | the row that the source is in (the fan which moves air around) | integer | 12 |
| source_col | the column that the source is in (the fan which moves air around) | integer | 5 |
| source_ach | the air changes per hour of the source | ACH (air changes / hour) | 3 |
| sink_row | the row that the sink is in (the sink image that takes in air) | integer | 0 |
| sink_col | the column that the sink is in (the sink image that takes in air) | integer | 5 |
| sink_ach | the air changes per hour of the source | ACH (air changes / hour) | 4 |
| mic | value to set the teacher have a microphone or not, affects how loudly they are speaking and reduces output of aerosol | boolean (true, false) | false |
| inhale_mask_factor | the affect in terms of % that a mask makes on inhaling for a given agent | float [0, 1] | 1 |
| exhale_mask_factor | the affect in terms of % that a mask makes on exhaling for a given agent | float [0, 1] | 0.05 |
| breathe_volume | volume breathed in per step | (concentration*.0005 cubic meters)*seconds | 0.233 |
| aerosol_mass | mass of a given aerosol | killograms | 5.445427e-20 |
| agent_volume | how much volume an agent takes up in their cell | cubic meters | 0.062 |
| cell_width | width of a cell on the grid | meters | 1 |
| cell_height | height of a cell on the grid | meters | 3 |
| diffusivity | rate of diffusion | square meters per second | 2.83e-5 |
| micro_current_factor | interaction term for micro currents on diffusivity | | 1000 |
| color_upper_limit | limit on cell color for visualization | float | 0.00000000000000000000075 |

An example of a paramater setup can be found in `sim_params.json`. Editing this file will result in a changed simulation.

Production rates from https://www.medrxiv.org/content/10.1101/2021.02.07.21251309v2.full.pdf

# Installation:
Required: python3 and pip

`$ git clone https://github.com/jayceslesar/covid-agents.git` \
`$ cd covid-agents` \
Use of virtual environment is recommended \
`$ pip install -r requirements.txt`

# How to Run:

Running `main.py` with a configuration of `sim_params.json` will run the model.
Upon running, it will ask if you would like to save the data into a directory. Screenshots can be saved to create a .gif of the model run (state how screenshots can be saved). \
A visual will appear to show the current state of the simulation. Darker blue means a greater concentration of an aerosol that contains an infectious agent (e.g., SARS-CoV-2).
Ex: `python3 main.py` will run a simulation and show the visual.

lines after questions are where the user (you enters answers) \
$ python3 main.py \
pygame 2.0.2 (SDL 2.0.16, Python 3.8.11) \
Hello from the pygame community. https://www.pygame.org/contribute.html \
Simulation will run for 3600 steps. \
What would you like to name the data file? some_data \
do you want screenshots? \
y \
What folder do you want to save your screenshots into? Please specify the path \
save_screenshots \
How many steps between screenshots? \
10


# General Usage:

Users will generally want to simulate an environment that most resembles a room that they plan on working and/or teaching in. Therefore, users should familiarize themselves with the parameters listed above so that the simulation most closely resembles the system they choose to model. \
The data output into the `data` folder is a csv where each row is a different cell with an agent at a timestep. Blank spaces are excluded so it is easier to analyze how much total infected aerosol a given agent as inhaled.

# References:
Production Rates: \
https://www.medrxiv.org/content/10.1101/2021.02.07.21251309v2.full.pdf \
https://www.pnas.org/content/118/8/e2021830118 \

Breath Capacity: \
https://www.bbc.co.uk/bitesize/guides/z3xq6fr/revision/2#:~:text=Tidal%20volume%20(TV)%20is%20the,is%206%20litres%20per%20minute \

Breaths per Minute: \
https://www.hopkinsmedicine.org/health/conditions-and-diseases/vital-signs-body-temperature-pulse-rate-respiration-rate-blood-pressure#:~:text=Normal%20respiration%20rates%20for%20an,to%2016%20breaths%20per%20minute \

Inactivation Rate of COVID-19: \
https://www.reuters.com/article/us-health-coronavirus-study/coronavirus-can-persist-in-air-for-hours-and-on-surfaces-for-days-study-idUSKBN2143QP \

Aerosol Info: \
https://www.cdc.gov/niosh/topics/aerosols/pdfs/Aerosol_101.pdf \
http://web.mit.edu/fluids-modules/www/low_speed_flows/2-7Aerosol.pdf \

Production Rates: \
https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2768712 \
https://academic.oup.com/cid/advance-article/doi/10.1093/cid/ciaa1283/5898624 \


