# app.py
from flask import Flask, jsonify, request, render_template
from green_space_calculate import calculate_green_space_ratio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/green-space-ratio', methods=['GET', 'POST'])
def get_green_space_ratio():
    area_name = request.args.get('area_name')  # Get area_name from query parameters
    try:
        green_space_ratio = calculate_green_space_ratio(area_name)
        return jsonify({"green_space_ratio":(green_space_ratio*100)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=6007)



