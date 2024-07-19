from flask import Flask, request, jsonify, render_template, redirect, url_for, session, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
import os
import json
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'
CHAT_DIRECTORY = 'chats'
USERS_FILE = 'users.json'
PROFILE_PIC_DIRECTORY = 'profile_pics'

# Create directories for saving chats and profile pictures if they don't exist
if not os.path.exists(CHAT_DIRECTORY):
    os.makedirs(CHAT_DIRECTORY)

if not os.path.exists(PROFILE_PIC_DIRECTORY):
    os.makedirs(PROFILE_PIC_DIRECTORY)

# Load users from file
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save users to file
def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file)

@app.route('/')
def index():
    if 'username' in session:
        users = load_users()
        username = session['username']
        user_data = users.get(username, {})
        profile_pic = user_data.get('profile_pic', 'default.png')
        return render_template('index.html', username=username, profile_pic=profile_pic)
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users:
            return 'Username already exists', 400
        users[username] = {
            'password': generate_password_hash(password),
            'chats': [],
            'profile_pic': 'default.png'
        }
        save_users(users)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            session['last_login'] = str(datetime.datetime.now())
            return redirect(url_for('index'))
        return 'Invalid credentials', 400
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    users = load_users()
    username = session['username']
    user_data = users.get(username, {})
    
    if request.method == 'POST':
        new_username = request.form.get('new_username')
        new_password = request.form.get('new_password')
        
        if new_username:
            users[new_username] = users.pop(username)
            session['username'] = new_username
            username = new_username
        
        if new_password:
            users[username]['password'] = generate_password_hash(new_password)
        
        if 'profile_pic' in request.files:
            profile_pic = request.files['profile_pic']
            profile_pic_filename = f"{username}.png"
            profile_pic.save(os.path.join(PROFILE_PIC_DIRECTORY, profile_pic_filename))
            users[username]['profile_pic'] = profile_pic_filename
        
        save_users(users)
    
    chats = [{'id': chat_id, 'name': chat['name']} for chat_id, chat in enumerate(user_data.get('chats', []))]
    profile_pic = user_data.get('profile_pic', 'default.png')
    return render_template('dashboard.html', name=username, chats=chats, profile_pic=profile_pic)

@app.route('/delete_chat/<int:chat_id>', methods=['DELETE'])
def delete_chat(chat_id):
    if 'username' not in session:
        return 'Unauthorized', 401
    users = load_users()
    username = session['username']
    if chat_id < len(users[username]['chats']):
        users[username]['chats'].pop(chat_id)
        save_users(users)
        return '', 204
    return 'Chat not found', 404

@app.route('/save_chat', methods=['POST'])
def save_chat():
    if 'username' not in session:
        return 'Unauthorized', 401
    data = request.json
    chat_name = data.get('chat_name')
    content = data.get('content')
    
    if not chat_name or not content:
        return jsonify({'error': 'Invalid request'}), 400

    users = load_users()
    username = session['username']
    chat_index = next((index for (index, d) in enumerate(users[username]['chats']) if d["name"] == chat_name), None)
    if chat_index is not None:
        users[username]['chats'][chat_index]['content'] = content
    else:
        users[username]['chats'].append({'name': chat_name, 'content': content})
    save_users(users)
    return jsonify({'status': 'Chat saved successfully'}), 200

@app.route('/load_chat/<chat_name>', methods=['GET'])
def load_chat(chat_name):
    if 'username' not in session:
        return 'Unauthorized', 401
    users = load_users()
    username = session['username']
    for chat in users[username]['chats']:
        if chat['name'] == chat_name:
            return jsonify({'content': chat['content']}), 200
    return jsonify({'error': 'Chat not found'}), 404

@app.route('/profile_pic/<username>')
def profile_pic(username):
    users = load_users()
    profile_pic = users.get(username, {}).get('profile_pic', 'default.png')
    return send_from_directory(PROFILE_PIC_DIRECTORY, profile_pic)

if __name__ == '__main__':
    app.run(debug=True)
