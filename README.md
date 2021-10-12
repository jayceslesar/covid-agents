# Agent Based Covid Model

A heavily paramaterizeable physics simulation to show how aersols spread within enviroments like offices and classrooms

One individual is 'infected' and releases infected aerosols into the room. Using diffusion the model determines where the 'infected' aerosols \
move to.

![Alt text](assets/img.jpg?raw=true "Title")

## Parameters: (found in sim_params.json)
- seed: the number to choose the seed for random variables in a simulation
- rows_people: the number of rows for the simulation (should be odd)
- cols_people: the number of cols for the simulation (should be odd)
- have_teacher: boolean value for if there is a teacher in the room (is at the front)
- moving_agent: boolean value to introduce a moving agent into the simulation
- iterations: the number of steps to take (each iteration/setp is a second if step_size is set to one)
- fan_cycles: a paramater to control the fan animation
- window_height: size paramater for the simulation visualization
- window_width: size paramater for the simulation visualization
- source_row: the row that the source is in
- source_col: the column that the source is in (produces air into the system -- the fan)
- source_ach: the air changes per hour of the source
- sink_row: the row that the sink is in
- snk_col: the column that the sink is in (takes in and evacuates air at a rate)
- sink_ach: the air changes per hour of the sink
- mic: boolean valuue if the teacher has a microphone or not (cuts production rate in half if true)
- inhale_mask_factor: the starting rate/fraction of inhaling given an agent has a mask
- exhale_mask_factor: rate/fraction of exhalation given a mask (N95 masks reduce outtake by 95% and so on...)
- breathe_volume: volume breathed in --> (concentration*.0005 cubic meters)*.233 seconds
- aerosol_mass: mass in mols per aerosol (kg)
- agent_volume: volume the agent takes up in the respective cell (cubic meters)
- cell_width: width of the cell (m)
- cell_height: height of the cell (m)
- diffusivity: rate of diffusion (meters squared/second)
- micro_current_factor: how much micro currents affect diffusivity
- color_upper_limit: cap for the color of a cell (colored by how much infected aerosol is inside)

Production rates from https://www.medrxiv.org/content/10.1101/2021.02.07.21251309v2.full.pdf

# How to Run:

Running `main.py` with a configuration of `sim_params.json` will run the model.
Upon running, it will ask if you would

