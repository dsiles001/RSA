# RSA (This is simply a demo. This should not be used for real world application as the prime numbers generated are much smaller than what they should be in order to improve security. The prime numbers generated can be modified inside the makeKeys() function.) 

Obviously, in order to use full functionality, there should be two participants when using this script, or at the least two terminal sessions.

1. On both ends of the exchange, input if you are sending a message (1) or receiving a message (2).
2. The receiver will be given his/her public keys, their n and e values. These values will have to be given to the sender. At this point the sender has also been given a prompt to enter the receiver's public keys.
3. Once the sender has inputed the receiver's public keys, he/she will be prompted to enter the message they would like to send.
4. Once the message has been encrypted, it will be displayed as num, num, num... These values will be given to the recepient in the same format they were displayed (num, num, num...)
5. Once they receiver has inputed the encrypted values, they will be shown the message the sender inputed.
