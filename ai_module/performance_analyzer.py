import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class PerformanceAnalyzer:
    def __init__(self, player_data):
        """Initialize the PerformanceAnalyzer with player data."""
        self.player_data = player_data

    def suggest_improvement_areas(self):
        """Suggest areas of improvement based on player statistics."""
        improvement_areas = {}
        avg_stats = self.player_data.mean()
        for column in self.player_data.columns:
            if avg_stats[column] < self.player_data[column].max() * 0.8:
                improvement_areas[column] = 'Consider focusing more on this area.'
        return improvement_areas

    def predict_performance_trends(self):
        """Predict future performance trends based on historical data."""
        X = self.player_data.drop('performance_metric', axis=1)
        y = self.player_data['performance_metric']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        return predictions.tolist()  

# Example usage:
# player_data = pd.DataFrame(...)  # Load the player data here
# analyzer = PerformanceAnalyzer(player_data)
# improvements = analyzer.suggest_improvement_areas()
# trends = analyzer.predict_performance_trends()