from flask import Flask, request, jsonify
from model import translate

app = Flask(__name__)

@app.route("/translate", methods=["POST"])
def translate_sentence():
    data = request.json
    sentence = data.get("sentence")
    target_lang = data.get("target_lang")
    source_lang = data.get("source_lang")

    result = translate(sentence=sentence, tgt_lang=target_lang, src_lang=source_lang)

    new_obj = {
        "translate_result": result,
    }

    return jsonify(new_obj), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)