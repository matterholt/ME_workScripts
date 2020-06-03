"""
Created on Tue Jun  2 09:02:18 2020

@author: MATTERHOLT
question for analysis report

1. what files are being stored
    - what type? , what year?, space taken up on hard drive
"""
from bokeh.plotting import figure, output_file, show
import json


def year_summary(year_list):
    list_summary = {}

    for year in year_list:
        list_summary[year] = list_summary.get(year, 0)+1

    return list_summary


def year_count(data_struct):
    """
    reduce object to a list of years
    """
    year = []
    for key in data_struct['file_data']:
        year.append(key['year'])

    summary = year_summary(year)
    return summary


def bar_graph(inputs):
    output_file("year_count.html")

    years = list(inputs.keys())
    year_freq = list(inputs.values())

    # sort by data
    year_sort = sorted(years)

    p = figure(plot_width=400, plot_height=400, x_range=year_sort)

    p.vbar(x=years, top=year_freq, width=0.5, color="navy", alpha=0.5)

    show(p)


def main(file_inventory):

    section_one = file_inventory[0]

    section_year_count = year_count(section_one)

    bar_graph(section_year_count)


if __name__ == "__main__":
    file_data = None

    data_file = r"sample.json"
    with open(data_file)as f:
        file_data = json.load(f)

    main(file_data)
