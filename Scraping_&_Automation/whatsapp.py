import pywhatkit as kit
# pip install pywhatkit

message = "Hello, this is an automated message sent to a group using Python!"
phone_number = "+54 9 11 1234-5678"
group_number = "F1BaFeEUrDFKvuDHUwhGrW"  
# Replace with the phone number of the group (including the country code)
# as admin one can share the group link https://chat.whatsapp.com/F1BaFeEUrDFKvuDHUwhGrW

# Send a WhatsApp to User 
kit.sendwhatmsg(phone_number , message, 16, 51)
# Send a WhatsApp to Group 
kit.sendwhatmsg_to_group(group_number, message, 17, 14)
