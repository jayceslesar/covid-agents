
import json
import itertools
import room as Room
from main import viz
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


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


def setup():
    data_path = os.path.join('new_exprs', 'simdata2')
    to_plot = {}
    for i, sim in enumerate(os.listdir(data_path)):
        print(i)
        to_plot[sim] = {}
        splits = sim.replace('.csv', '').split('_')
        # print(splits)
        source_loc = splits[2] + '_' + splits[3]
        sink_loc = splits[5] + '_' + splits[6]
        csv_path = os.path.join(data_path, sim)
        curr_df = pd.read_csv(csv_path)

        raw = []
        ordered_groups = curr_df.groupby(['agent_row', 'agent_col'])
        for name, group in ordered_groups:
            raw.append(group['aerosol_inhaled'].values[-1])

        to_plot[sim]['raw'] = raw
        to_plot[sim]['source'] = source_loc
        to_plot[sim]['sink'] = sink_loc

    with open("auc2.json", "w") as outfile:
        json.dump(to_plot, outfile)


def analyze():
    with open('auc2.json', 'r') as json_file:
        data = json.load(json_file)


    df = pd.DataFrame(columns=['name', 'source', 'sink', 'mean_auc', 'max_auc', 'min_auc', 'median_auc', 'raw', 'loc_string'])

    distrs = {}

    fig = go.Figure()
    for i, sim in enumerate(data.keys()):
        source = data[sim]['source']
        sink = data[sim]['sink']
        mean_val = np.mean(data[sim]['raw'])
        max_val = np.max(data[sim]['raw'])
        min_val = np.min(data[sim]['raw'])
        median_val = np.median(data[sim]['raw'])
        raw = data[sim]['raw']
        loc_string = f"{source}, {sink}"
        df.loc[i] = [sim.replace('.csv', ''), source, sink, mean_val, max_val, min_val, median_val, raw, loc_string]

        if loc_string not in distrs.keys():
            distrs[loc_string] = raw
        else:
            distrs[loc_string] += raw


        fig.add_trace(go.Box(y=np.log10(data[sim]['raw'])))
        # print(source, sink)

    # fig.show()

    sort = df.sort_values(by=['median_auc'])
    index = [i for i in range(len(sort))]
    fig = px.scatter(x=index, y=np.log10(sort['median_auc']))
    # fig.show()
    # print(distrs.keys())
    fig = go.Figure()
    for loc in distrs:
        fig.add_trace(go.Box(y=np.log10(distrs[loc]), name=loc))
    fig.show()


# TODO
# sort for max value for each boxplot
# trace 0, 5, 12, 18, 19, 25, 26, 28 --> anything around 10^-24

# group by source and sink and plot those distributions on boxplots

# next metric --> just median values for each location

# first 25 and last 25 and then every 20 in between --> for next steps of original data
# combine by source sink locations: medians so 6 points per simulation
if __name__ == '__main__':
    analyze()

# PAPER

# INTRODUCTION --> motivation and set scene --> aerosol --> address question how dissemination is determined by souce sink and host location 1 page double space
# methods --> describe model and procedure
# results
# discussion --> first paragraph summary of results, second to last is limitations, conclusion
# appendix --> ideas for future research

# literature search for similar probmlems medline, google scholar --> improves idea that this is important work

# before wednesday

# dont say what we are looking forward to researching

# should be self contained