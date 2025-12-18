# udr-display-hijack

Custom screen display for the **Ubiquiti Dream Router 7**.

Find an image or GIF you like.  
Best results are **160px tall × 80px wide** (1:2 portrait).

1. Resize or crop your media to **160×80**
   - [Online GIF crop tool](https://www.iloveimg.com/crop-image/crop-gif)
2. Run `convert.py` to convert it to `.raw` (format the DR7 display accepts)
3. Copy the output to the router via scp or whateva
4. Edit `hijack-display.sh` to point to the frame folder and adjust the frame delay
5. Run the script

Press `Ctrl+C` to stop playback and restore the default UI.

Enjoy.

## Future plans

- Run as a background process at startup
- Start/stop via a simple command or service
- React to router state (WAN down, client count, throughput, etc.)
