# PriceSync — Marketplace Upload Converter

Internal tool for generating ready-to-upload price files for Shopee, TikTok, and Lazada.

## What it does
1. Upload marketplace inventory report + client memo pricelist
2. Auto-joins SKU codes, applies discount prices, checks RRP
3. Runs QC (zero stock, RRP mismatch, unmatched SKUs)
4. Downloads the filled upload template

## Supported Marketplaces
- **Shopee** — Discount Promotion & Live Promotion
- **TikTok Shop**
- **Lazada** — with promo date fields

## Repo structure
```
pricesync/
├── app.py            ← Streamlit entry point
├── pricesync.html    ← Full React app (auto-generated, do not edit manually)
├── requirements.txt  ← Python dependencies
└── README.md
```

## Updating the app
When the app logic changes:
1. Get the new `App.jsx` and `pricesync.html` from Claude
2. Replace `pricesync.html` in the repo
3. Push to GitHub → Streamlit auto-redeploys

## Local development
```bash
pip install streamlit
streamlit run app.py
```
