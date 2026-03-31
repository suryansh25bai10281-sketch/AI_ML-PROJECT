import http.client
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# --- 1. AI MODEL (Trained on historical patterns) ---
def train_model():
    # Features: [Current Run Rate, Required Run Rate, Wickets Lost, Overs Remaining]
    data = {
        'crr': [8, 6, 10, 5, 8, 7, 9, 4],
        'rrr': [7, 10, 6, 14, 8, 9, 5, 18],
        'w': [2, 6, 1, 9, 4, 3, 2, 8],
        'o': [10, 4, 15, 2, 8, 12, 18, 1],
        'res': [1, 0, 1, 0, 1, 0, 1, 0] # 1 = Chasing team wins
    }
    model = LogisticRegression().fit(pd.DataFrame(data)[['crr', 'rrr', 'w', 'o']], data['res'])
    return model

# --- 2. FETCH DATA FROM YOUR API ---
def get_live_match(match_id):
    conn = http.client.HTTPSConnection("free-cricbuzz-cricket-api.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "47f4dbd8fcmsh3e4dd8c25dcf435p1c4d26jsnccaf472f54ed",
        'x-rapidapi-host': "free-cricbuzz-cricket-api.p.rapidapi.com"
    }
    try:
        conn.request("GET", f"/cricket-match-info?matchid={match_id}", headers=headers)
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        
        # Extract Team Names
        t1 = data.get('team1', {}).get('name', 'Team 1')
        t2 = data.get('team2', {}).get('name', 'Team 2')
        match_desc = data.get('matchDesc', 'Live Match')
        return t1, t2, match_desc
    except:
        return "Team A", "Team B", "Live Match"

# --- 3. VISUALIZATION ENGINE ---
def plot_analysis(team1, team2, match_desc, current_prob):
    # Setup Figure with 2 Subplots (Top: Gauge, Bottom: Trend)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [1, 3]})
    plt.subplots_adjust(hspace=0.4)

    # --- GRAPH 1: WIN PROBABILITY GAUGE ---
    p2 = current_prob * 100
    p1 = 100 - p2
    
    ax1.barh(['Win %'], [p1], color='#03A9F4', label=team1) # Team 1 (Blue)
    ax1.barh(['Win %'], [p2], left=[p1], color='#FFC107', label=team2) # Team 2 (Gold)
    
    ax1.text(p1/2, 0, f"{team1}\n{p1:.1f}%", ha='center', va='center', color='white', weight='bold')
    ax1.text(p1 + p2/2, 0, f"{team2}\n{p2:.1f}%", ha='center', va='center', color='black', weight='bold')
    ax1.set_title(f"Live AI Prediction: {match_desc}")
    ax1.set_xlim(0, 100)
    ax1.axis('off')

    # --- GRAPH 2: OVER-BY-OVER TREND ---
    # We simulate history for demonstration; in a real app, you'd append 
    # the 'current_prob' to a list at the end of every over.
    current_over = 12 # Assume we are at over 12
    overs = np.arange(1, current_over + 1)
    
    # Generate a dummy trend that ends at our current prediction
    trend = np.linspace(50, p2, len(overs)) + np.random.normal(0, 5, len(overs))
    trend = np.clip(trend, 5, 95) # Keep between 5% and 95%

    ax2.plot(overs, trend, marker='o', color='#FFC107', linewidth=2, label=f"{team2} Win Probability")
    ax2.axhline(y=50, color='gray', linestyle='--', alpha=0.5) # 50% Neutral line
    
    ax2.set_xlabel("Overs", fontsize=12)
    ax2.set_ylabel("Win Probability (%)", fontsize=12)
    ax2.set_title(f"Match Momentum: {team2} Win Probability Over-by-Over")
    ax2.set_ylim(0, 100)
    ax2.set_xlim(1, 20)
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    plt.show()

# --- 4. EXECUTION ---
match_id = "102040"
ai = train_model()
team1, team2, description = get_live_match(match_id)

# Calculate Prediction [CRR, RRR, Wickets, Overs_Rem]
# Example: 8.2 CRR, 9.5 RRR, 4 Wickets down, 8 Overs left
live_input = np.array([[8.2, 9.5, 4, 8]]) 
win_probability = ai.predict_proba(live_input)[0][1]

plot_analysis(team1, team2, description, win_probability)
