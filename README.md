# whatsapp-chat-extractor
Python script to extract relevant information from a WhatsApp conversation

WhatsApp's email conversation feature emails you a text file of your conversation with someone/in a group. This script will extract metadata, namely time, author, group and actual message and store it in a sqlalchemy table.

This can be used as a base for performing some interesting analytics using pandas: what is the average length of your messages when conversing with someone/in a group, how many times do you initiate a conversation versus the other person initiating, the timings/frequency of your messages, frequency of your emojis, etc. All of these metrics can be found out with respect to a person or as an overall measure.
