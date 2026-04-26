from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/JournalingApp')
@app.route('/JournalingApp/')
def journal_app():
    return render_template('journal_app_index.html')


@app.route('/JournalingApp/privacy')
def journal_privacy():
    return render_template('journal_app_privacy.html')


@app.route('/JournalingApp/terms')
def journal_terms():
    return render_template('journal_app_terms.html')


@app.route('/health')
def health():
    return {'status': 'healthy'}, 200


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
