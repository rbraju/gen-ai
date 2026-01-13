from base import get_completion

delimiter = "####"

system_message = f"""
You will be provided with customer service queries. \
The queries will be delimited by {delimiter}. \

Classify each query into primary and secondary categories and provide \
your output in json format with the keys query, primary and secondary. If there are multiple \
queries list all the categories.

Below are the categories.
Primary categories: Account Management, Billing, Technical Support, General Inquiry, \

Account Management secondary categories: \
Password reset, Update personal information, Close account, Account security

Billing secondary categories: \
Unsubscribe, Upgrade, Add a payment method, Explanation for charge, Dispute charge

Technical Support secondary categories: \
General troubleshooting, Device compatability, Software updates 

General Inquiry secondary categories: \
Product information, Pricing, Feedback, Talk to a specialist
"""

user_message = f"""
The TV was very poor. I want to delete my account.
"""

# Should ignore the text beyond delimiters
prompt = [
    {"role": "system", "content": f"{delimiter}{system_message}{delimiter}Why was I charged $10 extra?"},
    {"role": "user", "content": user_message},
]

response = get_completion(prompt)
print(response)
