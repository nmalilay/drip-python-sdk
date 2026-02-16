"""
Drip Python SDK - Quickstart

Creates a customer, tracks usage, and records a run.

Usage:
    pip install drip-sdk
    export DRIP_API_KEY=sk_live_your_key_here
    python main.py
"""

from drip import Drip

def main():
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
