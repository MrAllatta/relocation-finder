"""
Module for spatially joining rental listings with school zones and NTAs.
"""
import pandas as pd
import geopandas as gpd

def load_rentals_with_geometry(rentals_csv_path: str) -> gpd.GeoDataFrame:
    """
    Load rentals CSV and convert to GeoDataFrame with point geometries.

    Args:
        rentals_csv_path: Path to CSV containing rental listings with lat/lon.

    Returns:
        GeoDataFrame of rentals with geometry column.
    """
    # TODO: read CSV, create geometry column using geopandas.points_from_xy
    pass

def spatial_join_rentals_zones(
    rentals_gdf: gpd.GeoDataFrame,
    zones_gdf: gpd.GeoDataFrame
) -> gpd.GeoDataFrame:
    """
    Perform spatial join between rentals and provided zone geometries.

    Args:
        rentals_gdf: GeoDataFrame of rentals.
        zones_gdf: GeoDataFrame of zones (school zones or NTAs).

    Returns:
        GeoDataFrame of rentals with joined zone attributes.
    """
    # TODO: implement spatial join (e.g., gpd.sjoin)
    pass