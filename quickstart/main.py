"""
Drip Python SDK - Quickstart

Creates a customer, tracks usage, and records a run.

Usage:
    pip install drip-sdk
    export DRIP_API_KEY=sk_live_your_key_here
    python main.py

Or put your key in a .env file:
    echo 'DRIP_API_KEY=sk_live_your_key_here' > .env
    python main.py
"""

import os

def load_dotenv(path):
    """Load .env file into environment variables."""
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' not in line:
                    continue
                key, val = line.split('=', 1)
                val = val.strip()
                if len(val) >= 2 and val[0] in ('"', "'") and val[-1] == val[0]:
                    val = val[1:-1]
                os.environ.setdefault(key.strip(), val)
    except FileNotFoundError:
        pass

from drip import Drip

def main():
    load_dotenv('../.env')
    load_dotenv('.env')

    client = Drip()
    print("Connected to Drip API")

    # Ping
    health = client.ping()
    is_ok = health.get("ok") if isinstance(health, dict) else health.ok
    latency = health.get("latency_ms") if isinstance(health, dict) else health.latency_ms
    print(f"Ping: {'OK' if is_ok else 'FAIL'} ({latency}ms)")

    # Get or create customer
    try:
        customer = client.create_customer(external_customer_id="quickstart_user")
        print(f"Created customer: {customer.id}")
    except Exception:
        customers = client.list_customers()
        customer = next(c for c in customers.data if c.external_customer_id == "quickstart_user")
        print(f"Found existing customer: {customer.id}")

    # Track usage
    result = client.track_usage(
        customer_id=customer.id,
        meter="api_calls",
        quantity=1,
    )
    print(f"Usage tracked: {result.usage_event_id}")

    # Record a run (e.g. an AI inference job)
    run_result = client.record_run(
        customer_id=customer.id,
        workflow="quickstart-workflow",
        status="COMPLETED",
        events=[
            {
                "event_type": "inference",
                "quantity": 500,
                "units": "tokens",
            }
        ],
    )
    print(f"Run recorded: {run_result.run.id}")

    # Check balance
    balance = client.get_balance(customer.id)
    print(f"Balance: {balance.balance_usdc} USDC")

    print("Done! SDK is working.")


if __name__ == "__main__":
    main()
