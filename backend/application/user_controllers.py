from flask import Blueprint, jsonify, request,Flask, send_from_directory, render_template,redirect
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity,unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from application.models import User,User_issue,DisasterAnalysis,Admin,Blog,Reviews
from application.database import db
from datetime import timedelta,datetime
from flask import current_app as app,Flask
from flask_caching import Cache

from fpdf import FPDF
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import smtplib
# above things are imports 


app=Flask(__name__)
user_blueprint=Blueprint("user",__name__)

import os
from flask_swagger_ui import get_swaggerui_blueprint  # Import Swagger UI blueprint

SWAGGER_URL = '/api/user/docs'  # Unique URL for user docs
API_URL = '/api/user_api.yaml'

swagger_user_ui_blueprint = get_swaggerui_blueprint(
    '/api/user/docs',  # SWAGGER_URL
    '/api/user_api.yaml',  # API_URL
    config={
        'app_name': "User API Documentation by Anirudh",
        'title': "User API Documentation by Anirudh",
        'swagger_ui_config': {
            'docExpansion': 'none',
            'displayRequestDuration': True,
            'operationsSorter': 'alpha',
            'defaultModelsExpandDepth': -1,
            'defaultModelExpandDepth': 3
        }
    },
    blueprint_name='swagger_user'
)

@user_blueprint.route('/user_api.yaml')
def user_serve_admin_swagger():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    response = send_from_directory(current_dir, 'user_api.yaml')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response



cache=Cache(app)
@user_blueprint.route("/",methods=['GET','POST'])
def hello():
    return jsonify({
        'msg':'Hello You are connected from Backend!'
    })
    
# initialization stuff
    
#user_register
@user_blueprint.route("/user_register",methods=['GET','POST'])
def user_register():
    if request.method=="POST":
        data=request.get_json()
        email=data.get("email")
        password=data.get("password")
        name=data.get("name")
        
        hashed_password=generate_password_hash(password,method='pbkdf2:sha256',salt_length=8)
        
        u=db.session.execute(db.select(User).where(User.user_email==email)).scalar()
        # print(u.user_email)
        
        if u is None:
            # means a new user
            
            new_user=User(user_email=email,
                          password=hashed_password,
                          user_name=name,
                          )
            db.session.add(new_user)
            db.session.commit()
            
            return jsonify({
                'msg':'Registered Successful!'
            }),200
        
        else:
            return jsonify({
                'msg':'Oops! You are already registered go to login page!'
            }),201
        
        
#user_login
@user_blueprint.route("/user_login",methods=['GET','POST'])
def user_login():
    if request.method=="POST":
        data=request.get_json()
        email=data.get("email")
        password=data.get("password")
        
        u=db.session.execute(db.select(User).where(User.user_email==email)).scalar()
        if u is None:
            return jsonify({
                'message':'Incorrect Credentials User Does\'nt exist with this email id', 
            }),201
        
        if not check_password_hash(u.password,password):
            return jsonify({
                'message':'Wrong Password!', 
            }),202
        
        access_token=create_access_token(identity=u.user_id,expires_delta=timedelta(days=1))
        info={
            'id':u.user_id,
            'email':u.user_email,
            'name':u.user_name,
            'role':'user',
            'status':u.is_privileged
        }
        
        return jsonify({
            'access_token':access_token,
            'info':info,
        }),200
        
#user_logout      
@user_blueprint.route("/user_logout",methods=['GET','POST'])
@jwt_required()

def user_logout():
    if request.method=="POST":
        response=jsonify({
            'message':'Logged out Successfully'
        })
        
        unset_jwt_cookies(response)
        return response,200
    
#user_check_permission
@user_blueprint.route("/user_check_permission",methods=['GET','POST'])
@jwt_required()

def is_permitted():
    user_identity=get_jwt_identity()
    user=User.query.get(user_identity)
    
    if user:
        response= jsonify({
            'msg':'Access Granted'
        })
        unset_jwt_cookies(response)
        return response,200
    
    else:
        response= jsonify({
            'msg':'Access Denied'
        })
        unset_jwt_cookies(response)
        return response,201
    

#request the user
@user_blueprint.route("/send_request/<int:id>",methods=['GET','POST'])
def send_request(id):
    # check whether is this user eligible to take a book
    data=request.get_json()
    name=data.get("name")
    email=data.get("email")
    
    status=db.session.execute(db.select(User_issue).where(User_issue.user_id==id)).scalar()
    print(status)
    if status==None:
        is_eligible=True
        user=db.session.execute(db.select(User).where(User.user_id==id)).scalar()
        
       
            
        if is_eligible:
            request_date=datetime.today()
            new_instruction=User_issue(user_id=id,request_date=request_date)
            db.session.add(new_instruction)
            db.session.commit()
            
            return jsonify({
                'msg':'Request registered Successfully!'
            }),200
        
        else:
            return jsonify({
                'msg':'Max requests Sent!'
            }),202
            
    elif status.request_date==None and status.doi==None:
            status.request_date=datetime.today()  
            status.return_date=None
            db.session.commit()
            return jsonify({
                'msg':'Request registered Successfully!'
            }),200
            
    else:
        return jsonify({
            'msg':'You have Already Requested Please Wait!'
        }),201
        
@user_blueprint.route("/getUserInfo/<int:id>",methods=['GET','POST'])
def getUserInfo(id):
    user=db.session.execute(db.select(User).where(User.user_id==id)).scalar()
    
    user_i=db.session.execute(db.select(User_issue).where(User_issue.user_id==id)).scalar()
    user_info={
        'user_id':user.user_id,
        'user_name':user.user_name,
        'user_email':user.user_email,
        'is_privileged':user.is_privileged,
        'due_date':user_i.due_date,
        'doi':user_i.doi
    }
    
    print(user_info)
    
    return jsonify({
        'user_info':user_info
    }),200
    

@user_blueprint.route("/return_Status/<int:id>",methods=['GET','POST'])
def return_status(id):
    user=db.session.execute(db.select(User_issue).where(User_issue.user_id==id)).scalar()
    
    user.return_date=datetime.now()
    user.doi=None
    user.due_date=None
    user.status="Returned Privileged Status on his own before Due_date"
    
    db.session.commit()
    
    u=db.session.execute(db.Select(User).where(User.user_id==id)).scalar()
    u.is_privileged=0
    db.session.commit()
    
    return jsonify({
        'msg':'Sucess'
    }),200
    
    
def send_email(user_email, subject, body, pdf_path):
    sender_email = "anirudhpabbaraju1103@gmail.com"
    password = "atnipcvnvvxvcghn"  # Replace with your actual app password
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = user_email
    msg['Subject'] = subject
    
    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF file
    if pdf_path and os.path.exists(pdf_path):
        with open(pdf_path, "rb") as pdf_file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(pdf_file.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(pdf_path)}",
            )
            msg.attach(part)

    # Send the email using SMTP
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, user_email, msg.as_string())
            print(f"Email with PDF sent to {user_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

def send_activity_report(email):
    # Step 1: Fetch data from DisasterAnalysis table
    disaster_data = DisasterAnalysis.query.all()
    disaster_records = [record.to_dict() for record in disaster_data]
    
    # Step 2: Generate PDF
    pdf_path = generate_pdf(disaster_records)
    
    # Step 3: Send the PDF via email
    recipient_email = email # Replace with actual recipient email
    subject = "Disaster Analysis Report"
    body = "Please find attached the latest disaster analysis report."
    
    send_email(recipient_email, subject, body, pdf_path)
    
    # Optional: Clean up the generated PDF
    os.remove(pdf_path)

def generate_pdf(disaster_records):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Disaster Analysis Report", 0, 1, "C")
    pdf.set_font("Arial", "", 10)
    
    pdf.ln(10)
    for record in disaster_records:
        pdf.cell(0, 10, f"Disaster Name: {record['disaster_name']}", 0, 1)
        pdf.cell(0, 10, f"Date and Time: {record['time']}", 0, 1)
        pdf.cell(0, 10, f"Location: {record['location']}", 0, 1)
        pdf.cell(0, 10, f"Success Rate: {record['success_rate']}%", 0, 1)
        pdf.cell(0, 10, f"Total Disasters: {record['total']}", 0, 1)
        pdf.ln(5)  # Space between records
    
    # Save the PDF to a file
    pdf_path = "C:\\MY_PROJECTS\\MY_PROJECTS\\DMP\\backend\\application\\disaster_report.pdf"  # Specify the path to save the file
    pdf.output(pdf_path)
    
    return pdf_path
    
    

        
        
@user_blueprint.route("/generate_user_report/<int:id>",methods=['GET','POST'])
def generate_user_report(id):
   
        # Trigger the Celery task
        
    user=db.session.execute(db.Select(User).where(User.user_id==id)).scalar()
        
    job=send_activity_report(user.user_email)
    
    
    
    # Return the task ID to the client
    return jsonify({
        'status': 'Done',
    }), 200
    
#Change_password
@user_blueprint.route("/change_password",methods=['GET','POST'])
def change_password():
    data=request.get_json()
    email=data.get("email")
    id=data.get("id")
    role=data.get("role")
    print(id)
    password=data.get("new_password")
    old_password=data.get("old_password")
    if role=="user":
        u=db.session.execute(db.Select(User).where(User.user_id==id)).scalar()
    else:
        u=db.session.execute(db.select(Admin).where(Admin.admin_id==id)).scalar()
    if check_password_hash(u.password,old_password):
        u.password=generate_password_hash(password,method='pbkdf2:sha256',salt_length=8)
        u.email=email
        db.session.commit()
        
        return jsonify({
            'msg':'Password changed! Successful!'
        }),200
        
    else:
        return jsonify({
            'msg':'Password not same'
        }),201
        
@user_blueprint.route("/change_password2",methods=['GET','POST'])
def change_password2():
    data=request.get_json()
    email=data.get("email")
    id=data.get("id")
    role=data.get("role")
    print(id)
    password=data.get("new_password")
    if role=="user":
        u=db.session.execute(db.Select(User).where(User.user_id==id)).scalar()
    else:
        u=db.session.execute(db.select(Admin).where(Admin.admin_id==id)).scalar()
        u.password=generate_password_hash(password,method='pbkdf2:sha256',salt_length=8)
        u.email=email
        db.session.commit()
        
    return jsonify({
        'msg':'Password changed! Successful!'
    }),200
        
    
        
    
        
        
@user_blueprint.route("/getAllUserDetails",methods=['GET','POST'])
def getAllUserDetails():
    user_list=[]
    u=db.session.execute(db.select(User)).scalars().all()
    for x in u:
        bi=db.session.execute(db.select(Blog).where(Blog.user_id==x.user_id)).scalars().all()
        bi_count=len(bi)
        re=db.session.execute(db.select(Reviews).where(Reviews.user_id==x.user_id)).scalars().all()
        re_count=len(re)
        
        user_list.append({
            'user_id':x.user_id,
            'name':x.user_name,
            'email':x.user_email,
            'blog_count':bi_count,
            'review_count':re_count        
        })    
        
    
    return jsonify({
        'user_list':user_list
    }),200
    
import random

def send_email1(email,random_number):
    sender_email = "anirudhpabbaraju1103@gmail.com"
    password = "atnipcvnvvxvcghn"
    subject = "OTP for changing password!"
    
    # Build the email body
    body = f"""
    OTP: {random_number}
    """
    
    # Add latitude and longitude if available


    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email  # Assuming you're sending this alert to the user who triggered it
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Sending email using SMTP
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, email, text)
            print(f"Email sent to {email}")
    except Exception as e:
        print(f"Error sending email: {e}")  
    
@user_blueprint.route("/sendOtp/<string:email>",methods=['GET','POST'])
def sendOtp(email):
    random_number = random.randint(1000, 9999)
    send_email1(email,random_number)
    
    return jsonify({
        'original_otp':random_number
    }),200

    