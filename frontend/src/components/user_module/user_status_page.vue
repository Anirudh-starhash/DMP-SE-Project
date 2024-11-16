<template>
  <div :class="[isDarkMode ? 'dark' : 'main-class']">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"> 
   

      <user_header :isDarkMode="isDarkMode" @toggleDarkMode="toggleDarkMode"  :showRequests="computedShowRequests" :showStatus="computedStatRequests" />
      
      <h1 :class="[isDarkMode ? 'h1dark' : 'h1light']">Hey {{ name_ }} <span v-if="status == 1">(Privileged)</span> <button @click="send1" class=" button-wrapper2 add">Send Response</button></h1>
      <div class="user-info-container">
        <!-- Display user name, email, and ID -->
        <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">Name: {{ this.user_info.user_name }}</h2>
        <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">Email: {{ this.user_info.user_email }}</h2>
        <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">User ID: {{ this.user_info.user_id }}</h2>
        
        <!-- Display privilege status if the user is privileged -->
        <div v-if="this.user_info.is_privileged">
          <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">
            You are privileged! You will be privileged till {{ this.user_info.due_date }}.
          </h2>
          <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">
            You got privileged on {{ this.user_info.doi }}.
          </h2>
        </div>
        
        <!-- Display a message if the user is not privileged -->
        <div v-else>
          <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">
            You are not privileged.
          </h2>
        </div>
    
        <!-- Button to return privilege status -->
        <div class="d-flex mt-3">
          <button @click="returnPrivilegeStatus" class="btn btn-primary">Return Privilege Status</button>
          <div @click="getreport">
            <button class="btn btn-primary">Get Report</button>
          </div>
        </div>
      
      </div>
      <footer_page />
  </div>
</template>

<script>
import user_header from '../user_module/user_header.vue' 
import footer_page from '../other_module/footer_page.vue'
import axios from 'axios'
import { useRouter } from 'vue-router';
export default {
   name: "user_dashboard",
   data(){
    return{
      name_: "",
      isDarkMode: false,
      time:"",
      admin_blogs:[],
      my_blogs:[],
      my_blog_count:0,
      id:'',
      alertmessage:'',
      status:'',
      user_info:''
    }
   },
   components: {
    user_header,
    footer_page
   },
   
   methods: {
     toggleDarkMode(isDark) {
      this.isDarkMode = isDark;
     },
     create_blog(){
          this.id =JSON.parse(localStorage.getItem("info")).id
          this.$router.push(`/create_blog/${this.id}`)
      },
      async send1(){
          this.alertmessage=prompt("Enter the disaster name\n");
          this.id =JSON.parse(localStorage.getItem("info")).id
          const r=await axios.post(`http://127.0.0.1:5000/api/sendAlert/${this.id}`,
                  JSON.stringify({
                    alertMsg:this.alertmessage
                  }), {
                  headers:{
                      'Content-Type':'application/json'
                  }
                  }
          );

          if(r.status==200){
              alert('Alert Message sent Successful!');
          }
      },
      async returnPrivilegeStatus() {
          // Simulating a return or check for privilege status, you can change this logic
          alert('Returning privilege status...');
          this.id=JSON.parse(localStorage.getItem("info")).id
          const response = await axios.get(`http://127.0.0.1:5000/api/return_Status/${this.id}`);
          if (response.status === 200) {
            alert('Privilege status returned!');
            let info = JSON.parse(localStorage.getItem("info"));

            // Modify the status property
            info.status = "0";

            // Save the updated object back to localStorage
            localStorage.setItem("info", JSON.stringify(info));
            this.$router.push({path:`/user_dashboard/${info.id}`})
          }
      },
      async getreport(){
        try{
          let info = JSON.parse(localStorage.getItem("info"));
          const r=await axios.get(`http://127.0.0.1:5000/api/generate_user_report/${info.id}`);
          if(r.status==200){
            alert(`Report Sent to Your Mail Check it out from admin check it out!`)
          }
        }
        catch(error){
          console.log(error);
        }
      }
   },
   setup() {
      const router = useRouter();
      return { router };
   },
   async mounted() {
      const access_token = localStorage.getItem("access_token")
      if (!access_token) {
        alert('You have to login first');
        this.$router.push("/login_page");
      } else {
        this.name_ = JSON.parse(localStorage.getItem('info')).name
        this.status=JSON.parse(localStorage.getItem('info')).status
        try {
          const r = await axios.post("http://127.0.0.1:5000/api/user_check_permission", null, {
            headers: {
              Authorization: `Bearer ${access_token}`
            }
          });
          if (r.status === 200) {
              const response=await axios.get(`http://127.0.0.1:5000/api/getUserInfo/${this.$route.params.id}`);
              // console.log("Hello")
              if(response.status===200){
               this.user_info=response.data.user_info
              }
          } else {
            localStorage.removeItem("access_token")
            localStorage.removeItem("info")
            this.$router.push("/unauthorized");
          }
        } catch (error) {
          console.log(error);
        }
      }
      
    },
   
    computed: {
          computedShowRequests() {
              return this.status === "1" ? false : true;
          },
          computedStatRequests() {
              return this.status === "0" ? false : true;
          },
          notSet(){
              return this.time === "";
          }
      }
};
</script> 

<style scoped>
  .x {
      color: #fed7aa;
  }
  .x1 {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }
  span{
    color:black;
  }
  .x:hover {
      background-color: transparent !important;
  }
  .left, .right {
      float: left;
      width: 20%; /* The width is 20%, by default */
  }
  .add {
      margin-top: auto;
  }
  .x345{
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      gap:30px;
  }
  .button-wrapper2{
      width:100px;
      font-size:20px;
  }
  #add { 
      width: 70px; 
      height: 70px; 
      padding: 10px 16px; 
      border-radius: 35px; 
      font-size: 30px; 
      text-align: center; 
  } 
  #add:hover {
      transform: translate(2px);
      background-color: blue;
      color: white;
  }
  .x {
      height: 40px;
      width: 100px;
  }
  .x:hover {
      transform: translate(2px);
      background-color: darkolivegreen;
      color: aliceblue;
  }
  .main {
      float: left;
      width: 60%; /* The width is 60%, by default */
  }
  /* Use a media query to add a breakpoint at 800px: */
  @media screen and (max-width: 800px) {
      .left, .main, .right {
          width: 100%; /* The width is 100%, when the viewport is 800px or smaller */
      } 
  }
  h1 {
      color: salmon;
      text-align: center;
      font-family: foglghten;
      font-weight: bold;
      font-size: 40px;
  }
  p {
      color: darkblue;
      font-family: foglghten;
      font-size: 25px;
  }
  .center {
      display: flex;
      flex-direction: row;
      gap: 20px;
  }
  .image {
      align-items: center;
  }
 
  .image {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 500px;
      margin-top: 150px;
  }
  .intro {
      display: flex;
      flex-direction: column;
      width: 70%;
  }
  .text {
      display: flex;
      flex-direction: column;
      align-items: center;
  }
  .row {
      font-size: 20px;
      color: blue;
      height: 100%;
      margin-top: 50px;
  }
  .main-class {
      display: flex;
      flex-direction: column;
      background-size: cover; 
      background-image: url('../../assets/images/dmp_index.png');
      background-repeat: no-repeat;
      min-height: 100vh;
  }
  .dark {
      display: flex;
      flex-direction: column;
      background-size: cover; 
      background-image: url('../../assets/images/section.jpg');
      background-repeat: no-repeat;
      min-height: 100vh;
  }
  .add {
      margin-top: auto;
      width: 200px;
      height: 50px;
  }
  .add:hover {
      transform: translate(2px);
  }
  .h2light {
      font-size: 22px;
      color: darkblue;
      font-weight: bold;
      margin-bottom: auto;
  }
  .h2dark {
      font-size: 22px;
      color: black;
      font-weight: bold;
      margin-bottom: auto;
  }
  .h1light {
      padding: 20px;
      font-size: 32px;
      color: red;
      font-weight: bold;
      margin-bottom: auto;
  }
  .h1dark {
      padding: 20px;
      font-size: 32px;
      color: darkblue;
      font-weight: bold;
      margin-bottom: auto;
  }
 
  h1, h2, p, a {
      font-family: "Courier New", Courier, "Lucida Sans Typewriter", "Lucida Typewriter", monospace; 
      font-size: 25px; 
      font-style: normal; 
      font-variant: normal; 
      font-weight: 700; 
      line-height: 26.4px;
  }
  .custom-select {
      width: 100%;
      max-width: 300px;
  }
  .co{
    width:300px;
  }
 
  
  .top .title {
      width: 700px;
      margin: 38px auto 0 auto; 
  }
  
  .title h1 {
      font-size:24px;
      color:#FFF;
      font-weight:500;
  }
 
 
  .text{
      font-weight:bold;
      font-family:'Courier New', Courier, monospace;
      font-size:30px;
  }
  h2{
      font-weight:bold;
      font-size:30px;
      color:blue;
      font-family: 'Courier New', Courier, monospace;
  }
  .blogs {
      font-family: Arial, sans-serif;
      color: #333;
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      min-height: 100vh; /* Ensures the content takes up at least the full height of the viewport */
      background-color: #e2e8f0;
      text-align: center; /* Centers the text inside the blog items */
  }

    button{
      width:200px;
      color:blue;
      font-weight:bold;
      background-color: #fcd34d ;
      height:50px;
    }

    .add{
      display: relative;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    .button-wrapper {
      display: flex;
      justify-content: center;
      width: 100%;
  }
  .add:hover{
      transform: translate(10px);
  }
  .main-class {
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    min-height: 100vh; /* Ensure the container takes full viewport height */
    background-size: cover;
    background-image: url('../../assets/images/dmp_index.png');
    background-repeat: no-repeat;
    flex-direction: column;
  }
  
  .dark {
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    min-height: 100vh; /* Ensure the container takes full viewport height */
    background-size: cover;
    background-image: url('../../assets/images/section.jpg');
    background-repeat: no-repeat;
    flex-direction: column;
  }
  
  .user-info-container {
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    background-color: #f0f8ff; /* Alice Blue */
    border: 1px solid #d1d1d1; /* Grey border */
    margin-top: 30px;
    width: 60%; /* Adjust width to fit content */
    max-width: 600px; /* Optional: Limit the max width */
    text-align: center; /* Center text inside the container */
  }
  
  .user-info-container h2 {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 20px;
    color: #333; /* Darker text for better contrast */
    margin: 10px 0;
    padding: 10px;
    border-bottom: 1px solid #e0e0e0; /* Subtle separation between h2s */
  }
  
  .user-info-container h2:hover {
    background-color: #e8f4f8; /* Light background on hover */
    color: #0077b6; /* Slightly darker blue text on hover */
    cursor: pointer;
  }
  
  footer_page {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #43658b;
    color: white;
    text-align: center;
  }




</style >