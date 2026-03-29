#!/usr/bin/env python3
"""
Daily Motivation Script - Final Version
Adds a random motivational quote to README.md
"""

import random
from datetime import datetime

QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future depends on what you do today. - Mahatma Gandhi",
    "Success is not final, failure is not fatal. - Winston Churchill",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "It is during our darkest moments that we must focus to see the light. - Aristotle",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "Life is 10% what happens to you and 90% how you react to it. - Charles R. Swindoll",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "Do something today that your future self will thank you for. - Sean Patrick Flanery",
    "Great things never come from comfort zones. - Unknown",
    "Dream it. Believe it. Build it. - Unknown",
    "Success doesn't just find you. You have to go out and get it. - Unknown",
    "The harder you work for something, the greater you'll feel when you achieve it. - Unknown",
    "Dream bigger. Do bigger. - Unknown",
    "Don't stop when you're tired. Stop when you're done. - Unknown",
    "Wake up with determination. Go to bed with satisfaction. - Unknown",
    "Do what you have to do, to do what you want to do. - Unknown",
    "Success is the sum of small efforts repeated day in and day out. - Robert Collier",
    "Your limitation—it's only your imagination. - Unknown",
    "Push yourself, because no one else is going to do it for you. - Unknown",
    "Sometimes we're tested not to show our weaknesses, but to discover our strengths. - Unknown",
    "The key to success is to focus on goals, not obstacles. - Unknown",
    "Dream as if you'll live forever. Live as if you'll die today. - James Dean",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "If you are working on something that you really care about, you don't have to be pushed. The vision pulls you. - Steve Jobs",
    "You don't need to see the whole staircase, just take the first step. - Martin Luther King Jr.",
    "Everything you want is on the other side of fear. - Unknown",
    "Believe in yourself. You are braver than you believe, stronger than you seem, and smarter than you think. - A.A. Milne",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Unknown",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Don't let yesterday take up too much of today. - Will Rogers",
    "You learn more from failure than from success. - Unknown",
    "It's not about how good you are, it's about how good you want to be. - Unknown",
    "Failure is the condiment that gives success its flavor. - Truman Capote",
    "No one can make you feel inferior without your consent. - Eleanor Roosevelt",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "What we achieve inwardly will change outer reality. - Plutarch",
    "The mind is everything. What you think, you become. - Buddha",
    "Stop being afraid of what could go wrong and focus on what could go right. - Unknown",
]

def main():
    # Get date and quote
    today = datetime.now().strftime("%Y-%m-%d")
    quote = random.choice(QUOTES)
    
    # Read README
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""
    
    # Format entry
    entry = f"### 💪 Daily Motivation ({today})\n> {quote}\n"
    
    # Update README
    if "## Daily Motivation" not in content:
        new_content = f"## Daily Motivation\n\n{entry}\n---\n\n{content}"
    else:
        lines = content.split("\n")
        idx = None
        for i, line in enumerate(lines):
            if line.strip() == "## Daily Motivation":
                idx = i + 1
                break
        
        if idx is not None:
            lines.insert(idx, entry)
            new_content = "\n".join(lines)
        else:
            new_content = f"## Daily Motivation\n\n{entry}\n---\n\n{content}"
    
    # Write README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"✅ Added motivation for {today}")
    print(f"📝 Quote: {quote}")

if __name__ == "__main__":
    main()