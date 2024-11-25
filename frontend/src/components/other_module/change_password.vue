<template>
    <div class="abc">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      <div class="main">
         
         <h1>CHANGE PASSWORD PAGE</h1>
         <h2>{{message}}</h2>

         <div class="row">
          <form @submit.prevent="changePassword">
            <div class="mb-11 password-container">
              <label for="exampleEmail" class="form-label"><p class="x">Email</p></label>
              <div class="input-group">
                <input type="email" class="form-control" id="email" v-model="email">
              </div>
            </div>
            <div class="mb-11 password-container">
              <label for="exampleInputPassword1" class="form-label"><p class="x">Old Password</p></label>
              <div class="input-group">
                <input type="password" class="form-control" id="exampleInputPassword1" v-model="old_password">
                <span class="input-group-text" id="togglePassword"><i class="fas fa-eye"></i></span>
              </div>
              <div>
                <a href="/forgot_password">
                  <button :class="['btn', isDarkMode ? 'btn-dark' : 'btn-outline-primary', 'p-6', 'lh-1']">Forgot Password</button>
                </a>
              </div>
            </div>
            <div class="mb-11 password-container">
              <label for="exampleInputPassword2" class="form-label"><p class="x">New Password</p></label>
              <div class="input-group">
                <input type="password" class="form-control" id="exampleInputPassword2" v-model="new_password">
                <span class="input-group-text" id="togglePassword1"><i class="fas fa-eye"></i></span>
              </div>
            </div>
            <div class="mb-11 password-container">
              <label for="exampleInputPassword3" class="form-label"><p class="x">Confirm New Password</p></label>
              <div class="input-group">
                <input type="password" class="form-control" id="exampleInputPassword3" v-model="confirm_new">
                <span class="input-group-text" id="togglePassword2"><i class="fas fa-eye"></i></span>
              </div>
            </div>
            <button type="submit" class="btn btn-primary">Change Password</button>
          </form> 
        </div> 

        <div class="buttons">
          <div>
            <a href="/">
              <button :class="['btn', isDarkMode ? 'btn-dark' : 'btn-secondary', 'p-3', 'lh-1']">Home</button>
            </a>
          </div>
         
        </div>

      </div>
     
  
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import { useRouter } from 'vue-router';
  export default {
   name:'change_password',
   setup(){
    const router=useRouter();
    return {router};
   },
   data(){
    return {
      message:'Welcome to Change Password Page',
      id:'',
      email_error:"",
      isDarkMode: false,
      old_password:"",
      new_password:"",
      confirm_new:"",
      email:'',
      role:''
    }
   },
   async mounted() {
      const togglePassword = document.querySelector('#togglePassword');
      const password = document.querySelector('#exampleInputPassword1');
  
      togglePassword.addEventListener('click', function (e) {
        // Toggle the type attribute
        const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
        password.setAttribute('type', type);
        // Toggle the eye slash icon
        this.querySelector('i').classList.toggle('fa-eye-slash');
      });
      const togglePassword1 = document.querySelector('#togglePassword1');
      const password1 = document.querySelector('#exampleInputPassword2');
  
      togglePassword1.addEventListener('click', function (e) {
        // Toggle the type attribute
        const type = password1.getAttribute('type') === 'password' ? 'text' : 'password';
        password1.setAttribute('type', type);
        // Toggle the eye slash icon
        this.querySelector('i').classList.toggle('fa-eye-slash');
      });
      const togglePassword2 = document.querySelector('#togglePassword2');
      const password2 = document.querySelector('#exampleInputPassword3');
  
      togglePassword2.addEventListener('click', function (e) {
        // Toggle the type attribute
        const type = password2.getAttribute('type') === 'password' ? 'text' : 'password';
        password2.setAttribute('type', type);
        // Toggle the eye slash icon
        this.querySelector('i').classList.toggle('fa-eye-slash');
      });

      this.email=JSON.parse(localStorage.getItem("info")).email


    },
    methods: {
      toggleDarkMode() {
        this.isDarkMode = !this.isDarkMode;
      },
      async changePassword(){
        if(this.new_password==this.old_password){
          alert("Old Password and New Password can't be same");
          this.new_password=""
          this.confirm_new=""
        }
        if(this.new_password==this.confirm_new){
          const r=await axios.post("http://127.0.0.1:5000/api/change_password",
            JSON.stringify({
              'id':JSON.parse(localStorage.getItem("info")).id,
              'new_password':this.new_password,
              'old_password':this.old_password,
              'email':this.email,
              'role':JSON.parse(localStorage.getItem("info")).role
            }),
            {
              headers:{
                'Content-Type':'application/json'
              }
            }
          );

          if(r.status==200){
            this.id=JSON.parse(localStorage.getItem("info")).id
            this.role=JSON.parse(localStorage.getItem("info")).role
            alert('Password Successfully changed!');
            if(this.role=="user") this.$router.push(`/user_dashboard/${this.id}`)
            else this.$router.push({path:'/admin_dashboard'})
          }
          else if(r.status==201){
            alert('Your Password is Wrong enter correct one')
            this.old_password="";
            this.new_password="";
            this.confirm_new=""
          }
        }
        else{
          alert("Your new_password and confirm aren't same")
          this.new_password="";
          this.confirm_new=""

        }
      }
    }
  }
  </script>
  
  <style scoped>
  .abc {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: url("../../assets/images/dmp_index.png") no-repeat center center/cover;
    color: var(--text-color, #333);
    transition: all 0.3s ease;
  }
  h1{
    color:white;
  }
  
  /* Typography */
  .title {
    font-size: 42px;
    font-weight: bold;
    text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
    margin-bottom: 20px;
    text-align: center;
  }
  button:hover{
    background-color:gold;
    color:blue;
  }
  
  /* Form */
  .row {
    background: ghostwhite;
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0 8px 15px yellow;
    width: 500px;
    max-width: 100%;
    transition: all 0.5s ease;
  }

  form{
    display: flex;
    flex-direction: column;
    gap:10px;
  }
  
  
  /* Glowing Inputs */
  .glowing-input {
    border: 2px solid #ddd;
    padding: 10px;
    border-radius: 8px;
    transition: all 0.3s ease;
  }
  
  .glowing-input:focus {
    box-shadow: 0 0 10px 2px var(--focus-glow-color, blue);
    border-color: var(--focus-glow-color, blue);
  }
  
  .dark .glowing-input:focus {
    --focus-glow-color: white; /* White glow in dark mode */
  }
  
  /* Buttons */
  .buttons {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 20px;
  }
  
  .action-btn,
  .login-btn {
    border-radius: 20px;
    padding: 10px 20px;
    font-size: 16px;
  }
  
  .action-btn:hover {
    background-color: #ffd700;
    color: black;
  }
  
  .login-btn:hover {
    transform: scale(1.05);
  }
  
  /* Password Toggle Icon */
  .toggle-icon {
    cursor: pointer;
  }
  
  .toggle-icon i {
    font-size: 18px;
    color: #555;
  }
  p{
    font-weight: bold;
    font-size:20px;
    color:black;
  }
  h2{
    color:white;
    font-size:15px;
  }
  
  .password-container{
    display: flex;
    flex-direction: column;
    gap:10px;
  }
  
  .password-container .input-group .input-group-text {
    cursor: pointer;
    background-color: var(--input-bg-color);
    color: var(--input-text-color);
  }
  </style>
  