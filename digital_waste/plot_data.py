
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
import json


def total_files_size_year(data,year_range_file):
    """
    with the above data need to return a python dict that will contain
    year,file_count, total size of the files per year
    """

    parse_year_counts = []

    for year in year_range_file:
        if year != "unknown":
            print(year)
            size_count = 0
            file_count = 0
            for entry in data:
                    file_year = entry['year']
                    if year == file_year:
                        size_count += int(entry['size'])
                        file_count += 1

            parse_year_counts.append({'year': year,'total_size': size_count, 'total_file': file_count})
    return parse_year_counts


def ploted_data(data):
    years = list(map(lambda x: x['year'],data))
    hd_size = list(map(lambda x: x['total_size'],data))
    count = list(map(lambda x: x['total_file'],data))

    return {'years': years, 'hd_size': hd_size, 'count': count}    

def list_year_size_date(json_list):
    years_collected = list(map(lambda x:{'year': x['year'],'size':x['size'],'ext':x['extension']},json_list))
    return years_collected



def year_file_count_vBar(data_list):
    
    source = ColumnDataSource(data=data_list)
    
    year_sorted = sorted(data_list['years'])
    
    # output to static HTML file
    output_file("lines.html")
    
    # create a new plot with a title and axis labels
    def count():
        p = figure(title="simple line example",plot_width=950, x_axis_label='count', y_axis_label='year', x_range=year_sorted)
        p.vbar(x='years', top='count', width=0.5,color="navy", source=source, legend_label="file count")
        return p
    
    def size():
        p = figure(title="simple line example",plot_width=950, x_axis_label='count', y_axis_label='year', x_range=year_sorted)
        p.vbar(x='years', top='hd_size', width=0.5,color="red", source=source, legend_label="file size")
        return p
    
    file_count=count()
    hd_size = size()

    show(column(file_count,hd_size))

def main():
    file_data = None
    
    
    file =r"C:val_save-full.json"
    data_file = file
    with open(data_file)as f:
        file_data = json.load(f)
    
    
    year_range_file = set(list(map(lambda x: x['year'],file_data)))
    working_data = list_year_size_date(file_data)
    organize_byYear_size_count = total_files_size_year(working_data,year_range_file)
    plot_data_struct  = ploted_data(organize_byYear_size_count)
    year_file_count_vBar(plot_data_struct)
    
    
if __name__ == "__main__":
    main()
