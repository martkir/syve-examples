# syve-examples

### Monthly NFT Transfer Counts

Below is an example in both **cURL** and **Python** of how to get the monthly NFT transfer counts for the last 12 months. The code will execute in about 2.5 seconds.

**cURL**

```
curl -X POST https://api.syve.ai/v1/sql \
-H "Content-Type: application/json" \
-d '{
    "query": "SELECT HISTOGRAM(\"timestamp\", INTERVAL 1 MONTH) AS month, COUNT(*) as transfer_count FROM eth_erc721 WHERE \"timestamp\" >= NOW() - INTERVAL '\''12'\'' MONTH GROUP BY month ORDER BY month"
}'
```

**Python**

```
def sql_monthly_nft_transfer_count(nmonths=12):
    query_str = f"""
    SELECT \
        HISTOGRAM("@timestamp", INTERVAL 1 MONTH) AS month, \
        COUNT(*) as transfer_count \
    FROM eth_erc721 \
    WHERE "timestamp" >= NOW() - INTERVAL '{nmonths}' MONTH \
    GROUP BY month \
    ORDER BY month
    """
    query = {"query": query_str}
    url = "https://api.syve.ai/v1/sql"
    response = requests.post(url, json=query)
    records = response.json()
    return records
```

Run the following command:

```python monthly_nft_transfer_counts.py```

