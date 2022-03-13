#imports
from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import current_user, login_required
from app import db
from app.models import Post
from app.main.forms import UpdatePost,PostForm
from app.auth.utils import save_picture
import urllib.request,json



#Main blueprint intialization
main = Blueprint('main', __name__)



#Home default route
@main.route('/',methods=['GET','POST'])
@main.route('/home',methods=['GET','POST'])
def home():
    
    
    #URL for random quotes displayed in the app
    url = 'http://quotes.stormconsultancy.co.uk/random.json'
    
    #First request
    response1 = urllib.request.urlopen(url)
    data1 = response1.read()
    dict1 = json.loads(data1)
    
    #Second request
    response2 = urllib.request.urlopen(url)
    data2 = response2.read()
    dict2 = json.loads(data2)
    
    #Third Request
    response3 = urllib.request.urlopen(url)
    data3 = response3.read()
    dict3 = json.loads(data3)
    
    #Fourth Request
    response4 = urllib.request.urlopen(url)
    data4 = response4.read()
    dict4 = json.loads(data4)
    
    #Fiveth Request
    response5 = urllib.request.urlopen(url)
    data5 = response5.read()
    dict5 = json.loads(data5)
    
    #Sixth Request
    response6 = urllib.request.urlopen(url)
    data6 = response6.read()
    dict6 = json.loads(data6)
    
    posts=Post.query.all()
    return render_template('index.html', quote1=dict1, quote2=dict2, quote3=dict3,quote4=dict4,quote5=dict5,quote6=dict6,posts=posts)


@main.route('/create', methods=['GET','POST'])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        picture_file = save_picture(form.picture.data)
        post = Post(title=form.title.data,content=form.content.data,image_file=picture_file,user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash("Post Created successfully")
        return redirect(url_for('main.home'))
    return render_template('create.html', form=form)




#Individual Post Route
@main.route('/post/<int:post_id>', methods=['GET','POST'])
def post(post_id):
    form = UpdatePost()
    post = Post.query.get(post_id)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Post updated successfully")
        return redirect(url_for('main.post',post_id=post.id))
    form.title.data = post.title
    form.content.data = post.content
    return render_template('post.html', post=post, form=form)


#Route to Delete a Post
@main.route('/post/delete/<int:post_id>')
@login_required
def delete(post_id):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    post_to_delete = Post.query.get(post_id)
    id = current_user.id
    if id == post_to_delete.users.id:
        try:
            db.session.delete(post_to_delete)
            db.session.commit()
            flash("Post deleted successfully")
            return redirect(url_for('main.home'))
        except :
            return redirect(url_for('main.post'))
    else:
        return redirect(url_for('main.home'))
    