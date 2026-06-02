from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "name": "Maksym Havrysh",
        "role": "Video Editor / Motion Designer",
        "bio": "Video Editor/Motion Designer with 3-4 years of experience. I craft high-retention video content that drives sales. Former lead editor for a major media group.",
        "linkedin": "https://www.linkedin.com/", # Вставь свою ссылку на линкедин
        "advantages": [
            {
                "title": "3-4 Years of Experience", 
                "desc": "Specialized in professional video editing and dynamic motion design."
            },
            {
                "title": "Social Media Expertise", 
                "desc": "3 years of managing social channels, knowing exactly what hooks the audience."
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)