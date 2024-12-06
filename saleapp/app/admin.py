from app.models import Category , Product, User, UserRole
from app import  app, db
from flask_admin import  Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import  current_user, logout_user
from flask import  redirect

admin = Admin(app=app,name="EADMIN855", template_mode='bootstrap4')
class CategoryView(ModelView):
    column_list = ['id','products']
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)
class ProductView(ModelView):
    can_export = True
    column_list = ['id','name','price','active']
    column_searchable_list = ['name']
    column_filters = ['id','price']
    page_size = 8
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)
class UserView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role.__eq__(UserRole.ADMIN)

class LogOutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')
    def is_accessible(self):
        return current_user.is_authenticated
class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

    def is_accessible(self):
        return current_user.is_authenticated
admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(UserView(User, db.session))
admin.add_view(LogOutView("LogOut"))
admin.add_view(StatsView("Thong Ke"))