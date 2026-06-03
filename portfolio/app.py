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
                "title": " Product review/showcase",
                "platform": "Tik tok",
                "url": "https://www.tiktok.com/@nawyfps/video/7632614572423253281" # Твоя ссылка
            },
            {
                "title": "Silo Demo Showcase",
                "platform": "YouTube",
                "url": " https://youtu.be/rIqoK-alAXM" # Ссылка на любой ТикТок
            },
            {
                "title": "Viral YouTube Project",
                "platform": "YouTube",
                "url": " https://youtu.be/8x1Nbj4J3pc?si=nArL0yV75mirbfc7" # Твоя ссылка
            }
        ]
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
