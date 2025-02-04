import smtplib
import feedparser
from email.mime.text import MIMEText

# News Sources (Replace with your chosen RSS feeds)
news_feeds = {
    "BBC": "http://feeds.bbci.co.uk/news/rss.xml",
    "CNN": "http://rss.cnn.com/rss/edition.rss",
}

# Fetch headlines
def fetch_news():
    summaries = []
    for source, url in news_feeds.items():
        feed = feedparser.parse(url)
        if feed.entries:
            summaries.append(f"📰 {source} Headlines:")
            for entry in feed.entries[:5]:  # Get top 5 headlines
                summaries.append(f"- {entry.title}")
            summaries.append("")  # Line break
    return "\n".join(summaries)

# Send Email
def send_email(news_summary):
    sender_email = "your-email@gmail.com"  # Replace with your email
    receiver_email = "your-email@gmail.com"  # Replace with your email
    password = "your-app-password"  # Use an App Password (see below)

    msg = MIMEText(news_summary)
    msg["Subject"] = "Daily News Summary"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Run the script
news_summary = fetch_news()
send_email(news_summary)
