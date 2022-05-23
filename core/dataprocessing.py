from pyrosm import get_data
from pyrosm import OSM
from datetime import datetime
from shapely.geometry.point import Point
import geopandas as gpd
import pandas as pd


def extract_osmdata(region):
    """
    Extracts osm data of the region

    :param region: str
        Name of the place.
    :return: dataframe
        Metatdata of the place.
    """
    regiondata = get_data(region)
    osm = OSM(regiondata)
    buildings = extract_landscapes(osm)
    return buildings

def extract_landscapes(osm):
    """
    Extract only industrial and residential land from singapore
    :param osm:
    :return:
    """
    lands = {"building": ["residential", "industrial"]}
    buildings = osm.get_buildings(custom_filter=lands)
    return buildings

def combine_features(data, new_feature, *features):
    """
    Append the dataframe features together
    :param data: Dataframe
        Dataframe to be manipulated
    :param new_feature: str
        Name of the new feature.
    :param features: list of str
        Name of the features to be combined.
    :return: Dataframe
        Dataframe with the new feature.
    """
    data[new_feature] = list(zip(*features))
    return data

def convert_to_point(data, feature):
    """
    Type convert the latitude and longitude to point form in a dataframe of EPSG:4326
    coordinate system
    :param data: Dataframe
        Dataframe that contains latitude and longitude.
    :param feature: str
        Name of the feature to convert
    :return: geoDataframe
        geoDataframe with latlon points
    """

    data[feature]= data[feature].apply(Point)
    data_points = gpd.GeoDataFrame(data, geometry=feature, crs='EPSG:4326')

    return data_points

def bin_time(data):
    """
    Categorize time feature to Morning and evening
    :param data: Dataframe.
        Data that has the time.
    :return: Dataframe
        Categorized time feature.
    """
    data['Dates'] = pd.to_datetime(data['date']).dt.date
    data['Time'] = pd.to_datetime(data['date']).dt.time

    # binning
    data['time_bins'] = data['Time'].apply(
        lambda x: 'Morning' if (x > (datetime.strptime('06:00', '%H:%M').time()) and
                                (x < datetime.strptime('18:00', '%H:%M').time()))
        else 'Evening')

    return data







