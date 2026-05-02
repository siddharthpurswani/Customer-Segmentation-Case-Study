import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# ── Cluster metadata ─────────────────────────────────────────────────────────
CLUSTER_INFO = {
    0: {
        "label": "At-Risk / Lapsed",
        "badge": "at-risk",
        "description": "Hasn't purchased recently, low frequency and spend.",
        "suggestions": [
            "Send a personalised re-engagement email with a discount code.",
            "Run a win-back campaign — ask why they left.",
            "Offer a limited-time incentive to return (e.g. free shipping).",
            "Share a feedback survey to understand their experience.",
        ],
    },
    1: {
        "label": "Champion / Loyal",
        "badge": "loyal",
        "description": "Shops frequently, recently, and spends the most.",
        "suggestions": [
            "Offer exclusive early access to new products.",
            "Enrol in a VIP loyalty or rewards programme.",
            "Invite as a brand ambassador or for referral incentives.",
            "Up-sell / cross-sell premium or complementary items.",
        ],
    },
    2: {
        "label": "Potential Loyalist",
        "badge": "potential",
        "description": "Balanced RFM score — strong growth opportunity.",
        "suggestions": [
            "Send personalised product recommendations based on past purchases.",
            "Introduce a loyalty points programme to boost frequency.",
            "Offer a moderate bulk-buy discount to increase order value.",
            "Follow up after purchases to build the relationship.",
        ],
    },
}

# ── Load RFM lookup table once at startup ────────────────────────────────────
try:
    rfm_lookup = pd.read_csv("rfm_lookup.csv")
    rfm_lookup["CustomerID"] = rfm_lookup["CustomerID"].astype(str).str.strip()
    print(f"[startup] Loaded {len(rfm_lookup):,} customers from rfm_lookup.csv")
except FileNotFoundError:
    rfm_lookup = None
    print("[startup] WARNING: rfm_lookup.csv not found.")


# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if rfm_lookup is None:
        return jsonify({"error": "rfm_lookup.csv not loaded. Please check the server."}), 500

    data = request.get_json()
    customer_id = str(data.get("customer_id", "")).strip()

    if not customer_id:
        return jsonify({"error": "Please enter a Customer ID."}), 400

    row = rfm_lookup[rfm_lookup["CustomerID"] == customer_id]

    if row.empty:
        return jsonify({"error": f"Customer ID '{customer_id}' not found in records."}), 404

    row = row.iloc[0]
    cluster = int(row["Cluster"])
    info = CLUSTER_INFO[cluster]

    return jsonify({
        "customer_id": customer_id,
        "cluster": cluster,
        "label": info["label"],
        "badge": info["badge"],
        "description": info["description"],
        "suggestions": info["suggestions"],
        "rfm": {
            "recency": int(row["Recency"]),
            "frequency": int(row["Frequency"]),
            "monetary": round(float(row["Monetary"]), 2),
        },
    })


if __name__ == "__main__":
    app.run(debug=True)