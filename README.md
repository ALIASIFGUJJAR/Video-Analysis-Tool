# Video Analysis Tool

A simple web tool that helps you edit videos with cool effects. Built with Flask for smooth video processing.

## Main Features

### 1. Transformations
- Turn video sideways (90°)
- Flip video left-right
- Flip video up-down
- All transformations are handled by Flask's powerful back-end

### 2. Filtering
- Make video blurry
- Make video sharper
- Remove video noise
- Real-time filtering with Flask processing

### 3. Convolution
- Show edges in video
- Add 3D look
- Make video look like a cartoon
- Advanced convolution effects powered by Flask

### 4. Effects
- Make video black and white
- Add old-time movie look
- Reverse video colors
- Smooth effect processing through Flask

## How It Works

### FFmpeg's Role
FFmpeg is our main video processor that:
- Handles video loading and format conversion
- Applies effects using special filters
- Makes processing faster with GPU support
- Ensures high-quality output
- Manages video streams efficiently

### OpenCV's Role
OpenCV works as our backup processor that:
- Steps in if FFmpeg isn't available
- Provides additional video effects
- Helps with image processing
- Ensures the tool always works

### Working Together
- FFmpeg tries first for fast processing
- OpenCV helps if FFmpeg can't do something
- Both work through Flask to give you results
- You don't need to worry about which one is working

## Cool Features
- See your video before you edit it
- Just drag and drop your video
- Fast video editing
- Works even if some features aren't available
- Easy to use
- Shows progress while working

## How to Start

1. Get Python 3.8 or newer
2. Get FFmpeg:
   - Windows: Get it from https://ffmpeg.org/download.html
   - Put it in your computer's PATH
   - This is needed for fast video processing

3. Make a virtual space:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

4. Get the tools:
   ```bash
   pip install -r requirements.txt
   ```

5. Start the tool:
   ```bash
   python app.py
   ```

## What's Inside

```
video-analysis-tool/
├── app.py                 # Main program (Flask server)
├── static/               # Files and videos
│   └── uploads/         # Where videos go
├── templates/           # Web pages
│   └── index.html      # Main page
├── utils/              # Helper tools
│   ├── video_processor.py  # Video editor (FFmpeg/OpenCV)
│   └── effects.py         # Effects maker (OpenCV)
└── requirements.txt     # Needed tools
```

## How to Use

1. Go to `http://localhost:5000` in your web browser
2. Put in your video (works with MP4, AVI, MOV, MKV)
3. Watch your video in the player
4. Pick what you want to do:
   - Basic changes (turn, flip)
   - Make it look better (blur, sharpen)
   - Special effects (edges, 3D, cartoon)
   - Color changes (black & white, old-time look)
5. Wait while it works
6. Get your new video

## What You Need

- Python 3.8 or newer
- FFmpeg (works better with GPU)
- Any new web browser
- Videos under 500MB

## Tools We Use

- Flask==2.3.3 (Our web server)
- opencv-python==4.8.0.74 (For video effects)
- numpy==1.24.3 (For math operations)
- ffmpeg-python==0.2.0 (For video processing)
- python-dotenv==1.0.0 (For settings)
- Werkzeug==2.3.7 (For web tools) 