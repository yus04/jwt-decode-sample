from flask import Flask, request, jsonify
from flask_jwt_extended import decode_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-256-bit-secret'

@app.route('/api/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization').split()[1]
    decoded_token = decode_token(token)
    user_claims = decoded_token.get('claims')
    
    if user_claims.get('userType') == 'internal':
        return jsonify(message="Welcome internal user!")
    else:
        return jsonify(message="Access denied."), 403

if __name__ == '__main__':
    app.run()
