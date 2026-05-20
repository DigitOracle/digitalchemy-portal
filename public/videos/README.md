# Video Drop Folder

Drop section videos here using the filenames listed in `../../README.md`.

Each section card in `index.html` probes for its file at page load via a `HEAD` request to `public/videos/<key>.mp4`. If the file is present, the placeholder is replaced with an autoplay-muted-loop `<video>` element. No code change required.

## Recommended encoding

```powershell
# H.264 MP4 · 1920×1080 · web-optimised
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset slow -c:a aac -b:a 96k -movflags +faststart output.mp4
```

Keep individual files under ~10 MB for fast first paint. For hero, 15–30 seconds at 1080p (or 720p) is plenty.

## Provenance note

Per DigitAlchemy® brand rules, AI-generated video content carries DigitOracle® watermark. HeyGen-exported videos already meet this. Pexels stock does not require watermark.
