from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    data = {
        "name": "Maksym Havrysh",
        "role": "Video Editor / Motion Designer",
        "bio": "Video Editor/Motion Designer with 3-4 years of experience. I craft high-retention video content that drives sales. Former lead editor for a major media group.",
        "advantages": [
            {
                "title": "3-4 Years of Experience",
                "desc": "Specialized in professional video editing and dynamic motion design."
            },
            {
                "title": "Social Media Expertise",
                "desc": "3 years of managing social channels, knowing exactly what hooks the audience."
            },
            {
                "title": "Proven Sales Impact",
                "desc": "Lead editor for a major media group: my videos generated massive sales during the product launch."
            },
            {
                "title": "Maximum Retention",
                "desc": "Ad integrations consistently achieve near-100% watch time due to professional pacing."
            }
        ],
        "portfolio": [
            {
                "title": "Commercial Video Reel",
                "platform": "YouTube",
                "url": "https://www.tiktok.com/@aimstarshq/video/7621939553061965089" # Твоя ссылка
            },
            {
                "title": "TikTok Viral Trend Edit",
                "platform": "TikTok",
                "url": "https://youtu.be/RlireGjAfiA" # Ссылка на любой ТикТок
            },
            {
                "title": "Motion Graphics Showreel",
                "platform": "Vimeo",
                "url": "https://www.tiktok.com/@nawyfps/video/7632614572423253281" # Твоя ссылка
            }
        ]
    }
    return render_template('index.html', data=data)
