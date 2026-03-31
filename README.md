#🏏 Cricket Match Win Probability Predictor (AI-Based)

#📌 Overview

This project uses a simple Machine Learning model (Logistic Regression) to predict the win probability of a chasing team in a live cricket match.

It combines:

AI-based prediction
Live match data fetching via API
Data visualization using Matplotlib

The output includes:

A win probability gauge
An over-by-over momentum graph
#⚙️ Features
#📊 Predicts win probability using match conditions:
Current Run Rate (CRR)
Required Run Rate (RRR)
Wickets Lost
Overs Remaining
🌐 Fetches live match details from Cricbuzz API
📈 Visualizes:
Win probability comparison
Match momentum trend
🤖 Lightweight ML model (Logistic Regression)
🧠 Machine Learning Model

The model is trained on a small synthetic dataset with features:

Feature	Description
CRR	Current Run Rate
RRR	Required Run Rate
Wickets	Wickets lost
Overs	Overs remaining

Target:

1 → Chasing team wins
0 → Chasing team loses
📦 Requirements

Install dependencies before running:

pip install pandas numpy matplotlib scikit-learn
🔑 API Setup

This project uses the Cricbuzz API from RapidAPI.

#Steps:
Go to RapidAPI
Subscribe to Cricbuzz API
Replace this line in the code:
'x-rapidapi-key': "YOUR_API_KEY"

⚠️ Important: Never expose your API key publicly.

▶️ How to Run
Clone the repository or copy the code
Install dependencies
Set your API key
Run:
python main.py
📊 Example Input
live_input = np.array([[8.2, 9.5, 4, 8]])

This represents:

CRR = 8.2
RRR = 9.5
Wickets lost = 4
Overs remaining = 8
📈 Output
1. Win Probability Gauge
Shows percentage chance of both teams winning
2. Match Momentum Graph
Displays win probability trend across overs
⚠️ Limitations
Uses dummy training data (not real historical matches)
Trend graph is simulated
Accuracy is not production-level
Depends on API availability
🚀 Future Improvements
Use real historical match datasets
Real-time ball-by-ball updates
Deploy as a web app (Flask/Streamlit)
Improve model with advanced algorithms (XGBoost, Neural Networks)
📁 Project Structure
├── cricket_prediction.py          # Main script
├── README.md        # Documentation
👨‍💻 Author


Machine Learning
APIs
Data Visualization
📜 License

This project is open-source and free to use for learning purposes.
