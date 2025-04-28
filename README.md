 # Relocation Finder

 A data-first, human-centered tool to help relocating families identify neighborhoods and rental properties in New York City based on school quality, demographics, and rental availability.

 ## Directory Structure

 relocation_finder/ (project root)
 ├── README.md
 ├── requirements.txt
 ├── school_filter/        # Filter and prioritize schools by quality and demographics
 ├── neighborhood_mapper/  # Map schools to Neighborhood Tabulation Areas (NTAs)
 ├── rental_scraper/       # Scrape rental listings from StreetEasy
 ├── geocoder/             # Geocode rental addresses using Nominatim
 ├── spatial_join/         # Spatially join rentals to school zones and NTAs
 ├── cli_scripts/          # CLI entrypoints for each pipeline step
 └── utils/                # Helper functions for logging, retries, etc.

 ## Installation

 ```bash
 pip install -r requirements.txt
 ```

 ## Usage

 Filter schools:
 ```bash
 python cli_scripts/run_school_filter.py \
     --data-path PATH_TO_SCHOOL_DATA.csv \
     --min-quality 75.0 \
     --demographics '{"economically_disadvantaged": 0.3}' \
     --output filtered_schools.csv
 ```

 Scrape rentals:
 ```bash
 python cli_scripts/run_rental_scraper.py \
     --output rentals.csv \
     --bedrooms 3 \
     --bathrooms 2 \
     --max-price 5000.0 \
     --laundry
 ```

 Geocode rentals:
 ```bash
 python cli_scripts/run_geocoder.py \
     --input rentals.csv \
     --output rentals_geocoded.csv
 ```

 Spatial join:
 ```bash
 python cli_scripts/run_spatial_join.py \
     --rentals rentals_geocoded.csv \
     --school-zones school_zones.csv \
     --ntas nta_shapefile.shp \
     --output rentals_with_zones.csv
 ```

 ## Next Steps

 - Implement filtering logic in `school_filter` module.
 - Integrate shapefile parsing and spatial joins in `neighborhood_mapper` and `spatial_join`.
 - Flesh out scraping and parsing logic for StreetEasy in `rental_scraper`.
 - Add error handling, logging, and tests.