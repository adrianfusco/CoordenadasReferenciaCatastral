import pyproj
import webbrowser
import argparse


def utm_to_latlon(horizontal, vertical, zone):
    """
    Convert UTM coordinates to latitude and longitude.

    Parameters:
    - horizontal (int): Horizontal UTM coordinate.
    - vertical (int): Vertical UTM coordinate.
    - zone (int): UTM zone.

    Returns:
    - Tuple of float: Latitude and Longitude.
    """
    # Define the UTM projection for the input coordinates (ETRS89)
    utm_input = pyproj.Proj(proj="utm", zone=zone, ellps="GRS80")

    # Convert UTM coordinates to longitude and latitude
    lon, lat = utm_input(horizontal, vertical, inverse=True)

    return lat, lon


def format_coordinates(lat, lon):
    """
    Format latitude and longitude coordinates.

    Parameters:
    - lat (float): Latitude.
    - lon (float): Longitude.

    Returns:
    - str: Formatted coordinates.
    """
    # Format the coordinates as per your requirement
    formatted_coords = "{:.6f}, {:.6f}".format(lat, lon)
    return formatted_coords


def open_in_gmaps(lat, lon):
    """
    Open coordinates in Google Maps.

    Parameters:
    - lat (float): Latitude.
    - lon (float): Longitude.
    """
    # Open the coordinates in Google Maps
    gmaps_url = f"https://www.google.com/maps/place/{lat},{lon}"
    webbrowser.open(gmaps_url)


def main():
    """
    Main function to convert UTM coordinates and optionally open in Google Maps.
    """
    parser = argparse.ArgumentParser(description="Convert UTM coordinates to latitude and longitude.")
    parser.add_argument("horizontal", type=int, help="Horizontal UTM coordinate")
    parser.add_argument("vertical", type=int, help="Vertical UTM coordinate")
    parser.add_argument("zone", type=int, help="UTM zone")
    parser.add_argument("-gmaps", action="store_true", help="Open coordinates in Google Maps")

    args = parser.parse_args()

    # Convert UTM to latitude and longitude
    lat, lon = utm_to_latlon(args.horizontal, args.vertical, args.zone)

    # Format the coordinates
    formatted_coords = format_coordinates(lat, lon)

    print("Input UTM Coordinates:")
    print("Horizontal:", args.horizontal)
    print("Vertical:", args.vertical)
    print("Zone:", args.zone)

    print("\nOutput Latitude and Longitude:")
    print(formatted_coords)

    if args.gmaps:
        print("\nOpening coordinates in Google Maps...")
        open_in_gmaps(lat, lon)


if __name__ == "__main__":
    main()
