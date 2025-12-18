udr-display-hijack

Custom screen display for the Ubiquiti Dream Router 7.

Find an image or GIF you like.
Best results are 160px tall × 80px wide (1:2 portrait).

Resize or crop your media to 160×80

Run convert.py to convert it to .raw (format the DR7 display accepts)

Copy the output to the router

Edit hijack-display.sh to point to the frame folder and adjust the frame delay

Run the script

Press Ctrl+C to stop playback and restore the default UI.

Enjoy.

Future plans

Run as a background process at startup

Start/stop via a simple command or service

React to router state (WAN down, client count, throughput, etc.)
