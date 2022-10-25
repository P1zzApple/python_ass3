import requests

url = "https://solana-gateway.moralis.io/nft/mainnet/An36Gv8UFt6YW4rGdtdZu3BKWqJQVsFwRb5haRJwF2cK/metadata"

headers = {
    "accept": "application/json",
    "X-API-Key": "bLWa5EaQFs9umsZIshcBL1zoawIYShqQlMHXdiF7Y7HbxvV7wZvmJIxjibhA1Pcm"
}

response = requests.get(url, headers=headers)
result = response.text
#print(result)
