import os
import requests

def get_food_data(query):
    """
    Fetches nutritional information for a given food item from the USDA FoodData Central API.

    Args:
        query (str): The search query for the food item.

    Returns:
        dict: A dictionary containing the API response, or None if an error occurred.
    """

    api_key = os.environ.get("USDA_FDC_API_KEY")
    if not api_key:
        raise ValueError("USDA_FDC_API_KEY environment variable is not set.")

    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={query}&api_key={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

if __name__ == "__main__":
    search_query = "Doritos 3D Crunch Chili Cheese Nacho"
    food_data = get_food_data(search_query)

    if food_data:
        # Process the food data (e.g., print nutritional information)
        print(food_data['foods'][0].keys())
    else:
        print("Failed to retrieve food data.")