# 0x0E. Web stack debugging #1

It's 12:00 AM (or 00:00), in the middle of your sleep you get a call from your boss that somehow the web page is down. "What.", you say to yourself, "How did the web page go down if I didn't touch it for a full month?". You tell your boss to calm down and that you'll see what's going on.

After doing some research, turns out that Nginx is trying to *use the port 8080 instead of port 80*. Thus, another bug hunting (debugging) session begins.
