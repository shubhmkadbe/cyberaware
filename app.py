from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory leaderboard to store the user data
leaderboard = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_flag', methods=['POST'])
def submit_flag():
    # Extract data from the request
    data = request.json
    user_flag = data.get('flag')
    username = data.get('username')
    completion_time = data.get('completionTime')

    # Check if the flag is correct
    if user_flag == 'FLAG{CYBER_AWARE}':
        # Add the user to the leaderboard with their score and time
        leaderboard.append({
            'username': username,
            'score': 100,  # Fixed score for a correct flag
            'completionTime': completion_time
        })
        # Sort leaderboard by score (descending) and then by time (ascending)
        leaderboard.sort(key=lambda x: (-x['score'], x['completionTime']))
        return jsonify({'message': 'Congratulations! You successfully completed the challenge!', 'success': True})
    else:
        return jsonify({'message': 'Incorrect flag. Please try again.', 'success': False})

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    # Return the leaderboard data as a JSON response
    return jsonify(leaderboard)

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)
