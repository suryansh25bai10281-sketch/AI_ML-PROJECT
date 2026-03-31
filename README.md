# 🏏 Cricket Win Probability Predictor

An AI-powered live cricket match analyser that fetches real-time match data, predicts win probabilities using a machine learning model, and visualises match momentum through interactive charts.

---

## 📌 Features

- **Live Match Data** — Fetches team names and match details via the CricBuzz Cricket API
- **AI Prediction Engine** — Logistic Regression model trained on key batting performance features
- **Win Probability Gauge** — Horizontal bar chart showing real-time win % for both teams
- **Over-by-Over Trend Graph** — Visualises match momentum across all overs played

---

## 🧠 How the AI Model Works

The model is trained on four in-match features:

| Feature | Description |
|---|---|
| `crr` | Current Run Rate of the chasing team |
| `rrr` | Required Run Rate to win |
| `w` | Wickets lost so far |
| `o` | Overs remaining |

It predicts the probability of the **chasing team winning** (output: `1 = win`, `0 = loss`) using Scikit-learn's `LogisticRegression`.

---

## 📊 Output Visualisation

The script generates a two-panel matplotlib figure:

**Panel 1 — Win Probability Gauge**
A horizontal stacked bar showing the live win percentage split between both teams, with team names and percentages overlaid.

**Panel 2 — Match Momentum Trend**
A line chart plotting the chasing team's win probability over each over, with a 50% neutral reference line and a simulated trajectory ending at the current AI prediction.

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `scikit-learn` | Logistic Regression model |
| `pandas` | Training data structuring |
| `numpy` | Feature array construction |
| `matplotlib` | Visualisation |
| `http.client` | API requests |
| `json` | API response parsing |

---

## 🚀 Setup & Usage

### 1. Install dependencies

```bash
pip install scikit-learn pandas numpy matplotlib
```

### 2. Run the script

```bash
python cricket_predictor.py
```

### 3. Change the match

Update the `match_id` variable at the bottom of the file to any valid CricBuzz match ID:

```python
match_id = "102040"
```

### 4. Update live input features

Modify the `live_input` array with the current match state:

```python
# [Current Run Rate, Required Run Rate, Wickets Lost, Overs Remaining]
live_input = np.array([[8.2, 9.5, 4, 8]])
```

---

## 🔑 API Configuration

This project uses the **Free CricBuzz Cricket API** via [RapidAPI](https://rapidapi.com/). The API key is set inside `get_live_match()`:

```python
headers = {
    'x-rapidapi-key': "YOUR_API_KEY_HERE",
    'x-rapidapi-host': "free-cricbuzz-cricket-api.p.rapidapi.com"
}
```

> ⚠️ **Important:** Do not commit your API key to a public repository. Move it to an environment variable or a `.env` file before sharing:
> ```python
> import os
> 'x-rapidapi-key': os.environ.get("RAPIDAPI_KEY")
> ```

---

## 📁 Project Structure

```
cricket-predictor/
│
├── cricket_predictor.py   ← Main script (model + API + visualisation)
└── README.md              ← This file
```

---

## ⚠️ Limitations

- The training dataset is small (8 samples) — intended as a proof of concept. A production model would require hundreds of historical matches.
- The over-by-over trend graph uses simulated historical data. In a live deployment, you would call the script at the end of each over and append probabilities to a running list.
- API availability depends on your RapidAPI subscription tier and rate limits.

---

## 🔮 Possible Improvements

- Train on a larger historical dataset (e.g., IPL or T20 World Cup ball-by-ball data)
- Replace simulated trend with a real over-by-over data store (SQLite or CSV log)
- Add a second model for the first-innings team using projected total vs par score
- Build a Streamlit dashboard for browser-based live updates
- Add support for multiple simultaneous matches

---

## 📄 License

This project is for educational and personal use. CricBuzz data is subject to [RapidAPI's Terms of Service](https://rapidapi.com/terms/).
