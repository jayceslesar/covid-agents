import json
import itertools
import room as Room
from main import viz


with open('sim_params.json') as f:
    sim_params = json.load(f)



def get_all_coords(x, y):
    rows = list(range(y))
    cols = list(range(x))
    coords = []


    for i in rows:
        for j in cols:
            if i % 2 !=0 and j % 2 != 0:
                continue
            coords.append((i, j))
    combos = list(itertools.combinations(coords, 2))
    return combos


# each simulation is a half hour

def main():
    experiments = get_all_coords(6, 13)
    times = len(experiments)
    for i, experiment in enumerate(experiments):
        print(f'{i}/{times}')
        source, sink = experiment

        sim_params['SOURCE_ROW'] = int(source[0])
        sim_params['SOURCE_COL'] = int(source[1])

        sim_params['SINK_ROW'] = int(sink[0])
        sim_params['SINK_COL'] = int(sink[1])
        room = Room.Room(sim_params)

        name = f'SOURCE_{source[0]}_{source[1]}_SINK_{sink[0]}_{sink[1]}'
        viz(room, name=name, screenshots='N')

if __name__ == '__main__':
    main()