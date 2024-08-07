from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    languages = request.args.getlist('languages')

    if not video_id:
        return jsonify({"error": "Video ID is required"}), 400

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        return jsonify(transcript)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
