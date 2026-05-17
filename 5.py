import sys

# Define customer intents and responses
responses = {
    "hi": "Hello! Welcome to Apex Bank Support. How can I help you today?",
    "hello": "Hello! Welcome to Apex Bank Support. How can I help you today?",
    "balance": "To check your account balance, please log into our mobile app or text BAL to 56767.",
    "loan": "We offer Home, Car, and Personal loans at attractive interest rates starting from 7.5%.",
    "card": "To report a lost or stolen credit/debit card, please block it instantly via our net banking app.",
    "timing": "Our branches are open Monday to Friday from 10:00 AM to 4:00 PM.",
    "bye": "Thank you for banking with us. Have a great day ahead!"
}

print("🤖 Apex Bank Chatbot initialized! (Type 'bye' to exit)\n" + "-"*50)

while True:
    user_input = input("You: ").strip().lower()
    
    # Simple rule-based keyword matching loop
    matched_reply = next((responses[key] for key in responses if key in user_input), None)
    
    if matched_reply:
        print(f"Bot: {matched_reply}")
        if "bye" in user_input: sys.exit()
    else:
        print("Bot: I'm sorry, I didn't quite catch that. Can you please rephrase your query?")
