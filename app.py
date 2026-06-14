import streamlit as st

st.set_page_config(
    page_title="Dashboard Options â€” Complete Guide",
    page_icon="??",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #080808; color: #f0f0f0; }
.stApp { background-color: #080808; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #0d0d0d 0%, #111111 100%); border-right: 1px solid #1a1a1a; }
[data-testid="stSidebar"] * { color: #f0f0f0 !important; }
.hero { background: radial-gradient(ellipse at 50% 0%, #003322 0%, #080808 60%); border: 1px solid #1a1a1a; border-radius: 20px; padding: 70px 40px; text-align: center; margin-bottom: 40px; position: relative; overflow: hidden; }
.hero::before { content: ''; position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 300px; height: 2px; background: linear-gradient(90deg, transparent, #00ff88, transparent); }
.hero-title { font-size: 3.5rem; font-weight: 900; letter-spacing: -2px; background: linear-gradient(135deg, #ffffff 0%, #00ff88 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 16px; line-height: 1.1; }
.hero-sub { font-size: 1.2rem; color: #888; max-width: 600px; margin: 0 auto 30px; line-height: 1.7; }
.hero-badge { display: inline-block; background: rgba(0,255,136,0.1); border: 1px solid rgba(0,255,136,0.3); border-radius: 100px; padding: 6px 18px; font-size: 0.8rem; color: #00ff88; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 24px; }
.btn-primary { display: inline-block; background: linear-gradient(135deg, #00ff88, #00cc6a); color: #000 !important; font-weight: 700; font-size: 0.95rem; padding: 14px 32px; border-radius: 10px; text-decoration: none; margin: 6px; box-shadow: 0 0 20px rgba(0,255,136,0.3); }
.btn-outline { display: inline-block; background: transparent; color: #f0f0f0 !important; border: 1px solid #333; font-weight: 600; font-size: 0.95rem; padding: 14px 32px; border-radius: 10px; text-decoration: none; margin: 6px; }
.section-title { font-size: 2rem; font-weight: 800; color: #fff; margin-bottom: 8px; letter-spacing: -1px; }
.section-sub { color: #666; margin-bottom: 32px; font-size: 1rem; }
.neon-line { width: 50px; height: 3px; background: linear-gradient(90deg, #00ff88, transparent); border-radius: 2px; margin-bottom: 24px; }
.feat-card { background: #111; border: 1px solid #1e1e1e; border-radius: 14px; padding: 28px 24px; margin-bottom: 16px; }
.feat-icon { font-size: 2rem; margin-bottom: 14px; }
.feat-title { font-size: 1.05rem; font-weight: 700; color: #fff; margin-bottom: 8px; }
.feat-desc { font-size: 0.88rem; color: #666; line-height: 1.6; }
.greek-card { background: linear-gradient(135deg, #111 0%, #0d1a12 100%); border: 1px solid rgba(0,255,136,0.15); border-radius: 14px; padding: 24px; text-align: center; margin-bottom: 16px; }
.greek-letter { font-size: 2.5rem; font-weight: 900; color: #00ff88; font-family: 'JetBrains Mono', monospace; }
.greek-name { font-size: 1rem; font-weight: 700; color: #fff; margin: 8px 0 4px; }
.greek-desc { font-size: 0.82rem; color: #666; line-height: 1.5; }
.social-link { display: flex; align-items: center; gap: 14px; background: #111; border: 1px solid #1e1e1e; border-radius: 12px; padding: 18px 22px; text-decoration: none; margin-bottom: 12px; }
.social-icon { font-size: 1.5rem; }
.stat-card { background: #111; border: 1px solid #1e1e1e; border-radius: 14px; padding: 24px; text-align: center; }
.stat-number { font-size: 2.5rem; font-weight: 900; color: #00ff88; line-height: 1; }
.stat-label { color: #555; font-size: 0.85rem; margin-top: 6px; }
.step { display: flex; gap: 18px; margin-bottom: 28px; }
.step-num { width: 40px; height: 40px; border-radius: 50%; flex-shrink: 0; background: rgba(0,255,136,0.1); border: 1px solid rgba(0,255,136,0.3); display: flex; align-items: center; justify-content: center; font-weight: 800; color: #00ff88; font-size: 0.9rem; }
.step-title { font-weight: 700; color: #fff; margin-bottom: 4px; }
.step-desc { color: #666; font-size: 0.88rem; line-height: 1.6; }
.code-block { background: #0d0d0d; border: 1px solid #1e1e1e; border-radius: 10px; padding: 16px 20px; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; color: #00ff88; margin: 16px 0; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:20px 0 10px;">
        <div style="font-size:2rem;">??</div>
        <div style="font-weight:800; font-size:1.1rem; color:#fff;">Dashboard Options</div>
        <div style="font-size:0.75rem; color:#00ff88; margin-top:4px;">Complete Guide</div>
    </div>
    <hr style="border-color:#1e1e1e; margin:10px 0 20px;">
    """, unsafe_allow_html=True)

    page = st.radio("Navigate", ["?? Home", "?? Features", "?? Greeks Guide", "?? Get Started", "?? Links"], label_visibility="collapsed")

    st.markdown("""
    <div style="margin-top:30px; padding:16px; background:#0d0d0d; border:1px solid #1e1e1e; border-radius:12px; text-align:center;">
        <div style="font-size:0.75rem; color:#555; margin-bottom:10px;">VISIT THE PLATFORM</div>
        <a href="https://dashboardoptions.com" target="_blank"
           style="display:block; background:linear-gradient(135deg,#00ff88,#00cc6a); color:#000; font-weight:700; padding:10px; border-radius:8px; text-decoration:none; font-size:0.85rem;">
            Open Platform ?
        </a>
    </div>
    """, unsafe_allow_html=True)

# -- HOME --
if "?? Home" in page:
    st.markdown("""
    <div class="hero">
        <div class="hero-badge">? Institutional-Grade Options Analytics</div>
        <div class="hero-title">Dashboard Options</div>
        <p class="hero-sub">Real-time options Greeks, flow analytics, and market intelligence â€” all in one platform. Built for serious traders.</p>
        <a href="https://dashboardoptions.com" target="_blank" class="btn-primary">?? Launch Platform</a>
        <a href="https://github.com/khalid-naami/guide-dashboardoptions" target="_blank" class="btn-outline">? Star on GitHub</a>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, (num, label) in zip([c1,c2,c3,c4], [("30+","Analytics Pages"),("10","Greeks Tracked"),("100%","Free & Open"),("8","Real-Time Data")]):
        with col:
            st.markdown(f'<div class="stat-card"><div class="stat-number">{num}</div><div class="stat-label">{label}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="section-title">What is Dashboard Options?</div>
    <div class="neon-line"></div>
    <p class="section-sub">A professional-grade options analytics platform giving individual traders access to institutional-level data â€” completely free. From Greeks exposure to volatility surfaces, earnings intelligence to macro liquidity.</p>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="feat-card"><div class="feat-icon">??</div><div class="feat-title">For Active Traders</div><div class="feat-desc">Real-time options flow, GEX levels, and intraday exposure data to identify where the big money is positioned.</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="feat-card"><div class="feat-icon">??</div><div class="feat-title">For Researchers</div><div class="feat-desc">Deep volatility analysis, IV surfaces, COT reports, and seasonality data for rigorous market research.</div></div>', unsafe_allow_html=True)

# -- FEATURES --
elif "?? Features" in page:
    st.markdown('<div class="section-title">Platform Features</div><div class="neon-line"></div><p class="section-sub">30+ analytics pages covering every aspect of options trading</p>', unsafe_allow_html=True)
    features = [
        ("??","Options Dashboard","Full options chain with real-time Greeks, volume, OI, and key levels."),
        ("??","Options Flow","Track unusual options activity and large block trades as they happen."),
        ("??","GEX Surface","Gamma Exposure surface showing dealer positioning and key gamma levels."),
        ("??","Exposure Heatmap","Visual heatmap of Greeks exposure across all strikes and expirations."),
        ("?","Delta Exposure","Net delta exposure by strike â€” where are market makers delta-hedged?"),
        ("??","Gamma Exposure","Gamma levels that act as magnets or repellers for price action."),
        ("??","Vanna Exposure","Vanna-driven flows that intensify during volatility expansion/contraction."),
        ("?","Charm Exposure","Time-decay driven delta changes â€” critical near expiration."),
        ("??","Vomma Exposure","Volatility of volatility sensitivity across the options surface."),
        ("??","Speed Exposure","Third-order Greek tracking for advanced positioning analysis."),
        ("??","Color Exposure","Color (Speed of Gamma) exposure visualization across strikes."),
        ("??","IV Surface","3D Implied Volatility surface showing vol smile across strikes and dates."),
        ("??","Volatility Calendar","Historical and implied volatility comparison across time."),
        ("??","Volatility Analysis","In-depth volatility metrics, skew analysis, and term structure."),
        ("??","Implied Probabilities","Market-implied probability of price ranges at expiration."),
        ("??","Expected Move","Calculate expected price move based on options pricing."),
        ("???","Strategy Builder","Build and visualize multi-leg options strategies with P&L diagrams."),
        ("??","OI & Volume","Open Interest and Volume analysis across all strikes."),
        ("??","Multi-Ticker View","Compare multiple tickers side-by-side simultaneously."),
        ("??","Market Sentiment","Aggregated sentiment indicators from options market data."),
        ("??","Earnings Intelligence","Earnings event analysis with historical options behavior."),
        ("??","FOMC Meetings","Fed meeting calendar with market impact analysis."),
        ("???","COT Report","Commitment of Traders report visualization and analysis."),
        ("??","Macro Liquidity","Global liquidity indicators and macro market conditions."),
        ("?","Maritime Intelligence","Shipping and trade data for commodity market correlation."),
        ("???","Seasonality","Historical seasonality patterns for any ticker."),
        ("??","Risk Analysis","Portfolio risk metrics and scenario analysis tools."),
        ("??","Portfolio","Track and analyze your options portfolio exposure."),
        ("??","Breaking News","Real-time financial news feed for market-moving events."),
        ("??","Analysis","Comprehensive technical and fundamental analysis tools."),
    ]
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(features):
        with cols[i % 3]:
            st.markdown(f'<div class="feat-card"><div class="feat-icon">{icon}</div><div class="feat-title">{title}</div><div class="feat-desc">{desc}</div></div>', unsafe_allow_html=True)

# -- GREEKS --
elif "?? Greeks Guide" in page:
    st.markdown('<div class="section-title">Options Greeks â€” Complete Guide</div><div class="neon-line"></div><p class="section-sub">Dashboard Options tracks all Greeks in real-time â€” here is what they mean.</p>', unsafe_allow_html=True)
    greeks = [
        ("?","Delta","Price Sensitivity","Measures how much an option price changes for every $1 move in the underlying. 0 to 1 for calls, -1 to 0 for puts."),
        ("G","Gamma","Delta Acceleration","Rate of change of Delta. High Gamma = Delta changes rapidly. Market makers must hedge Gamma, creating mechanical flows."),
        ("T","Theta","Time Decay","Daily loss in option value due to time passing. Options lose value every day â€” Theta is the cost of holding."),
        ("V","Vega","Vol Sensitivity","How much the option price changes with a 1% change in IV. Long options benefit from rising IV."),
        ("?","Rho","Rate Sensitivity","Sensitivity to interest rate changes. Less critical for short-term options."),
        ("V'","Vanna","Delta-Vega Cross","How Delta changes with IV. Creates powerful flows during volatility expansions and contractions."),
        ("?","Charm","Delta Decay","Rate at which Delta changes over time. Critical near expiration â€” causes mechanical hedging flows."),
        ("?","Vomma","Vega Convexity","Rate of change of Vega with IV. High Vomma benefits long volatility positions."),
        ("?³","Speed","Gamma Momentum","Third-order derivative â€” how Gamma changes with price movement."),
        ("C","Color","Gamma Decay","How Gamma changes over time â€” predicts dealer Gamma shift approaching expiration."),
    ]
    cols = st.columns(2)
    for i, (letter, name, subtitle, desc) in enumerate(greeks):
        with cols[i % 2]:
            st.markdown(f'<div class="greek-card"><div class="greek-letter">{letter}</div><div class="greek-name">{name}</div><div style="font-size:0.75rem;color:#00ff88;margin-bottom:8px;font-weight:600;">{subtitle}</div><div class="greek-desc">{desc}</div></div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#0d1a12; border:1px solid rgba(0,255,136,0.2); border-radius:14px; padding:24px; margin-top:10px;">
        <div style="font-weight:700; color:#00ff88; margin-bottom:12px;">?? Why Greeks Matter</div>
        <p style="color:#888; line-height:1.7; font-size:0.9rem;">Market makers who sell options must continuously delta-hedge. When large options expire or IV spikes, mechanical hedging flows from Gamma, Vanna, and Charm can move markets significantly â€” independent of any news. Dashboard Options lets you track these flows in real-time.</p>
    </div>
    """, unsafe_allow_html=True)

# -- GET STARTED --
elif "?? Get Started" in page:
    st.markdown('<div class="section-title">Get Started in Minutes</div><div class="neon-line"></div><p class="section-sub">Two ways to use Dashboard Options</p>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div style="background:#111; border:1px solid rgba(0,255,136,0.3); border-radius:14px; padding:28px; margin-bottom:20px;">
            <div style="font-size:1.5rem; margin-bottom:12px;">??</div>
            <div style="font-weight:800; font-size:1.1rem; color:#fff; margin-bottom:8px;">Use Online</div>
            <div style="color:#666; font-size:0.88rem; margin-bottom:20px;">No installation needed. Access from any browser.</div>
            <a href="https://dashboardoptions.com" target="_blank" class="btn-primary" style="display:block; text-align:center;">?? Open Now</a>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div style="background:#111; border:1px solid #1e1e1e; border-radius:14px; padding:28px; margin-bottom:20px;">
            <div style="font-size:1.5rem; margin-bottom:12px;">??</div>
            <div style="font-weight:800; font-size:1.1rem; color:#fff; margin-bottom:8px;">Run Locally</div>
            <div style="color:#666; font-size:0.88rem; margin-bottom:20px;">Clone the repo and run on your machine.</div>
            <a href="https://github.com/khalid-naami/guide-dashboardoptions" target="_blank" class="btn-outline" style="display:block; text-align:center;">? Clone on GitHub</a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-title" style="margin-top:10px;">Local Installation Steps</div><div class="neon-line"></div>', unsafe_allow_html=True)

    steps = [
        ("1","Download","Visit GitHub and clone or download the repository."),
        ("2","Navigate","Open terminal and cd into the project directory."),
        ("3","Virtual Environment","Run: python -m venv venv"),
        ("4","Activate","Windows: .\\venv\\Scripts\\activate | Mac/Linux: source venv/bin/activate"),
        ("5","Launch","Run: python main.py â€” installs dependencies and launches automatically."),
    ]
    for num, title, desc in steps:
        st.markdown(f"""
        <div class="step">
            <div class="step-num">{num}</div>
            <div>
                <div class="step-title">{title}</div>
                <div class="step-desc">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="code-block">
git clone https://github.com/khalid-naami/guide-dashboardoptions<br>
cd "Dashboard options"<br>
python -m venv venv<br>
.\\venv\\Scripts\\activate<br>
python main.py
    </div>
    """, unsafe_allow_html=True)

# -- LINKS --
elif "?? Links" in page:
    st.markdown('<div class="section-title">Links & Community</div><div class="neon-line"></div><p class="section-sub">Connect with Dashboard Options across all platforms</p>', unsafe_allow_html=True)

    for icon, name, handle, url in [
        ("🌐", "Website", "dashboardoptions.com", "https://dashboardoptions.com/"),
        ("👤", "Khalid Naami", "khalidnaami.com", "https://khalidnaami.com/"),
        ("💻", "GitHub", "khalid-naami/guide-dashboardoptions", "https://github.com/khalid-naami/guide-dashboardoptions"),
        ("🐦", "Twitter / X", "@DashboardOption", "https://x.com/DashboardOption"),
        ("💼", "LinkedIn", "Dashboard Options", "https://www.linkedin.com/company/dashboard-options/"),
        ("📸", "Instagram", "@dashboardoptions", "https://www.instagram.com/dashboardoptions/"),
        ("🎮", "Discord Server", "Join our trading community", "https://discord.gg/NRSzCYRzpJ"),
        ("✈️", "Telegram", "Daily market updates", "https://t.me/dashboardoptions"),
        ("▶️", "YouTube", "Tutorials & analysis", "https://www.youtube.com/@DashboardOptions"),
    ]:
        st.markdown(f'<a href="{url}" target="_blank" class="social-link"><div class="social-icon">{icon}</div><div><div style="font-weight:700;color:#fff;font-size:0.95rem;">{name}</div><div style="color:#888;font-size:0.82rem;">{handle}</div></div><div style="margin-left:auto;color:#00ff88;">→</div></a>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background:linear-gradient(135deg,#0d1a12 0%,#111 100%); border:1px solid rgba(0,255,136,0.2); border-radius:16px; padding:40px; text-align:center; margin-top:30px;">
        <div style="font-size:2rem; margin-bottom:12px;">??</div>
        <div style="font-size:1.5rem; font-weight:800; color:#fff; margin-bottom:8px;">Ready to Trade Smarter?</div>
        <div style="color:#666; margin-bottom:24px;">Join traders using institutional-level data â€” for free.</div>
        <a href="https://dashboardoptions.com" target="_blank" class="btn-primary">Open Dashboard Options Now ?</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; padding:40px 0 20px; color:#555; font-size:0.8rem; margin-top:60px; border-top:1px solid #1a1a1a;">
    Built with ❤️ by <a href="https://khalidnaami.com/" style="color:#00ff88;text-decoration:none;">Khalid Naami</a>
    &nbsp;·&nbsp;
    <a href="https://dashboardoptions.com/" style="color:#00ff88;text-decoration:none;">dashboardoptions.com</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/khalid-naami/guide-dashboardoptions" style="color:#00ff88;text-decoration:none;">GitHub</a>
    &nbsp;·&nbsp;
    <a href="https://x.com/DashboardOption" style="color:#00ff88;text-decoration:none;">𝕏</a>
    &nbsp;·&nbsp;
    <a href="https://www.instagram.com/dashboardoptions/" style="color:#00ff88;text-decoration:none;">Instagram</a>
    &nbsp;·&nbsp;
    <a href="https://www.linkedin.com/company/dashboard-options/" style="color:#00ff88;text-decoration:none;">LinkedIn</a>
    &nbsp;·&nbsp;
    <a href="https://t.me/dashboardoptions" style="color:#00ff88;text-decoration:none;">Telegram</a>
    &nbsp;·&nbsp;
    <a href="https://discord.gg/NRSzCYRzpJ" style="color:#00ff88;text-decoration:none;">Discord</a>
    &nbsp;·&nbsp;
    <a href="https://www.youtube.com/@DashboardOptions" style="color:#00ff88;text-decoration:none;">YouTube</a>
</div>
""", unsafe_allow_html=True)

