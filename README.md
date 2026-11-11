# Time Based One Time Password USB
Raspberry Pi Pico 2W with the pico explorer to display the code.



How Verification Works:

Website End:

  1. Stores your secret key (when you first set it up)
  
  2. Receives your typed code +current time
  
  3. Computes the expected code using the SAME secret +current time


Raspberry Pico 2W End:

  1. Makes 6-digit code from shared secret +current time

  2. You TYPE the code into the websites text box, and login




