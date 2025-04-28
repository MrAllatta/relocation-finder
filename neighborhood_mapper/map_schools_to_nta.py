"""
Module for mapping schools to Neighborhood Tabulation Areas (NTAs).
"""
import pandas as pd
import geopandas as gpd

def load_school_zones(csv_wkt_path: str) -> gpd.GeoDataFrame:
    """
    Load school zone shapefile data from CSV with WKT geometries.

    Args:
        csv_wkt_path: Path to CSV containing WKT geometry column.

    Returns:
        GeoDataFrame of school zones.
    """
    # TODO: parse CSV and convert WKT to geometry
    pass

def load_ntas(shapefile_path: str) -> gpd.GeoDataFrame:
    """
    Load NTA (Neighborhood Tabulation Area) shapefile.

    Args:
        shapefile_path: Path to NTA shapefile.

    Returns:
        GeoDataFrame of NTAs.
    """
    # TODO: read shapefile into GeoDataFrame
    pass

def map_schools_to_nta(
    schools_gdf: gpd.GeoDataFrame,
    nta_gdf: gpd.GeoDataFrame
) -> gpd.GeoDataFrame:
    """
    Spatially join school locations to NTAs.

    Args:
        schools_gdf: GeoDataFrame of schools with point geometries.
        nta_gdf: GeoDataFrame of NTAs.

    Returns:
        GeoDataFrame of schools with NTA attributes.
    """
    # TODO: implement spatial join between schools and NTAs
    pass