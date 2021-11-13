
import json
import itertools
import room as Room
from main import viz


with open('sim_params.json') as f:
    sim_params = json.load(f)


first_50_source_locs = [(2, 2), (2, 3), (2, 2), (2, 2), (2, 3)]
first_50_sink_locs = [(10, 5), (12, 5), (7, 4), (8, 3), (12, 1)]

last_50_source_locs = [(3, 0), (0, 0), (0, 0), (0, 0), (1, 0)]
last_50_sink_locs = [(6, 0), (11, 2), (12, 2), (10, 0), (10, 1)]


def first():
    infected_locs = [(11, 5), (1, 1), (1, 9), (9, 1), (9, 9)]
    for i in range(len(first_50_source_locs)):
        source = first_50_source_locs[i]
        sink = first_50_sink_locs[i]

        sim_params['SOURCE_ROW'] = int(source[0])
        sim_params['SOURCE_COL'] = int(source[1])

        sim_params['SINK_ROW'] = int(sink[0])
        sim_params['SINK_COL'] = int(sink[1])

        for infected_loc in infected_locs:
            sim_params['INFECTED_AGENT_LOCS'] = [list(infected_loc)]
            room = Room.Room(sim_params)

            name = f'FIRST_SOURCE_{source[0]}_{source[1]}_SINK_{sink[0]}_{sink[1]}_INFECTED_{infected_loc[0]}_{infected_loc[1]}'
            viz(room, name=name, screenshots='N')


def last():
    infected_locs = [(11, 5), (1, 1), (1, 9), (9, 1), (9, 9)]
    for i in range(len(first_50_source_locs)):
        source = last_50_source_locs[i]
        sink = last_50_source_locs[i]

        sim_params['SOURCE_ROW'] = int(source[0])
        sim_params['SOURCE_COL'] = int(source[1])

        sim_params['SINK_ROW'] = int(sink[0])
        sim_params['SINK_COL'] = int(sink[1])

        for infected_loc in infected_locs:
            sim_params['INFECTED_AGENT_LOCS'] = [list(infected_loc)]
            room = Room.Room(sim_params)

            name = f'LAST_SOURCE_{source[0]}_{source[1]}_SINK_{sink[0]}_{sink[1]}_INFECTED_{infected_loc[0]}_{infected_loc[1]}'
            viz(room, name=name, screenshots='N')

if __name__ == '__main__':
    first()
    last()