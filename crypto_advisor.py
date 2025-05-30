# Rule-based Crypto Advisor Chatbot

# Predefined dataset of cryptocurrencies
crypto_data = {
    'Bitcoin': {
        'price_trend': 'rising',
        'market_cap': 'high',
        'energy_use': 'high',
        'sustainability_score': 5
    },
    'Ethereum': {
        'price_trend': 'rising',
        'market_cap': 'high',
        'energy_use': 'medium',
        'sustainability_score': 6
    },
    'Cardano': {
        'price_trend': 'rising',
        'market_cap': 'medium',
        'energy_use': 'low',
        'sustainability_score': 9
    },
    'Dogecoin': {
        'price_trend': 'falling',
        'market_cap': 'medium',
        'energy_use': 'medium',
        'sustainability_score': 4
    }
}

# Main chatbot logic
def crypto_advisor():
    print("Welcome to the Crypto Advisor Chatbot!")
    print("Ask about 'profitability', 'sustainability', or 'long-term growth'")
    user_input = input("What are you interested in? ").strip().lower()

    recommendations = []

    if user_input == "profitability":
        for coin, data in crypto_data.items():
            if data['price_trend'] == 'rising' and data['market_cap'] == 'high':
                recommendations.append(f"{coin} is rising in price and has high market cap—likely profitable.")
    
    elif user_input == "sustainability":
        for coin, data in crypto_data.items():
            if data['energy_use'] == 'low' and data['sustainability_score'] > 7:
                recommendations.append(f"{coin} is eco-friendly and scores high on sustainability.")

    elif user_input == "long-term growth":
        for coin, data in crypto_data.items():
            if (data['price_trend'] == 'rising' and 
                data['energy_use'] == 'low' and 
                data['sustainability_score'] > 7):
                recommendations.append(f"{coin} is trending up and eco-friendly—great for long-term growth!")

    else:
        print("Sorry, I can only advise on profitability, sustainability, or long-term growth.")
        return

    if recommendations:
        print("\nHere are some suggestions:")
        for rec in recommendations:
            print("•", rec)
    else:
        print("No strong recommendations based on current data.")

    # Disclaimer
    print("\n⚠️ Crypto is risky—always do your own research (DYOR)!")

# Run the chatbot
if __name__ == "__main__":
    crypto_advisor()

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_by_id('bitcoin')
print(bitcoin_data['market_data']['current_price']['usd'])
