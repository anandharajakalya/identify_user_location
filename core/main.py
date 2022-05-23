import dataprocessing, iofiles, algorithm
import definitions, os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # download osm data for singapore(only residential and industrial)
    buildings = dataprocessing.extract_osmdata("singapore")

    geolocdata = iofiles.read_csv(os.path.join(definitions.ROOT_DIR, "data\geolocationdata.csv"))
    geolocdata_features = dataprocessing.bin_time(geolocdata)


    geolocdata_new = dataprocessing.combine_features(geolocdata_features, 'coordinates', geolocdata_features.latitude,
                                                     geolocdata_features.longitude)

    geopoints = dataprocessing.convert_to_point(geolocdata_new, 'coordinates')


    # Execute point in polygon
    results = algorithm.execute_pip(geopoints, buildings)

    iofiles.to_csv(results, '../data/results.csv')

