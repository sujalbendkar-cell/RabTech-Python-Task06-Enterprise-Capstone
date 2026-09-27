"""
Analytics Engine.
Processes raw market data, computes averages, trends, and risk indicators.
"""

from typing import List, Dict, Any

class AnalyticsProcessor:
    @staticmethod
    def process_telemetry(data: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not data:
            return {"total": 0, "avg_price": 0.0, "top_gainer": "None"}

        total_count = len(data)
        avg_price = sum(item["price"] for item in data) / total_count
        top_gainer = max(data, key=lambda x: x["change_24h"])
        top_loser = min(data, key=lambda x: x["change_24h"])
        positive_count = sum(1 for item in data if item["change_24h"] > 0)

        market_sentiment = "BULLISH 🟢" if positive_count >= (total_count / 2) else "BEARISH 🔴"

        return {
            "total_assets": total_count,
            "avg_price": round(avg_price, 2),
            "top_gainer": f"{top_gainer['name']} (+{top_gainer['change_24h']}%)",
            "top_loser": f"{top_loser['name']} ({top_loser['change_24h']}%)",
            "market_sentiment": market_sentiment,
            "positive_count": positive_count,
            "negative_count": total_count - positive_count
        }
