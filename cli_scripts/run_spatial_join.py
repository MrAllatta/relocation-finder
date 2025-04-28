"""
CLI script to spatially join rentals with school zones and NTAs.
"""
import argparse

import geopandas as gpd
from spatial_join.join_rentals_to_zones import (
    load_rentals_with_geometry,
    spatial_join_rentals_zones,
)
from utils.helpers import setup_logging

def main():
    """
    Entry point for the spatial join CLI.
    """
    parser = argparse.ArgumentParser(
        description='Spatial join rentals with school zones and NTAs.'
    )
    parser.add_argument(
        '--rentals', required=True, help='Path to rentals CSV with lat/lon.'
    )
    parser.add_argument(
        '--school-zones', required=True, help='Path to school zones CSV with WKT.'
    )
    parser.add_argument(
        '--ntas', required=True, help='Path to NTAs shapefile.'
    )
    parser.add_argument(
        '--output', required=True, help='Path to output CSV with joined data.'
    )
    args = parser.parse_args()
    setup_logging()

    # Load rentals with geometry
    rentals_gdf = load_rentals_with_geometry(args.rentals)
    # Load school zones and NTAs
    school_zones = gpd.read_file(args.school_zones)
    ntas = gpd.read_file(args.ntas)
    # Join rentals to school zones
    rentals_with_zones = spatial_join_rentals_zones(rentals_gdf, school_zones)
    # Join resulting to NTAs
    final_gdf = spatial_join_rentals_zones(rentals_with_zones, ntas)
    # Save results
    # TODO: export final_gdf to CSV or shapefile
    # final_gdf.to_csv(args.output, index=False)
    pass

if __name__ == '__main__':
    main()