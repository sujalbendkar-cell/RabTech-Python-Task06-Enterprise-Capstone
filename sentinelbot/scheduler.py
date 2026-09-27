"""
Automated Scheduler Engine.
Executes periodic automated report generation routines.
"""

import time
import schedule
from sentinelbot.api_client import TelemetryAPIClient
from sentinelbot.analytics import AnalyticsProcessor
from sentinelbot.pdf_generator import PDFReportEngine

class AutomationScheduler:
    def __init__(self, interval_seconds: int = 10, output_pdf: str = "SentinelBot_Executive_Report.pdf"):
        self.interval_seconds = interval_seconds
        self.output_pdf = output_pdf
        self.client = TelemetryAPIClient()

    def job(self):
        print("\n⏰ [SCHEDULER TRIGGERED] Running automated telemetry audit...")
        data = self.client.fetch_market_telemetry()
        summary = AnalyticsProcessor.process_telemetry(data)
        PDFReportEngine.generate_report(data, summary, self.output_pdf)
        print("✅ [SCHEDULER COMPLETED] Automated audit cycle done.")

    def start(self, max_runs: int = 2):
        print(f"🚀 Starting Automated Scheduler (Runs every {self.interval_seconds}s)...")
        schedule.every(self.interval_seconds).seconds.do(self.job)
        
        runs = 0
        while runs < max_runs:
            schedule.run_pending()
            time.sleep(1)
            runs += 1
        print("🛑 Scheduler finished test execution cycle.")
