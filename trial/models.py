from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from trial import db, login_manager
from trial.search import add_to_index, remove_from_index, query_index
from slugify import slugify 



class SearchableMixin(object):
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0: 
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id)), total

    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)


db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)




#Function to reload user from user id stored in session
#Decorate the function so that the extension can easily know  
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#Create User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    ref_no = db.Column(db.String(120), nullable=False)
    acc_gen_no = db.Column(db.String(120), nullable=False)
    ssf_no = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    sex = db.Column(db.String(120), nullable=False)
    job_pos = db.Column(db.String(120), nullable=False)
    date_engaged = db.Column(db.Date, nullable=False)
    pres_appt = db.Column(db.Date, nullable=False)
    station = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(100), nullable=False, default='staff@gmail.com')
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='default.jpg')
    posts = db.relationship('Leave', backref='author', lazy=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['ADMIN_HIGHWAYS']:
                self.role = Role.query.filter_by(name='Administrator').first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def is_administrator(self):
        return self.can(Permission.ADMIN)


    #Create methods that make it easy to create tokens
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        #Return a token created by the dumps
        return s.dumps({'user_id': self.id}).decode('utf-8')

    #Create a method that verifies a token
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        #Check for expired token using a try-catch(exception) block
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.image_file}')"


class AnonymousUser(AnonymousUserMixin):

    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser

#Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic') 

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        return self.permissions & perm == perm

    @staticmethod
    def insert_roles():
        roles = {
            'User' : [Permission.WRITE],
            'Moderator' : [Permission.WRITE, Permission.MODERATE],
            'Administrator' : [Permission.WRITE, Permission.MODERATE, Permission.ADMIN],
        }

        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name 


class Permission:
    WRITE = 1
    MODERATE = 2
    ADMIN = 4
 


#Create User Model
class Staff(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    ref_no = db.Column(db.String(120), nullable=False)
    acc_gen_no = db.Column(db.String(120), nullable=False)
    ssf_no = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    sex = db.Column(db.String(120), nullable=False)
    job_pos = db.Column(db.String(120), nullable=False)
    date_engaged = db.Column(db.Date, nullable=False)
    pres_appt = db.Column(db.Date, nullable=False)
    station = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(100), nullable=False, default='staff@gmail.com')
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.image_file}')"


#Create a Blog Post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180), nullable=False)
    slug = db.Column(db.String(180), nullable=False)
    body = db.Column(db.Text, nullable=False)
    comments = db.Column(db.Integer, default=0)
    views = db.Column(db.Integer, default=0)
    image = db.Column(db.String(120), default='image.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref=db.backref('author', lazy=True))
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
 
    def __repr__(self):
        return f"Post('{self.title}', '{self.body}', '{self.image}')"

    #Create a static method
    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)

db.event.listen(Post.title, 'set', Post.generate_slug, retval=False)

#Create Comment Form Model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False) 
    post = db.relationship('Post', backref=db.backref('post', lazy=True))
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=False)
    

    def __repr__(self):
        return f"Comment('{self.name}')"



#Create Leave Form Model
class Leave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    rank = db.Column(db.String(40), nullable=False)
    section = db.Column(db.String(40), nullable=False) 
    date_app = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    tele_no = db.Column(db.Integer, nullable=False)
    leave_cat = db.Column(db.String(30), nullable=False)
    no_of_days = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    supp_info = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text, nullable=False)
    mobile_no = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    days_proceed = db.Column(db.Integer, nullable=False)
    effec_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    resump_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    outs_days = db.Column(db.Integer, nullable=False)
    leave_status = db.Column(db.String(20), index = True, unique = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Leave('{self.name}', '{self.rank}', '{self.section}', '{self.date_app}', '{self.tele_no}', \
            '{self.leave_cat}','{self.no_of_days}','{self.start_date}','{self.end_date}','{self.supp_info}', \
            '{self.address}', '{self.mobile_no}', '{self.email}', '{self.days_proceed}', '{self.effec_date}', \
            '{self.resump_date}', '{self.outs_days}')"



#Create Upgrading Table
class Upgrading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)

    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Upgrading('{self.id}','{self.video_title}','{self.video_link}')"


#Create Regravelling Table
class Regravelling(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)

    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f"Regravelling('{self.id}','{self.video_title}','{self.video_link}')"

#Create Construction Table
class Construction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.Text, nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)

    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Construction('{self.id}','{self.video_title}','{self.video_link}')"


#Create Rehabilitation Table
class Rehabilitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)

    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Rehabilitation('{self.id}','{self.video_title}','{self.video_link}')"

#Create Partialreconstruction Table
class Partialreconstruction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='n/a') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)

    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Partialreconstruction('{self.id}','{self.video_title}','{self.video_link}')"

#Create Supply Table
class Supply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)

    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Supply('{self.id}','{self.video_title}','{self.video_link}')"

#Create Decongestion Table
class Decongestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)

    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Decongestion('{self.id}','{self.video_title}','{self.video_link}')"

#Create Resealing Table
class Resealing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)

    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Resealing('{self.id}','{self.video_title}','{self.video_link}')"

#Create Preconstruction Table
class Preconstruction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)

    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Preconstruction('{self.id}','{self.video_title}','{self.video_link}')"

#Create Resurfacing Table
class Resurfacing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)
    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Resurfacing('{self.id}','{self.video_title}','{self.video_link}')"

#Create Repairs Table
class Repairs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)

    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Repairs('{self.id}','{self.video_title}','{self.video_link}')"

#Create Asphalticoverlay Table
class Asphalticoverlay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)

    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Asphalticoverlay('{self.id}','{self.video_title}','{self.video_link}')"


class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(120), nullable=True)
    project = db.Column(db.String(120), nullable=True)
    length = db.Column(db.String(50), nullable=True, default='N/A') 
    contractor = db.Column(db.String(120), nullable=True, default='N/A')
    date_commenced = db.Column(db.Date, nullable=True, default=None)
    date_completed = db.Column(db.Date, nullable=True, default=None)
    contract_sum = db.Column(db.String(50), nullable=True, default='N/A')
    amt_to_date = db.Column(db.String(50), nullable=True, default='N/A')
    video_title = db.Column(db.String(300), nullable=True, default='N/A')
    video_link = db.Column(db.String(250), nullable=True, default='N/A')
    video_description = db.Column(db.Text, nullable=True, default='N/A')
    video_thumb = db.Column(db.String(50), default='default.png')
    uploaded_time = db.Column(db.DateTime, default=datetime.now)

    # this is the column with which we are creating the relation with user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Contract('{self.id}','{self.video_title}','{self.video_link}')" 
    
class Roadcondition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg = db.Column(db.String(50), nullable=True)
    road_no = db.Column(db.String(50), nullable=True)
    road_name = db.Column(db.String(50), nullable=True, default='N/A')
    link_ref = db.Column(db.String(50), nullable=True, default='N/A')
    sect_ref = db.Column(db.String(50), nullable=True, default='N/A') 
    fr_om = db.Column(db.String(50), nullable=True, default='N/A')
    t_o = db.Column(db.String(50), nullable=True, default='N/A')
    start = db.Column(db.String(50), nullable=True, default='N/A')
    end = db.Column(db.String(50), nullable=True, default='N/A')
    length = db.Column(db.String(50), nullable=True, default='N/A')
    width = db.Column(db.String(50), nullable=True, default='N/A')
    surf_type = db.Column(db.String(50), nullable=True, default='N/A')
    cond_score = db.Column(db.String(50), nullable=True, default='N/A')
    iri = db.Column(db.String(50), nullable=True, default='N/A')
    cond = db.Column(db.String(50), nullable=True, default='N/A')

    def __repr__(self):
        return f"Roadcondition('{self.id}','{self.reg}','{self.road_no}')" 


class Roadcondition2K19(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg = db.Column(db.String(50), nullable=True)
    road_no = db.Column(db.String(50), nullable=True)
    road_name = db.Column(db.String(50), nullable=True, default='N/A')
    link_ref = db.Column(db.String(50), nullable=True, default='N/A')
    sect_ref = db.Column(db.String(50), nullable=True, default='N/A') 
    fr_om = db.Column(db.String(50), nullable=True, default='N/A')
    t_o = db.Column(db.String(50), nullable=True, default='N/A')
    start = db.Column(db.String(50), nullable=True, default='N/A')
    length = db.Column(db.String(50), nullable=True, default='N/A')
    width = db.Column(db.String(50), nullable=True, default='N/A')
    surf_type = db.Column(db.String(50), nullable=True, default='N/A')
    cond_score = db.Column(db.String(50), nullable=True, default='N/A')
    iri = db.Column(db.String(50), nullable=True, default='N/A')
    cond = db.Column(db.String(50), nullable=True, default='N/A')

    def __repr__(self):
        return f"Roadcondition2K19('{self.id}','{self.reg}','{self.road_no}')"  

