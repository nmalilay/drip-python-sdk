# Drip Python SDK - Quickstart

Get up and running in 30 seconds.

## Steps

```bash
# 1. Clone the SDK
git clone https://github.com/nmalilay/drip-python-sdk.git
cd drip-python-sdk

# 2. Install
pip install -e .

# 3. Set your API key
export DRIP_API_KEY=sk_live_your_key_here

# 4. Run
cd quickstart
python main.py
```

You can also put the key in a `.env` file:

```bash
echo 'DRIP_API_KEY=sk_live_your_key_here' > quickstart/.env
```

## What it does

1. Pings the API to check it's alive
2. Creates a customer (or finds existing one)
3. Tracks a usage event (1 API call)
4. Records a run with events (500 tokens)
5. Checks the customer's balance

## Next steps

- See the [full SDK docs](../README.md) for all available methods
- Use `from drip import drip` for a pre-initialized singleton
- Add middleware for [FastAPI](../src/drip/middleware/fastapi.py) or [Flask](../src/drip/middleware/flask.py)
