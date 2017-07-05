from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>/')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__':
    show_user_profile("BY")
    show_post(8888)
    app.run(debug=True)