"""
Automated PDF Report Generator Engine.
Generates enterprise-grade executive PDF reports using ReportLab.
"""

import os
from datetime import datetime
from typing import List, Dict, Any

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

class PDFReportEngine:
    @staticmethod
    def generate_report(data: List[Dict[str, Any]], summary: Dict[str, Any], output_pdf: str):
        doc = SimpleDocTemplate(
            output_pdf,
            pagesize=letter,
            rightMargin=36,
            leftMargin=36,
            topMargin=36,
            bottomMargin=36
        )

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "TitleStyle",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=22,
            textColor=colors.HexColor("#1E293B"),
            spaceAfter=6
        )

        subtitle_style = ParagraphStyle(
            "SubTitleStyle",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10,
            textColor=colors.HexColor("#64748B"),
            spaceAfter=15
        )

        heading_style = ParagraphStyle(
            "SectionHeading",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            textColor=colors.HexColor("#0F172A"),
            spaceBefore=12,
            spaceAfter=8
        )

        body_style = ParagraphStyle(
            "BodyTextCustom",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10,
            textColor=colors.HexColor("#334155"),
            leading=14
        )

        story = []

        # 1. Header & Title
        story.append(Paragraph("🤖 SENTINELBOT ENTERPRISE ANALYTICS REPORT", title_style))
        story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Author: Sujal Bendkar (Intern ID: RAB-2026-9471669A59)", subtitle_style))
        story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#2563EB"), spaceAfter=15))

        # 2. Executive Summary
        story.append(Paragraph("📊 Executive Summary", heading_style))
        summary_text = (
            f"Analyzed <b>{summary['total_assets']}</b> market assets. "
            f"Overall Sentiment: <b>{summary['market_sentiment']}</b>. "
            f"Average Price: <b>${summary['avg_price']:.2f}</b>. "
            f"Top Gainer: <b>{summary['top_gainer']}</b> | Top Loser: <b>{summary['top_loser']}</b>."
        )
        story.append(Paragraph(summary_text, body_style))
        story.append(Spacer(1, 15))

        # 3. Telemetry Data Table
        story.append(Paragraph("📈 Market Telemetry Details", heading_style))

        table_data = [["Asset Name", "Symbol", "Current Price ($)", "24h Change (%)", "Market Cap ($)"]]
        for item in data:
            table_data.append([
                item["name"],
                item["symbol"],
                f"${item['price']:,.2f}",
                f"{item['change_24h']:+.2f}%",
                f"${item['market_cap']:,.0f}"
            ])

        t = Table(table_data, colWidths=[120, 70, 110, 110, 130])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1E293B")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")])
        ]))

        story.append(t)
        story.append(Spacer(1, 20))

        # 4. Footer Metadata
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E2E8F0"), spaceAfter=10))
        story.append(Paragraph("Confidential Report | Generated automatically by SentinelBot Capstone Engine | RabTech Academy Python Track", subtitle_style))

        doc.build(story)
        print(f"✅ Generated PDF Report: {os.path.abspath(output_pdf)}")
