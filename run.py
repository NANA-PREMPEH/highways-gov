from trial import create_app, db
from trial.models import User, EmployeeDetails, Role, Permission
 
app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, EmployeeDetails=EmployeeDetails, Role=Role, Permission=Permission)


if __name__ == "__main__": 
    app.run(debug=True) 