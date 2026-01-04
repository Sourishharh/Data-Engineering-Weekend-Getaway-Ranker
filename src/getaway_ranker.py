import pandas as pd

def get_weekend_recommendations(city_name, limit=5):
    # Load dataset
    travel_data = pd.read_csv("data/travel_places_india.csv")

    # Normalize column headers
    travel_data.columns = travel_data.columns.str.strip()

    # Select records for given city
    city_places = travel_data[
        travel_data["City"].str.lower() == city_name.lower()
    ].copy()

    if len(city_places) == 0:
        print("Sorry, no tourist places found for this city.")
        return

    # Scale rating values
    max_rating = city_places["Google review rating"].max()
    city_places["rating_score"] = city_places["Google review rating"] / max_rating

    # Scale popularity values
    max_reviews = city_places["Number of google review in lakhs"].max()
    city_places["popularity_score"] = (
        city_places["Number of google review in lakhs"] / max_reviews
    )

    # Combined ranking score
    city_places["final_rank_score"] = (
        0.6 * city_places["rating_score"] +
        0.4 * city_places["popularity_score"]
    )

    # Sort destinations
    ranked_places = city_places.sort_values(
        by="final_rank_score",
        ascending=False
    )

    print(f"\nBest Weekend Getaways from {city_name}:\n")

    for index, place in ranked_places.head(limit).iterrows():
        print(
            f"{place['Name']} | "
            f"Rating: {place['Google review rating']} | "
            f"Reviews: {place['Number of google review in lakhs']} lakh"
        )


if __name__ == "__main__":
    user_city = input("Enter source city: ")
    get_weekend_recommendations(user_city)