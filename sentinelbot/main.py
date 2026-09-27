"""
CLI Entry Point for SentinelBot Capstone Automation Engine.
"""

import sys
import argparse
import os
from sentinelbot.api_client import TelemetryAPIClient
from sentinelbot.analytics import AnalyticsProcessor
from sentinelbot.pdf_generator import PDFReportEngine
from sentinelbot.scheduler import AutomationScheduler

def main():
    parser = argparse.ArgumentParser(
        prog="sentinelbot",
        description="Enterprise Python Automation Capstone Project - PDF Report & Telemetry Engine"
    )
    parser.add_argument("--pdf", type=str, default="SentinelBot_Executive_Report.pdf", help="Output PDF file path")
    parser.add_argument("--schedule", type=int, help="Run background scheduler with interval in seconds")
    parser.add_argument("--version", "-v", action="version", version="SentinelBot v1.0.0 (RabTech Task 06 Capstone)")

    args = parser.parse_args()

    print("==================================================")
    print("  🤖 SENTINELBOT ENTERPRISE CAPSTONE ENGINE")
    print("==================================================")

    if args.schedule:
        scheduler = AutomationScheduler(interval_seconds=args.schedule, output_pdf=args.pdf)
        scheduler.start(max_runs=2)
    else:
        print("\n🌐 Fetching live market & telemetry APIs...")
        client = TelemetryAPIClient()
        raw_data = client.fetch_market_telemetry()

        print("⚙️ Processing statistical analytics...")
        summary = AnalyticsProcessor.process_telemetry(raw_data)

        print(f"📄 Generating PDF Report: {args.pdf}...")
        PDFReportEngine.generate_report(raw_data, summary, args.pdf)

        print("\n==================================================")
        print("  🎉 Capstone Execution Completed Successfully!")
        print("==================================================")

if __name__ == "__main__":
    main()
