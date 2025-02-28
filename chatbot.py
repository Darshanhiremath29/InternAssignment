from flask import Flask, request, jsonify
from scraper import scrape_docs

app = Flask(__name__)

# List of supported CDP documentation links
CDP_DOCS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

@app.route('/ask', methods=['POST'])
def answer_question():
    """
    API endpoint to receive user questions and return relevant answers.
    """
    data = request.json
    question = data.get("question", "").lower()
    
    for platform, url in CDP_DOCS.items():
        if platform in question:
            answer = scrape_docs(url)
            return jsonify({"platform": platform, "answer": answer[:1000]})  # Limit response length

    return jsonify({"error": "Platform not recognized. Ask about Segment, mParticle, Lytics, or Zeotap."})

if __name__ == '__main__':
    app.run(debug=True)
