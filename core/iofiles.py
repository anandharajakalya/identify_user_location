import pandas as pd

def read_csv(path_to_data):
    """
    read a comma seperated file into pandas dataframe
    path_to_data: location of the csvfile to be read
    :return: read output
    """
    data = pd.read_csv(path_to_data)
    return data

def to_csv(data, path_to_file):
    """
        write the data to csv
    :param data: Dataframe
        Data to be written to csv.
    :param path_to_file: str
        Path of the file to be written.
    :return: None
    """
    data.to_csv(path_to_file)

    return