# Website Blocker
This script blocks "distracting" websites that affects productivity.

The script is set to block Facebook and Gmail between the hours of 8AM - 4PM.

You can modify the websites by adjusting the variables in block_website.

You can modify the times by adjusting the variable 8 (for 8AM) and 16 (for 4PM) in this line:

if dt(dt.now().year, dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month,dt.now().day,16):

Please remember the time is set in a 24 hour format (i.e., 20 = 8PM, 13 = 1PM, etc.)

If you have any questions please ask me via email at mymobiservices@gmail.com
