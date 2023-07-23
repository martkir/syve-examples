import requests
import json
import time


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


def main():
    fetch_start = time.time()
    records = sql_monthly_nft_transfer_count(nmonths=6)
    fetch_took = time.time() - fetch_start
    print(json.dumps(records, indent=4))
    print("Took: %.2f seconds" % fetch_took)


if __name__ == "__main__":
    main()
