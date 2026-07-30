import time
from aqt import mw
from aqt.gui_hooks import deck_browser_will_render_content

def get_streak_stats():
    """Calcule la streak et vérifie si une révision a été faite aujourd'hui."""
    try:
        # Anki décale les journées selon l'heure de reset
        query = """
            SELECT DISTINCT cast((id/1000 - 14400) / 86400 AS int) AS day
            FROM revlog
            ORDER BY day DESC
        """
        days = [row[0] for row in mw.col.db.all(query)]
        
        if not days:
            return 0, False

        today = int((time.time() - 14400) / 86400)
        reviewed_today = (days[0] == today)

        if days[0] < today - 1:
            return 0, False

        streak = 0
        expected_day = days[0]

        for day in days:
            if day == expected_day:
                streak += 1
                expected_day -= 1
            elif day < expected_day:
                break

        return streak, reviewed_today
    except Exception:
        return 0, False

def add_kawaii_banner(deck_browser, content):
    """Injecte la bannière Kawaii de manière sécurisée via le hook officiel."""
    if not mw.col:
        return

    streak, reviewed_today = get_streak_stats()
    
    status_text = "✨ Mission accomplie !" if reviewed_today else "🌸 N'oublie pas tes révisions !"
    flame_icon = "🔥" if streak > 0 else "💤"
    badge_color = "#ff85a2" if reviewed_today else "#ffb3c6"

    html_card = f"""
    <style>
        @keyframes kawaii-pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.08); }}
            100% {{ transform: scale(1); }}
        }}
        
        .kawaii-streak-card {{
            background: linear-gradient(135deg, #fff0f5 0%, #ffe4e1 100%);
            border: 3px solid #ffb6c1;
            border-radius: 20px;
            padding: 14px 20px;
            margin: 15px auto 20px auto;
            max-width: 500px;
            text-align: center;
            box-shadow: 0 6px 15px rgba(255, 182, 193, 0.4);
            font-family: 'Comic Sans MS', 'Segoe UI', sans-serif;
            color: #4a4a4a;
        }}
        
        .kawaii-header {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }}
        
        .kawaii-flame {{
            font-size: 2.2rem;
            display: inline-block;
            animation: kawaii-pulse 2s infinite ease-in-out;
        }}
        
        .kawaii-count {{
            font-size: 2rem;
            font-weight: 800;
            color: #ff477e;
        }}
        
        .kawaii-subtext {{
            font-size: 0.9rem;
            margin-top: 4px;
            color: #6c757d;
            font-weight: 600;
        }}
    </style>

    <div class="kawaii-streak-card">
        <div class="kawaii-header">
            <span class="kawaii-flame">{flame_icon}</span>
            <span class="kawaii-count">{streak} jour{"s" if streak > 1 else ""} !</span>
            <span class="kawaii-flame">{flame_icon}</span>
        </div>
        <div class="kawaii-subtext">{status_text}</div>
    </div>
    """

    # Ajout du HTML au sommet de la page d'accueil via l'API officielle
    content.tree = html_card + content.tree

# Utilisation du hook moderne Anki
deck_browser_will_render_content.append(add_kawaii_banner)