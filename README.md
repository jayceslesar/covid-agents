# Agent Based Covid Model

A heavily paramaterizeable physics simulation to show how aersols spread within enviroments like offices and classrooms

## Parameters: (found in sim_params.json)
- seed: the number to choose the seed for random variables in a simulation
- rows_people: the number of rows for the simulation (should be odd)
- cols_people: the number of cols for the simulation (should be odd)
- have_teacher: boolean value for if there is a teacher in the room (is at the front)
- moving_agent: boolean value to introduce a moving agent into the simulation
- iterations: the number of steps to take
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
- exhale_mask_factor: rate/fraction of exhalation given a mask
- breathe_volume: volume  breathed in
- aerosol_mass: mass in mols per aerosol
- agent_volume: volume the agent takes up in the respective cell
- cell_width: width of the cell (m)
- cell_height: height of the cell (m)
- diffusivity: rate of diffusion
- micro_current_factor: how much micro currents affect diffusivity
- color_upper_limit: cap for the color of a cell (colored by how much infected aerosol is inside)
