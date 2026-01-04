<<<<<<< HEAD
# Data-Engineering-Weekend-Getaway-Ranker
=======
## Weekend Getaway Ranker

**A Data Engineering Recommendation System (Python Project)** 

Weekend Getaway Ranker is a Python-based data engineering application that recommends and ranks popular weekend travel destinations in India based on user ratings and popularity metrics.
This project was developed as part of the Aeka Advisor Assignment using Python and Pandas.

## Project Objective

To build a lightweight recommendation engine that helps users identify the best weekend travel destinations by analyzing real-world tourism data and ranking locations using transparent, rule-based logic.

## Technologies Used

Python 3 – Core programming language

Pandas – Data processing and analysis

CSV Dataset – India’s Must-See Places dataset

Git & GitHub – Version control and submission

## Key Features

🏙️ City-based destination filtering

⭐ Ranking based on Google review ratings

🔥 Popularity-based scoring using review counts

⚖️ Normalized scoring for fair comparison

🧹 Data cleaning and preprocessing

📄 Command-line based interaction

📦 Lightweight and dependency-minimal

##  How It Works

The user provides a source city as input.

Tourist destinations belonging to that city are filtered from the dataset.

Ratings and popularity values are normalized to a common scale.

A weighted ranking score is calculated for each destination.

Destinations are sorted and displayed in ranked order.

This approach ensures transparency and avoids black-box recommendations.

## 📂 Project Structure
```text
weekend-getaway-ranker/
│
├── data/
│   └── travel_places_india.csv   # Travel dataset
│
├── src/
│   └── getaway_ranker.py         # Ranking logic script
│
├── output/
│   └── sample_output.txt         # Sample outputs for cities
│
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

## Installation

Install the required dependency using:
```text
pip install -r requirements.txt
```

## Execution

Run the script from the project root directory:
```text
python src/getaway_ranker.py
```

## Enter a source city when prompted, for example:
```text

📌 Sample Output
 Source City: Kolkata
Howrah Bridge | Rating: 4.6 | Reviews: 1.2 lakh
Dakshineswar Kali Temple | Rating: 4.7 | Reviews: 0.82 lakh
Science City Kolkata | Rating: 4.4 | Reviews: 0.88 lakh
Victoria Memorial | Rating: 4.6 | Reviews: 0.73 lakh
Alipore Zoological Gardens | Rating: 4.3 | Reviews: 0.66 lakh
```

```text
Source City: Delhi
Gurudwara Bangla Sahib | Rating: 4.8 | Reviews: 1.05 lakh
India Gate | Rating: 4.6 | Reviews: 2.6 lakh
Akshardham Temple | Rating: 4.6 | Reviews: 0.4 lakh
Red Fort | Rating: 4.5 | Reviews: 1.5 lakh
Humayun's Tomb | Rating: 4.5 | Reviews: 0.4 lakh
```
```text
Source City: Mumbai
Gateway of India | Rating: 4.6 | Reviews: 3.6 lakh
Marine Drive | Rating: 4.5 | Reviews: 1.5 lakh
Siddhivinayak Temple | Rating: 4.8 | Reviews: 1.05 lakh
Haji Ali Dargah | Rating: 4.4 | Reviews: 0.16 lakh
Chowpatty Beach | Rating: 4.3 | Reviews: 0.05 lakh
```

## Key Learnings

Working with large, real-world datasets

Cleaning and standardizing data for analysis

Feature normalization for fair ranking

Designing recommendation logic without machine learning

Handling Pandas warnings and best practices


## Conclusion

Weekend Getaway Ranker demonstrates how structured tourism data can be transformed into meaningful travel recommendations using simple yet effective data engineering techniques. The project emphasizes clarity, transparency, and real-world applicability, making it suitable for academic submission, GitHub review, and interview discussions.
>>>>>>> 5571c3c (project done)
