from flask import Flask, request, redirect, render_template_string, session, flash
import json, random, string
from pathlib import Path
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret123"
DB_PATH = Path(__file__).parent / "data.json"


# ─────────────── DB ───────────────
def load_data():
    if DB_PATH.exists():
        with open(DB_PATH) as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)

def generate_account():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def get_user(account, pin):
    for u in load_data():
        if u["accountNo"] == account and u["pin"] == pin:
            return u
    return None

def now():
    return datetime.now().strftime("%b %d, %Y · %I:%M %p")


# ─────────────── BASE TEMPLATE ───────────────
BASE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SmartBank</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0;}
:root{
  --bg:#08091a;--surface:#111827;--surface2:#1a2236;--surface3:#1f2d45;
  --border:rgba(255,255,255,0.07);--border2:rgba(255,255,255,0.12);
  --accent:#6366f1;--accent-hover:#4f52d6;--accent2:#22d3ee;
  --green:#10b981;--red:#f43f5e;--amber:#f59e0b;
  --text:#f1f5f9;--muted:#64748b;--muted2:#94a3b8;
  --radius:14px;--radius-lg:20px;
}
body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text);min-height:100vh;}

/* ── Layout ── */
.page{max-width:440px;margin:0 auto;padding:20px 16px 40px;}
.center{display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;padding:20px;}

/* ── Topbar ── */
.topbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:28px;}
.logo{font-size:20px;font-weight:700;letter-spacing:-0.5px;}
.logo span{color:var(--accent);}
.avatar{width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:600;cursor:pointer;}
.greeting{font-size:12px;color:var(--muted);text-align:right;margin-bottom:2px;}

/* ── Flash messages ── */
.flashes{margin-bottom:16px;}
.flash{padding:12px 16px;border-radius:var(--radius);font-size:13px;margin-bottom:8px;display:flex;align-items:center;gap:8px;animation:slideIn 0.3s ease;}
.flash.success{background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.3);color:#6ee7b7;}
.flash.error{background:rgba(244,63,94,0.12);border:1px solid rgba(244,63,94,0.3);color:#fca5a5;}
.flash.info{background:rgba(99,102,241,0.12);border:1px solid rgba(99,102,241,0.3);color:#a5b4fc;}
@keyframes slideIn{from{opacity:0;transform:translateY(-8px);}to{opacity:1;transform:translateY(0);}}

/* ── Balance card ── */
.balance-card{
  background:linear-gradient(135deg,#1e1b4b 0%,#312e81 45%,#1e3a5f 100%);
  border-radius:22px;padding:28px 24px;margin-bottom:20px;position:relative;
  overflow:hidden;border:1px solid rgba(99,102,241,0.25);
}
.balance-card::before{content:'';position:absolute;top:-50px;right:-50px;width:180px;height:180px;border-radius:50%;background:rgba(99,102,241,0.12);}
.balance-card::after{content:'';position:absolute;bottom:-30px;left:-20px;width:120px;height:120px;border-radius:50%;background:rgba(34,211,238,0.07);}
.bal-label{font-size:11px;color:rgba(255,255,255,0.45);text-transform:uppercase;letter-spacing:2px;margin-bottom:8px;}
.bal-amount{font-size:38px;font-weight:700;letter-spacing:-1.5px;position:relative;z-index:1;}
.bal-amount sup{font-size:18px;font-weight:500;vertical-align:super;opacity:0.7;}
.bal-change{font-size:12px;color:rgba(255,255,255,0.4);margin-top:4px;}
.bal-acct{font-size:11px;color:rgba(255,255,255,0.3);margin-top:18px;letter-spacing:3px;position:relative;z-index:1;}

/* ── Action buttons ── */
.action-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:24px;}
.action-btn{
  background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:16px 8px 12px;display:flex;flex-direction:column;align-items:center;gap:7px;
  text-decoration:none;color:var(--text);cursor:pointer;
  transition:background 0.2s,border-color 0.2s,transform 0.15s;
}
.action-btn:hover{background:var(--surface2);border-color:rgba(99,102,241,0.4);transform:translateY(-2px);}
.action-icon{width:40px;height:40px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:17px;}
.action-label{font-size:11px;color:var(--muted2);font-weight:500;}

/* ── Stats row ── */
.stats-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:24px;}
.stat-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:16px;}
.stat-label{font-size:10px;color:var(--muted);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:6px;}
.stat-value{font-size:22px;font-weight:700;}
.mini-bars{display:flex;gap:3px;margin-top:10px;}
.mbar{flex:1;height:3px;border-radius:3px;background:var(--border);}

/* ── Section header ── */
.section-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;}
.section-title{font-size:12px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:1.5px;}
.section-link{font-size:12px;color:var(--accent);text-decoration:none;}

/* ── Transaction list ── */
.txn-list{display:flex;flex-direction:column;gap:8px;margin-bottom:24px;}
.txn{display:flex;align-items:center;gap:12px;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:14px 16px;transition:background 0.15s;}
.txn:hover{background:var(--surface2);}
.txn-icon{width:42px;height:42px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0;}
.txn-info{flex:1;min-width:0;}
.txn-name{font-size:14px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.txn-meta{font-size:11px;color:var(--muted);margin-top:2px;}
.txn-amt{font-size:15px;font-weight:600;white-space:nowrap;}
.txn-tag{display:inline-block;font-size:10px;padding:2px 7px;border-radius:20px;margin-left:4px;vertical-align:middle;}
.tag-green{background:rgba(16,185,129,0.1);color:#6ee7b7;}
.tag-red{background:rgba(244,63,94,0.1);color:#fca5a5;}
.tag-blue{background:rgba(99,102,241,0.1);color:#a5b4fc;}
.tag-amber{background:rgba(245,158,11,0.1);color:#fcd34d;}
.credit{color:var(--green);}
.debit{color:var(--red);}

/* ── Forms ── */
.auth-card{background:var(--surface);border:1px solid var(--border);border-radius:22px;padding:36px 32px;width:100%;max-width:380px;}
.auth-logo{text-align:center;font-size:24px;font-weight:700;margin-bottom:6px;}
.auth-logo span{color:var(--accent);}
.auth-sub{text-align:center;font-size:13px;color:var(--muted);margin-bottom:28px;}
.form-group{margin-bottom:16px;}
.form-label{display:block;font-size:12px;color:var(--muted2);font-weight:500;margin-bottom:6px;letter-spacing:0.3px;}
.form-input{
  width:100%;padding:12px 14px;background:var(--surface2);border:1px solid var(--border2);
  border-radius:var(--radius);color:var(--text);font-size:14px;font-family:inherit;
  transition:border-color 0.2s,box-shadow 0.2s;outline:none;
}
.form-input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(99,102,241,0.15);}
.form-input::placeholder{color:var(--muted);}
.btn{
  width:100%;padding:13px;background:var(--accent);color:#fff;border:none;
  border-radius:var(--radius);font-size:14px;font-weight:600;cursor:pointer;
  font-family:inherit;transition:background 0.2s,transform 0.15s;letter-spacing:0.2px;
}
.btn:hover{background:var(--accent-hover);transform:translateY(-1px);}
.btn:active{transform:translateY(0);}
.btn-ghost{background:transparent;border:1px solid var(--border2);color:var(--muted2);}
.btn-ghost:hover{background:var(--surface2);border-color:var(--border2);}
.btn-danger{background:#be123c;}
.btn-danger:hover{background:#9f1239;}
.auth-footer{text-align:center;margin-top:20px;font-size:13px;color:var(--muted);}
.auth-footer a{color:var(--accent);text-decoration:none;font-weight:500;}
.divider{display:flex;align-items:center;gap:12px;margin:18px 0;color:var(--muted);font-size:12px;}
.divider::before,.divider::after{content:'';flex:1;height:1px;background:var(--border);}

/* ── Page header ── */
.page-header{display:flex;align-items:center;gap:12px;margin-bottom:24px;}
.back-btn{width:38px;height:38px;border-radius:12px;background:var(--surface);border:1px solid var(--border);display:flex;align-items:center;justify-content:center;text-decoration:none;color:var(--muted2);font-size:18px;transition:background 0.2s;}
.back-btn:hover{background:var(--surface2);}
.page-title{font-size:18px;font-weight:600;}

/* ── Amount input special ── */
.amount-wrapper{position:relative;}
.amount-prefix{position:absolute;left:14px;top:50%;transform:translateY(-50%);font-size:20px;font-weight:600;color:var(--muted2);}
.amount-input{padding-left:36px !important;font-size:24px !important;font-weight:700 !important;}

/* ── Empty state ── */
.empty-state{text-align:center;padding:40px 20px;color:var(--muted);}
.empty-icon{font-size:40px;margin-bottom:12px;opacity:0.4;}

/* ── Account info strip ── */
.acct-strip{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:14px 16px;margin-bottom:20px;display:flex;justify-content:space-between;align-items:center;}
.acct-strip-label{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:1px;}
.acct-strip-val{font-size:13px;font-weight:600;letter-spacing:1px;}

/* ── Logout row ── */
.bottom-row{margin-top:16px;}

</style>
</head>
<body>
{% with messages = get_flashed_messages(with_categories=True) %}
{% if messages %}
<div style="max-width:440px;margin:16px auto 0;padding:0 16px;">
  <div class="flashes">
    {% for cat, msg in messages %}
    <div class="flash {{ cat }}">
      {% if cat == 'success' %}✓{% elif cat == 'error' %}✕{% else %}ℹ{% endif %}
      {{ msg }}
    </div>
    {% endfor %}
  </div>
</div>
{% endif %}
{% endwith %}
{{ content | safe }}
</body>
</html>
"""


# ─────────────── HOME ───────────────
@app.route("/")
def home():
    content = """
    <div class="center">
      <div style="text-align:center;max-width:340px;">
        <div style="font-size:52px;margin-bottom:16px;">🏦</div>
        <h1 style="font-size:32px;font-weight:700;letter-spacing:-1px;margin-bottom:8px;">Smart<span style="color:var(--accent)">Bank</span></h1>
        <p style="color:var(--muted);font-size:15px;line-height:1.6;margin-bottom:36px;">Your secure & modern financial partner. Banking made beautiful.</p>
        <div style="display:flex;flex-direction:column;gap:12px;">
          <a href="/login" class="btn" style="display:block;text-decoration:none;text-align:center;">Login to Account</a>
          <a href="/register" class="btn btn-ghost" style="display:block;text-decoration:none;text-align:center;">Create New Account</a>
        </div>
      </div>
    </div>
    """
    return render_template_string(BASE, content=content)


# ─────────────── REGISTER ───────────────
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = load_data()
        age = int(request.form["age"])
        if age < 18:
            flash("You must be 18 or older to register.", "error")
            return redirect("/register")

        user = {
            "name": request.form["name"],
            "age": age,
            "email": request.form["email"],
            "pin": int(request.form["pin"]),
            "accountNo": generate_account(),
            "balance": 0,
            "transactions": []
        }
        data.append(user)
        save_data(data)

        content = f"""
        <div class="center">
          <div class="auth-card" style="text-align:center;">
            <div style="font-size:44px;margin-bottom:16px;">🎉</div>
            <h2 style="font-size:22px;font-weight:700;margin-bottom:8px;">Account Created!</h2>
            <p style="color:var(--muted);font-size:13px;margin-bottom:24px;">Save your account number securely.</p>
            <div style="background:var(--surface2);border:1px solid var(--border2);border-radius:var(--radius);padding:20px;margin-bottom:24px;">
              <div style="font-size:11px;color:var(--muted);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:6px;">Account Number</div>
              <div style="font-size:26px;font-weight:700;letter-spacing:4px;color:var(--accent);">{user['accountNo']}</div>
            </div>
            <a href="/login" class="btn" style="display:block;text-decoration:none;text-align:center;">Proceed to Login</a>
          </div>
        </div>
        """
        return render_template_string(BASE, content=content)

    content = """
    <div class="center">
      <div class="auth-card">
        <div class="auth-logo">Smart<span>Bank</span></div>
        <div class="auth-sub">Open your account in seconds</div>
        <div class="form-group">
          <label class="form-label">Full Name</label>
          <form method="POST">
          <input class="form-input" name="name" placeholder="Rahul Mehta" required>
        </div>
        <div class="form-group">
          <label class="form-label">Age</label>
          <input class="form-input" name="age" type="number" placeholder="25" required min="18">
        </div>
        <div class="form-group">
          <label class="form-label">Email Address</label>
          <input class="form-input" name="email" type="email" placeholder="you@email.com" required>
        </div>
        <div class="form-group">
          <label class="form-label">4-Digit PIN</label>
          <input class="form-input" name="pin" type="password" placeholder="••••" maxlength="4" required>
        </div>
        <button type="submit" class="btn">Create Account</button>
        </form>
        <div class="auth-footer">Already have an account? <a href="/login">Login</a></div>
      </div>
    </div>
    """
    return render_template_string(BASE, content=content)


# ─────────────── LOGIN ───────────────
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        account = request.form["account"].strip()
        try:
            pin = int(request.form["pin"])
        except ValueError:
            flash("Invalid PIN.", "error")
            return redirect("/login")

        user = get_user(account, pin)
        if user:
            session["account"] = account
            session["pin"] = pin
            flash(f"Welcome back, {user['name'].split()[0]}! 👋", "success")
            return redirect("/dashboard")
        else:
            flash("Invalid account number or PIN.", "error")
            return redirect("/login")

    content = """
    <div class="center">
      <div class="auth-card">
        <div class="auth-logo">Smart<span>Bank</span></div>
        <div class="auth-sub">Secure login to your account</div>
        <form method="POST">
          <div class="form-group">
            <label class="form-label">Account Number</label>
            <input class="form-input" name="account" placeholder="e.g. $I3M1Z3" required style="letter-spacing:2px;">
          </div>
          <div class="form-group">
            <label class="form-label">4-Digit PIN</label>
            <input class="form-input" name="pin" type="password" placeholder="••••" maxlength="4" required>
          </div>
          <button type="submit" class="btn">Login</button>
        </form>
        <div class="auth-footer">New here? <a href="/register">Create an account</a></div>
      </div>
    </div>
    """
    return render_template_string(BASE, content=content)


# ─────────────── DASHBOARD ───────────────
@app.route("/dashboard")
def dashboard():
    if "account" not in session:
        return redirect("/login")
    user = get_user(session["account"], session["pin"])
    if not user:
        return redirect("/login")

    txns = user.get("transactions", [])[-5:][::-1]

    def tag(t):
        typ = t.get("type", "")
        if typ == "deposit":   return '<span class="txn-tag tag-green">Deposit</span>'
        if typ == "withdraw":  return '<span class="txn-tag tag-red">Withdraw</span>'
        if typ == "transfer_out": return '<span class="txn-tag tag-amber">Transfer</span>'
        if typ == "transfer_in":  return '<span class="txn-tag tag-blue">Received</span>'
        return ""

    def icon(t):
        typ = t.get("type", "")
        colors = {
            "deposit": ("rgba(16,185,129,0.12)", "⬇"),
            "withdraw": ("rgba(244,63,94,0.12)", "⬆"),
            "transfer_out": ("rgba(245,158,11,0.12)", "↔"),
            "transfer_in": ("rgba(99,102,241,0.12)", "↙"),
        }
        bg, emoji = colors.get(typ, ("rgba(255,255,255,0.05)", "•"))
        return f'<div class="txn-icon" style="background:{bg}">{emoji}</div>'

    txn_html = ""
    if txns:
        for t in txns:
            amt = t["amount"]
            sign = "+" if t["type"] in ("deposit", "transfer_in") else "-"
            cls = "credit" if sign == "+" else "debit"
            note = t.get("note", "")
            txn_html += f"""
            <div class="txn">
              {icon(t)}
              <div class="txn-info">
                <div class="txn-name">{t.get('desc','Transaction')}</div>
                <div class="txn-meta">{t.get('date','')} {tag(t)}</div>
                {f'<div class="txn-meta" style="margin-top:2px;font-style:italic;">"{note}"</div>' if note else ''}
              </div>
              <div class="txn-amt {cls}">{sign}₹{amt:,}</div>
            </div>"""
    else:
        txn_html = '<div class="empty-state"><div class="empty-icon">💸</div><div>No transactions yet</div></div>'

    # mini income/expense stats
    all_txns = user.get("transactions", [])
    income = sum(t["amount"] for t in all_txns if t["type"] in ("deposit", "transfer_in"))
    expense = sum(t["amount"] for t in all_txns if t["type"] in ("withdraw", "transfer_out"))
    income_bars = min(5, max(0, round(income / max(income + expense, 1) * 5))) if income else 0
    expense_bars = min(5, max(0, round(expense / max(income + expense, 1) * 5))) if expense else 0

    def bars(n, color):
        return "".join([f'<div class="mbar" style="background:{color}"></div>' if i < n else '<div class="mbar"></div>' for i in range(5)])

    first_name = user['name'].split()[0]

    content = f"""
    <div class="page">
      <div class="topbar">
        <div class="logo">Smart<span>Bank</span></div>
        <div style="text-align:right">
          <div class="greeting">Good day,</div>
          <div style="font-size:14px;font-weight:600;">{user['name']}</div>
        </div>
      </div>

      <div class="balance-card">
        <div class="bal-label">Total Balance</div>
        <div class="bal-amount"><sup>₹</sup>{user['balance']:,}</div>
        <div class="bal-change">Account · {user.get('accountNo','')}</div>
        <div class="bal-acct">{user.get('email','')}</div>
      </div>

      <div class="action-grid">
        <a href="/deposit" class="action-btn">
          <div class="action-icon" style="background:rgba(16,185,129,0.12)">⬇</div>
          <div class="action-label">Deposit</div>
        </a>
        <a href="/withdraw" class="action-btn">
          <div class="action-icon" style="background:rgba(244,63,94,0.12)">⬆</div>
          <div class="action-label">Withdraw</div>
        </a>
        <a href="/transfer" class="action-btn">
          <div class="action-icon" style="background:rgba(99,102,241,0.12)">↔</div>
          <div class="action-label">Transfer</div>
        </a>
        <a href="/history" class="action-btn">
          <div class="action-icon" style="background:rgba(34,211,238,0.12)">☰</div>
          <div class="action-label">History</div>
        </a>
      </div>

      <div class="stats-row">
        <div class="stat-card">
          <div class="stat-label">Total In</div>
          <div class="stat-value" style="color:var(--green)">₹{income:,}</div>
          <div class="mini-bars">{bars(income_bars, "var(--green)")}</div>
        </div>
        <div class="stat-card">
          <div class="stat-label">Total Out</div>
          <div class="stat-value" style="color:var(--red)">₹{expense:,}</div>
          <div class="mini-bars">{bars(expense_bars, "var(--red)")}</div>
        </div>
      </div>

      <div class="section-header">
        <div class="section-title">Recent Activity</div>
        <a href="/history" class="section-link">See all →</a>
      </div>
      <div class="txn-list">{txn_html}</div>

      <div class="bottom-row">
        <a href="/logout" class="btn btn-ghost btn-danger" style="display:block;text-align:center;text-decoration:none;">Logout</a>
      </div>
    </div>
    """
    return render_template_string(BASE, content=content)


# ─────────────── DEPOSIT ───────────────
@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if "account" not in session:
        return redirect("/login")

    if request.method == "POST":
        try:
            amount = int(request.form["amount"])
        except ValueError:
            flash("Enter a valid amount.", "error")
            return redirect("/deposit")

        if amount <= 0:
            flash("Amount must be greater than zero.", "error")
            return redirect("/deposit")

        note = request.form.get("note", "").strip()
        data = load_data()
        for user in data:
            if user["accountNo"] == session["account"]:
                user["balance"] += amount
                user.setdefault("transactions", []).append({
                    "type": "deposit",
                    "desc": "Cash Deposit",
                    "amount": amount,
                    "date": now(),
                    "note": note
                })
        save_data(data)
        flash(f"₹{amount:,} deposited successfully!", "success")
        return redirect("/dashboard")

    content = """
    <div class="page">
      <div class="page-header">
        <a href="/dashboard" class="back-btn">←</a>
        <div class="page-title">Deposit Funds</div>
      </div>
      <div style="background:var(--surface);border:1px solid var(--border);border-radius:22px;padding:28px 24px;">
        <div style="text-align:center;margin-bottom:28px;">
          <div style="font-size:44px;">⬇️</div>
          <p style="color:var(--muted);font-size:13px;margin-top:8px;">Add money to your account</p>
        </div>
        <form method="POST">
          <div class="form-group">
            <label class="form-label">Amount (₹)</label>
            <div class="amount-wrapper">
              <span class="amount-prefix">₹</span>
              <input class="form-input amount-input" name="amount" type="number" placeholder="0" min="1" required>
            </div>
          </div>
          <div class="form-group">
            <label class="form-label">Note (optional)</label>
            <input class="form-input" name="note" placeholder="e.g. Salary, Freelance payment...">
          </div>
          <button type="submit" class="btn" style="background:var(--green);">Confirm Deposit</button>
        </form>
      </div>
    </div>
    """
    return render_template_string(BASE, content=content)


# ─────────────── WITHDRAW ───────────────
@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if "account" not in session:
        return redirect("/login")

    user = get_user(session["account"], session["pin"])

    if request.method == "POST":
        try:
            amount = int(request.form["amount"])
        except ValueError:
            flash("Enter a valid amount.", "error")
            return redirect("/withdraw")

        if amount <= 0:
            flash("Amount must be greater than zero.", "error")
            return redirect("/withdraw")

        if amount > user["balance"]:
            flash(f"Insufficient balance. Available: ₹{user['balance']:,}", "error")
            return redirect("/withdraw")

        note = request.form.get("note", "").strip()
        data = load_data()
        for u in data:
            if u["accountNo"] == session["account"]:
                u["balance"] -= amount
                u.setdefault("transactions", []).append({
                    "type": "withdraw",
                    "desc": "Cash Withdrawal",
                    "amount": amount,
                    "date": now(),
                    "note": note
                })
        save_data(data)
        flash(f"₹{amount:,} withdrawn successfully!", "success")
        return redirect("/dashboard")

    content = f"""
    <div class="page">
      <div class="page-header">
        <a href="/dashboard" class="back-btn">←</a>
        <div class="page-title">Withdraw Funds</div>
      </div>
      <div style="background:var(--surface);border:1px solid var(--border);border-radius:22px;padding:28px 24px;">
        <div style="text-align:center;margin-bottom:16px;">
          <div style="font-size:44px;">⬆️</div>
        </div>
        <div class="acct-strip" style="margin-bottom:20px;">
          <div>
            <div class="acct-strip-label">Available Balance</div>
            <div class="acct-strip-val" style="font-size:20px;color:var(--green)">₹{user['balance']:,}</div>
          </div>
        </div>
        <form method="POST">
          <div class="form-group">
            <label class="form-label">Amount (₹)</label>
            <div class="amount-wrapper">
              <span class="amount-prefix">₹</span>
              <input class="form-input amount-input" name="amount" type="number" placeholder="0" min="1" max="{user['balance']}" required>
            </div>
          </div>
          <div class="form-group">
            <label class="form-label">Note (optional)</label>
            <input class="form-input" name="note" placeholder="e.g. Rent, Groceries...">
          </div>
          <button type="submit" class="btn" style="background:var(--red);">Confirm Withdrawal</button>
        </form>
      </div>
    </div>
    """
    return render_template_string(BASE, content=content)


# ─────────────── TRANSFER ───────────────
@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    if "account" not in session:
        return redirect("/login")

    sender = get_user(session["account"], session["pin"])

    if request.method == "POST":
        to_account = request.form["to_account"].strip()
        try:
            amount = int(request.form["amount"])
        except ValueError:
            flash("Enter a valid amount.", "error")
            return redirect("/transfer")

        note = request.form.get("note", "").strip()

        if to_account == session["account"]:
            flash("Cannot transfer to your own account.", "error")
            return redirect("/transfer")

        if amount <= 0:
            flash("Amount must be greater than zero.", "error")
            return redirect("/transfer")

        if amount > sender["balance"]:
            flash(f"Insufficient balance. Available: ₹{sender['balance']:,}", "error")
            return redirect("/transfer")

        data = load_data()
        recipient = next((u for u in data if u["accountNo"] == to_account), None)

        if not recipient:
            flash("Recipient account not found.", "error")
            return redirect("/transfer")

        for u in data:
            if u["accountNo"] == session["account"]:
                u["balance"] -= amount
                u.setdefault("transactions", []).append({
                    "type": "transfer_out",
                    "desc": f"Transfer to {recipient['name']}",
                    "amount": amount,
                    "date": now(),
                    "note": note
                })
            if u["accountNo"] == to_account:
                u["balance"] += amount
                u.setdefault("transactions", []).append({
                    "type": "transfer_in",
                    "desc": f"Transfer from {sender['name']}",
                    "amount": amount,
                    "date": now(),
                    "note": note
                })
        save_data(data)
        flash(f"₹{amount:,} transferred to {recipient['name']} successfully!", "success")
        return redirect("/dashboard")

    content = f"""
    <div class="page">
      <div class="page-header">
        <a href="/dashboard" class="back-btn">←</a>
        <div class="page-title">Transfer Funds</div>
      </div>
      <div style="background:var(--surface);border:1px solid var(--border);border-radius:22px;padding:28px 24px;">
        <div style="text-align:center;margin-bottom:16px;">
          <div style="font-size:44px;">↔️</div>
        </div>
        <div class="acct-strip">
          <div>
            <div class="acct-strip-label">Your Balance</div>
            <div class="acct-strip-val" style="color:var(--green)">₹{sender['balance']:,}</div>
          </div>
          <div style="text-align:right;">
            <div class="acct-strip-label">From</div>
            <div class="acct-strip-val">{sender['accountNo']}</div>
          </div>
        </div>
        <form method="POST">
          <div class="form-group">
            <label class="form-label">Recipient Account Number</label>
            <input class="form-input" name="to_account" placeholder="e.g. $I3M1Z3" required style="letter-spacing:2px;">
          </div>
          <div class="form-group">
            <label class="form-label">Amount (₹)</label>
            <div class="amount-wrapper">
              <span class="amount-prefix">₹</span>
              <input class="form-input amount-input" name="amount" type="number" placeholder="0" min="1" required>
            </div>
          </div>
          <div class="form-group">
            <label class="form-label">Note (optional)</label>
            <input class="form-input" name="note" placeholder="e.g. Rent split, Birthday gift...">
          </div>
          <button type="submit" class="btn">Transfer Now</button>
        </form>
      </div>
    </div>
    """
    return render_template_string(BASE, content=content)


# ─────────────── HISTORY ───────────────
@app.route("/history")
def history():
    if "account" not in session:
        return redirect("/login")

    user = get_user(session["account"], session["pin"])
    txns = user.get("transactions", [])[::-1]

    def tag(t):
        typ = t.get("type", "")
        if typ == "deposit":       return '<span class="txn-tag tag-green">Deposit</span>'
        if typ == "withdraw":      return '<span class="txn-tag tag-red">Withdraw</span>'
        if typ == "transfer_out":  return '<span class="txn-tag tag-amber">Sent</span>'
        if typ == "transfer_in":   return '<span class="txn-tag tag-blue">Received</span>'
        return ""

    def icon(t):
        typ = t.get("type", "")
        colors = {
            "deposit": ("rgba(16,185,129,0.12)", "⬇"),
            "withdraw": ("rgba(244,63,94,0.12)", "⬆"),
            "transfer_out": ("rgba(245,158,11,0.12)", "↔"),
            "transfer_in": ("rgba(99,102,241,0.12)", "↙"),
        }
        bg, emoji = colors.get(typ, ("rgba(255,255,255,0.05)", "•"))
        return f'<div class="txn-icon" style="background:{bg}">{emoji}</div>'

    rows = ""
    if txns:
        for t in txns:
            sign = "+" if t["type"] in ("deposit", "transfer_in") else "-"
            cls = "credit" if sign == "+" else "debit"
            note = t.get("note", "")
            rows += f"""
            <div class="txn">
              {icon(t)}
              <div class="txn-info">
                <div class="txn-name">{t.get('desc','Transaction')}</div>
                <div class="txn-meta">{t.get('date','')} {tag(t)}</div>
                {f'<div class="txn-meta" style="margin-top:2px;font-style:italic;">"{note}"</div>' if note else ''}
              </div>
              <div class="txn-amt {cls}">{sign}₹{t['amount']:,}</div>
            </div>"""
    else:
        rows = '<div class="empty-state"><div class="empty-icon">📭</div><div>No transactions yet</div></div>'

    content = f"""
    <div class="page">
      <div class="page-header">
        <a href="/dashboard" class="back-btn">←</a>
        <div class="page-title">Transaction History</div>
      </div>
      <div style="background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:var(--radius);padding:14px 16px;margin-bottom:20px;display:flex;justify-content:space-between;">
        <div>
          <div style="font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:3px;">Account</div>
          <div style="font-size:13px;font-weight:600;letter-spacing:1px;">{user['accountNo']}</div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:3px;">Total Transactions</div>
          <div style="font-size:13px;font-weight:600;">{len(user.get('transactions', []))}</div>
        </div>
      </div>
      <div class="txn-list">{rows}</div>
    </div>
    """
    return render_template_string(BASE, content=content)


# ─────────────── LOGOUT ───────────────
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)