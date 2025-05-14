import cv2
import numpy as np
import ffmpeg
import os
from .effects import apply_effect

class VideoProcessor:
    def __init__(self, input_path):
        self.input_path = input_path
        self.cap = cv2.VideoCapture(input_path)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def process_video(self, effect, output_path):
        try:
            # Get video information using FFmpeg
            probe = ffmpeg.probe(self.input_path)
            video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
            
            # Set up FFmpeg input
            stream = ffmpeg.input(self.input_path)
            
            # Apply effects based on the selected effect
            if effect == 'grayscale':
                stream = stream.filter('hue', s=0)
            elif effect == 'blur':
                stream = stream.filter('gblur', sigma=5)
            elif effect == 'edge_detection':
                stream = stream.filter('edgedetect', mode='canny')
            elif effect == 'sepia':
                stream = stream.filter('colorchannelmixer', rr=0.393, gg=0.769, bb=0.189)
            elif effect == 'invert':
                stream = stream.filter('negate')
            elif effect == 'sharpen':
                stream = stream.filter('unsharp', luma_msize_x=5, luma_msize_y=5, luma_amount=1.5)
            elif effect == 'cartoon':
                # Apply multiple filters for cartoon effect
                stream = stream.filter('hqdn3d')  # Denoise
                stream = stream.filter('colorlevels', rimin=0, gimin=0, bimin=0, rimax=0.9, gimax=0.9, bimax=0.9)
                stream = stream.filter('edgedetect', mode='canny')
            elif effect == 'emboss':
                stream = stream.filter('convolution', '0 -1 0 -1 1 1 0 1 0:0 -1 0 -1 1 1 0 1 0:0 -1 0 -1 1 1 0 1 0:0 -1 0 -1 1 1 0 1 0')
            elif effect == 'noise_reduction':
                stream = stream.filter('hqdn3d', luma_spatial=4, chroma_spatial=3)
            elif effect == 'rotate_90':
                stream = stream.filter('transpose', 1)  # Rotate 90 degrees clockwise
            elif effect == 'flip_horizontal':
                stream = stream.filter('hflip')
            elif effect == 'flip_vertical':
                stream = stream.filter('vflip')
            
            # Set up output with FFmpeg
            stream = stream.output(
                output_path,
                acodec='copy',  # Copy audio without re-encoding
                vcodec='libx264',  # Use H.264 codec
                preset='medium',  # Encoding preset
                crf=23  # Constant Rate Factor for quality
            )
            
            # Run FFmpeg command
            stream.overwrite_output().run(capture_stdout=True, capture_stderr=True)
            
            return output_path
            
        except ffmpeg.Error as e:
            print('FFmpeg error:', e.stderr.decode())
            # Fallback to OpenCV if FFmpeg fails
            return self._process_with_opencv(effect, output_path)
        finally:
            if hasattr(self, 'cap'):
                self.cap.release()

    def _process_with_opencv(self, effect, output_path):
        """Fallback method using OpenCV if FFmpeg processing fails"""
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, self.fps, (self.frame_width, self.frame_height))
        
        frame_count = 0
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            
            # Apply the selected effect
            processed_frame = apply_effect(frame, effect)
            
            # Write the processed frame
            out.write(processed_frame)
            
            frame_count += 1
            if frame_count % 30 == 0:  # Log progress every 30 frames
                progress = (frame_count / self.total_frames) * 100
                print(f"Processing: {progress:.1f}%")
        
        # Release resources
        out.release()
        
        return output_path

    def __del__(self):
        if hasattr(self, 'cap'):
            self.cap.release() 