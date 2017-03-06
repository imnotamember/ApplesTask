import os

def create_data_file(
        experiment_info,
        task_name,
        header='Participant number, Cumulative trial number, Trial number, Block number, Task, ImageL, ImageR, StimL, '
               'StimR, Correct Response, Response, Correct, Accuracy, Response Time by trial, Response Time by stim, '
               'Trial time, Trial Type, SOA'):
    file_name = experiment_info['Participant'] + '-' + experiment_info['date'] + '-' + task_name + '.csv'
    folder_name = os.path.join('Data', experiment_info['Participant'], '')
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_path = '%s%s' % (folder_name, file_name)
    with open(file_path, 'w') as f:
        f.write(header)
        f.write('\n')
    return file_path


def write_data(filename, data):
    with open(filename, 'a') as f:
        row_string = ",".join(map(str, data))
        f.write(row_string + '\n')

