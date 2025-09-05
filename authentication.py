from azure.identity import DefaultAzureCredential
from azure.communication.identity import CommunicationIdentityClient
from azure.communication.sms import SmsClient

credential = DefaultAzureCredential()


def create_identity_and_get_token(resource_endpoint):
    client = CommunicationIdentityClient(resource_endpoint, credential)
    user, token_response = client.create_user_and_token(scopes=["voip"])

    return token_response


def send_sms(resource_endpoint, from_phone_number, to_phone_number, message_content):
    sms_client = SmsClient(resource_endpoint, credential)

    response = sms_client.send(
        from_=from_phone_number,
        to=[to_phone_number],
        message=message_content,
        enable_delivery_report=True  # optional property
    )
    return response


# You can find your endpoint and access key from your resource in the Azure portal
# e.g. "https://<RESOURCE_NAME>.communication.azure.com";
endpoint = "https://<RESOURCE_NAME>.communication.azure.com/"

print("Retrieving new Access Token, using Service Principals")
result = create_identity_and_get_token(endpoint)
print(f'Retrieved Access Token: {result.token}')

print("Sending SMS using Service Principals")

# You will need a phone number from your resource to send an SMS.
sms_result = send_sms(endpoint, "<FROM_NUMBER>",
                      "<TO_NUMBER>", "Hello from Service Principals")
print(f'SMS ID: {sms_result[0].message_id}')
print(f'Send Result Successful: {sms_result[0].successful}')
