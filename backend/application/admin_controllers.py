from flask import Blueprint, jsonify, request, Flask, send_from_directory, render_template,redirect
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from application.models import Admin, User, User_issue, DisasterAnalysis
from application.database import db
from datetime import timedelta, datetime
from fpdf import FPDF
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from flask_swagger_ui import get_swaggerui_blueprint  # Import Swagger UI blueprint

lib_blueprint = Blueprint("lib", __name__)

SWAGGER_URL = '/api/admin/docs'
API_URL = '/api/admin_api.yaml'

swagger_admin_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Admin API Documentation by Anirudh",
        'title': "Admin API Documentation by Anirudh",
        'swagger_ui_config': {
            'docExpansion': 'none',
            'displayRequestDuration': True,
            'operationsSorter': 'alpha',
            'defaultModelsExpandDepth': -1,
            'defaultModelExpandDepth': 3
        }
    },
    blueprint_name='swagger_admin'
)
# Add cache control headers to the YAML route
@lib_blueprint.route('/admin_api.yaml')
def admin_serve_admin_swagger():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    response = send_from_directory(current_dir, 'admin_api.yaml')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@lib_blueprint.route('/admin_api.yaml')
def serve_admin_swagger():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(current_dir, 'admin_api.yaml')

#admin_login  
@lib_blueprint.route("/admin_login",methods=['GET','POST'])
def admin_login():
    if request.method=="POST":
        data=request.get_json()
        email=data.get("email")
        password=data.get("password")
        
        lib=db.session.execute(db.select(Admin).where(Admin.admin_email==email)).scalar()
        if lib is None:
            return jsonify({
                'message':'Incorrect Credentials Admin Does\'nt exist with this email id', 
            }),201
        
        if lib.password!=password:
            return jsonify({
                'message':'Wrong Password!', 
            }),202
        
        access_token=create_access_token(identity=lib.admin_id,expires_delta=timedelta(days=1))
        info={
            'id':lib.admin_id,
            'email':lib.admin_email,
            'role':'admin'
        }
        
        return jsonify({
            'access_token':access_token,
            'info':info,
        }),200
        
        
@lib_blueprint.route("/admin_logout",methods=['GET','POST'])
@jwt_required()
def admin_logout():
    if request.method=="POST":
        response=jsonify({
            'message':'Logged out Successfully'
        })
        
        unset_jwt_cookies(response)
        return response,200
    
@lib_blueprint.route("/lib_check_permission",methods=['GET','POST'])
@jwt_required()

def is_permitted():
    lib_identity=get_jwt_identity()
    lib=Admin.query.get(lib_identity)
    print(lib)
    
    
    if lib:
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
        


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email1(alert_message, user_name, user_email, latitude, longitude,email,disaster_type):
    sender_email = "anirudhpabbaraju1103@gmail.com"
    password = "atnipcvnvvxvcghn"
    subject = "Alert Notification"
    
    # Build the email body
    body = f"""
    Important Alert: {alert_message}
    
    Sent by: {user_name}
    Sender's email : {email}
    Disaster Type : {disaster_type}
    User's Email: {user_email}
    """
    
    # Add latitude and longitude if available
    if latitude and longitude:
        body += f"\nLocation: Latitude: {latitude}, Longitude: {longitude}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = user_email  # Assuming you're sending this alert to the user who triggered it
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Sending email using SMTP
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, user_email, text)
            print(f"Email sent to {user_email}")
    except Exception as e:
        print(f"Error sending email: {e}")  
        
@lib_blueprint.route("/sendAlert/<int:id>",methods=['GET','POST'])
def sendAlert(id):
    data = request.get_json()
    alert_message = data.get('alertMsg')
    name=data.get('name')
    email=data.get('email')
    disaster_type=data.get('dt')

    # Get the user who triggered the alert
    alert_user = User.query.get(id)
    # name=alert_user.user_name

    if not alert_user:
        return jsonify({"error": "User not found."}), 404

    # Get all users in the database
    all_users = User.query.all()

    if not all_users:
        return jsonify({"error": "No users found in the database."}), 404
    
    print(alert_message)

    # Send email to all users in the database
    latitude = "17.9835° N"
    longitude = "79.5308° E"
    for user in all_users:
        if user.user_id!=alert_user.user_id:
            send_email1(alert_message,name,user.user_email,latitude,longitude,email,disaster_type)

    return jsonify({"message": "Alert sent to all users."}), 200
    
@lib_blueprint.route("/getAllRequests",methods=['GET','POST'])
def getRequests():
    user_info=db.session.execute(db.Select(User_issue)).scalars().all()
    if user_info==[]:
        return jsonify({
            'msg':'Currently no info dude!'
        }),201
    else:
        issued_users=[]
        requested_users=[]
        returned_users=[]
        
        for x in user_info:
            b=db.session.execute(db.select(User).where(User.user_id==x.user_id)).scalar()
            if x.doi!=None:
                if datetime.today()<x.due_date:
                    if b!=None:
                        issued_users.append({
                            'user_id':x.user_id,
                            'user_name':b.user_name,
                            'user_email' :b.user_email,
                            'issue_date':x.doi,
                            'due_date':x.due_date
                        })
                    else:
                        issued_users.append({
                            'user_id':x.user_id,
                            'user_name':b.user_name,
                            'user_email' :b.user_email,
                            'issue_date':x.doi,
                            'due_date':x.due_date
                        })
                        
                else:
                    x.issue_date=None
                    x.return_date=datetime.today()
                    db.session.commit()
                
            if x.return_date!=None:
                if b!=None:
                    returned_users.append({
                        'user_id':x.user_id,
                        'user_name':b.user_name,
                        'user_email' :b.user_email,
                        'return_date':x.return_date,
                        'status':x.status,
                        "re_issue":x.re_issue
                    })
                else:
                    returned_users.append({
                        'user_id':x.user_id,
                        'user_name':b.user_name,
                        'user_email' :b.user_email,
                        'return_date':x.return_date,
                        'status':x.status,
                        "re_issue":x.re_issue
                    })
                    
                
            if x.request_date!=None:
                if b!=None:
                    requested_users.append({
                        'user_id':x.user_id,
                        'user_name':b.user_name,
                        'user_email' :b.user_email,
                        'request_date':x.request_date,
                    })
                else:
                    requested_users.append({
                        'user_id':x.user_id,
                        'user_name':b.user_name,
                        'user_email' :b.user_email,
                        'request_date':x.request_date,
                    })
                    
        return jsonify({
            'msg':'All updates Successfull!',
            'issued_users':issued_users,
            'requested_users':requested_users,
            'returned_users':returned_users
        }),200
        
    
@lib_blueprint.route("/grantUser",methods=['GET','POST'])
def grantUser():
    data=request.get_json()
    user_id=data.get("user_id")
    
    status=db.session.execute(db.select(User_issue).where(User_issue.user_id==user_id)).scalar()
    
    if status.request_date!=None:
        status.doi=datetime.today()
        user=db.session.execute(db.select(User).where(User.user_id==user_id)).scalar()
        user.is_privileged=1
        status.due_date=status.doi+timedelta(days=15)
        
        status.request_date=None
        db.session.commit()
        
        return jsonify({
            'msg':'Successfully!',
        }),200
    else:
        return jsonify({
            'msg':'Some Error'
        }),201

@lib_blueprint.route("/rejectUser",methods=['GET','POST'])
def rejectUser():
    data=request.get_json()
    user_id=data.get("user_id")
    
    status=db.session.execute(db.select(User_issue).where(User_issue.user_id==user_id)).scalar()
    
    if status!=None:
        db.session.delete(status)
        db.session.commit()
        
        user=db.session.execute(db.Select(User).where(User.user_id==user_id)).scalar()
        user.is_privileged=0
        
        db.session.commit()
        
        return jsonify({
            'msg':'reject Successfully done!',
        }),200
    else:
        return jsonify({
            'msg':'Some Error'
        }),201
        
        
@lib_blueprint.route("/revokeUser",methods=['GET','POST'])
def revokeUser():
    data=request.get_json()
    user_id=data.get("user_id")
    days_left=data.get("days_left")
    
    status=db.session.execute(db.select(User_issue).where(User_issue.user_id==user_id)).scalar()
    
    if status==None:
        return jsonify({
            'msg':'Some Error!'
        }),201
        
    else:
        status.return_date=datetime.today()
        status.doi=None
        status.status=f"Revoked By librarian before {days_left} days!"
        status.due_date=None
        
        user=db.session.execute(db.Select(User).where(User.user_id==user_id)).scalar()
        user.is_privileged=1
        
        db.session.commit()
        
        return jsonify({
            'msg':'Success!'
        }),200
        

@lib_blueprint.route('/getAnalysisDetails', methods=['GET','POST'])
def get_analysis_details():
    disaster_data=db.session.execute(db.Select(DisasterAnalysis)).scalars().all()
    dis_serialized = [dis.to_dict() for dis in disaster_data]
    
    # print(dis_serialized)
    return jsonify({
        'section_info':dis_serialized
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

def send_activity_report():
    # Step 1: Fetch data from DisasterAnalysis table
    disaster_data = DisasterAnalysis.query.all()
    disaster_records = [record.to_dict() for record in disaster_data]
    
    # Step 2: Generate PDF
    pdf_path = generate_pdf(disaster_records)
    
    # Step 3: Send the PDF via email
    recipient_email = "anirudhpabbaraju1103@gmail.com"  # Replace with actual recipient email
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
    
    

        
        
@lib_blueprint.route("/generate_report",methods=['GET','POST'])
def generate_report():
   
        # Trigger the Celery task
        
    job=send_activity_report()
    
    
    
    # Return the task ID to the client
    return jsonify({
        'status': 'Done',
    }), 200
        
        

