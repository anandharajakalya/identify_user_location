import geopandas as gpd
from timer import Timer


def execute_pip(geolocdata_points, buildings):
    """
    Perform spatial join to match points and polygons
    :param geolocdata_points: geoDataframe
        Dataframe containing the points.
    :param buildings: geoDataframe
        Dataframe contaiing the polygons.
    :return: geoDataframe
        Dataframe containing matching points and polygons
    """
    t = Timer()
    t.start()
    pointInPoly = gpd.tools.sjoin(geolocdata_points, buildings, op="within", how='left')

    return pointInPoly

