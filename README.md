<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Person Counter in Video using YOLOv8 and OpenCV</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
            padding: 2em;
            background: #fff;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        h2 {
            color: #555;
        }
        pre {
            background: #333;
            color: #fff;
            padding: 10px;
            overflow-x: auto;
        }
        code {
            background: #eee;
            padding: 2px 4px;
            font-size: 90%;
            color: #c7254e;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Person Counter in Video using YOLOv8 and OpenCV</h1>
        <p>This project uses YOLOv8 and OpenCV to detect and count the number of people in a video in real-time.</p>

        <h2>Prerequisites</h2>
        <p>Make sure you have the following installed on your machine:</p>
        <ul>
            <li>Python 3.7 or higher</li>
            <li>pip (Python package manager)</li>
            <li>Git</li>
        </ul>

        <h2>Installation</h2>
        <p>Clone the repository:</p>
        <pre><code>git clone https://github.com/your-username/person-counter-yolov8.git
cd person-counter-yolov8
</code></pre>
        
        <p>Create and activate a virtual environment (optional but recommended):</p>
        <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
</code></pre>
        
        <p>Install the dependencies:</p>
        <pre><code>pip install -r requirements.txt
</code></pre>

        <h2>Usage</h2>
        <p>Download the YOLOv8 model weights and place them in the <code>weights</code> directory. You can get them from the <a href="https://github.com/ultralytics/yolov5/releases" target="_blank">Ultralytics YOLOv8 repository</a>.</p>
        <p>Ensure you have an input video. Place it in the <code>videos</code> directory.</p>
        <p>Run the main script:</p>
        <pre><code>python main.py --video_path videos/your_video.mp4 --output_path output/your_output.mp4
</code></pre>
        <p>You can specify the input video path and the output video path using the <code>--video_path</code> and <code>--output_path</code> arguments.</p>

        <h2>Contributing</h2>
        <p>Feel free to submit issues or pull requests if you have suggestions for improving this project.</p>

        <h2>License</h2>
        <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.</p>
    </div>
</body>
</html>
