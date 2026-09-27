"""
Unit Tests for SentinelBot Capstone Engine.
"""

import unittest
import os
import tempfile
from sentinelbot.api_client import TelemetryAPIClient
from sentinelbot.analytics import AnalyticsProcessor
from sentinelbot.pdf_generator import PDFReportEngine

class TestSentinelBot(unittest.TestCase):
    def setUp(self):
        self.client = TelemetryAPIClient()

    def test_api_fallback(self):
        data = self.client._get_fallback_telemetry()
        self.assertEqual(len(data), 5)
        self.assertIn("BTC", [item["symbol"] for item in data])

    def test_analytics_processing(self):
        data = self.client._get_fallback_telemetry()
        summary = AnalyticsProcessor.process_telemetry(data)
        self.assertEqual(summary["total_assets"], 5)
        self.assertIn("market_sentiment", summary)

    def test_pdf_generation(self):
        data = self.client._get_fallback_telemetry()
        summary = AnalyticsProcessor.process_telemetry(data)
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tf:
            path = tf.name
        try:
            PDFReportEngine.generate_report(data, summary, path)
            self.assertTrue(os.path.exists(path))
            self.assertGreater(os.path.getsize(path), 1000)
        finally:
            if os.path.exists(path):
                os.remove(path)

if __name__ == "__main__":
    unittest.main()
