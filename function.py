import pandas as pd
import grafic

project_frame = pd.DataFrame({'Name': [], 'Data': [], 'Enter' : []})
def add_new() :
    shape_data = grafic.shape_date.get()
    shape_enter = grafic.shape_enter.get()
    shape_name = grafic.shape_name.get()

    project_frame.loc[len(project_frame)] = [shape_name, shape_data, shape_enter]
    grafic.consol.delete('1.0', 'end') 
    grafic.consol.insert('1.0', project_frame)

def remove() :
    global project_frame

    shape_row = grafic.remove_row.get()

    project_frame = project_frame.drop(int(shape_row))
    grafic.consol.delete('1.0', 'end')
    grafic.consol.insert('1.0', project_frame)

def export() :
    title = grafic.project_title.get()
    date = grafic.project_date.get()
    project_from = grafic.project_from.get()
    file_name = title + '_' + date + '_' + project_from

    project_frame.to_csv(f'{file_name}.csv')