from PIL import Image, ImageSequence
import os
import sys

WIDTH = 80
HEIGHT = 160

def rgb888_to_rgb565_le(img):
    raw = bytearray()
    for r, g, b in img.getdata():
        rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
        raw.append(rgb565 & 0xFF)         # low byte
        raw.append((rgb565 >> 8) & 0xFF)  # high byte
    return raw
    
def convert_image(path):
    base = os.path.splitext(os.path.basename(path))[0]
    out = f"{base}.raw"
    img = Image.open(path).convert("RGB").resize((WIDTH, HEIGHT))
    raw = rgb888_to_rgb565_le(img)
    with open(out, "wb") as f:
        f.write(raw)
    print(f"Wrote {out} ({len(raw)} bytes)")
    
def convert_video_or_gif(path):
    base = os.path.splitext(os.path.basename(path))[0]
    outdir = f"{base}_frames"
    os.makedirs(outdir, exist_ok=True)
    img = Image.open(path)
    frame_count = 0
    for frame in ImageSequence.Iterator(img):
        frame = frame.convert("RGB").resize((WIDTH, HEIGHT))
        raw = rgb888_to_rgb565_le(frame)
        out = os.path.join(outdir, f"frame_{frame_count:03}.raw")
        with open(out, "wb") as f:
            f.write(raw)
        frame_count += 1
    print(f"Wrote {frame_count} frames to {outdir}/")

def main():
    kind = input("Convert image or video? [i/v]: ").strip().lower()
    path = input("Enter filename: ").strip()
    if not os.path.isfile(path):
        print("File not found")
        sys.exit(1)
    if kind == "i":
        convert_image(path)
    elif kind == "v":
        convert_video_or_gif(path)
    else:
        print("Invalid choice (use i or v)")
        sys.exit(1)

if __name__ == "__main__":
    main()

