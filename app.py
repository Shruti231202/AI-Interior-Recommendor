from flask import Flask, request, jsonify, render_template
import os 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enables cross-origin communication

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.get_json(force=True)
        print("Received data:", data)

        room_type = data.get("room_type", "").lower()
        color_preference = data.get("color_preference", "").lower()
        belief = data.get("belief", "").lower()

        if not (room_type and color_preference and belief):
            return jsonify({"recommendation": "⚠️ Please fill in all fields before submitting."})

        recs = {
            "living room": f"Use {color_preference} tones with cozy sofas, warm lighting, and plants. Following {belief} layout brings harmony.",
            "bedroom": f"Opt for {color_preference} shades to create a relaxing environment. {belief.capitalize()} alignment improves rest.",
            "kitchen": f"Try {color_preference} hues for freshness and creativity. A {belief} setup supports prosperity.",
            "office": f"Choose {color_preference} colors to boost focus. Facing {belief} enhances productivity.",
            "pooja room": f"Use {color_preference} tones with ample light. {belief.capitalize()} direction fosters peace."
        }

        recommendation = recs.get(room_type, "No recommendation found for this room type.")
        return jsonify({"recommendation": recommendation})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"recommendation": "Server error occurred."}), 500

if __name__ == '__main__':
    from os import environ
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)),debug=True)

