<template>
    <div :class="[isDarkMode?'dark':'main-class']">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  
         <!-- header-->
          <librarian_header :showRequests="false"  :isDarkMode="isDarkMode" @toggleDarkMode="toggleDarkMode" />
  
  
        <div class="main-content">
          <div id="display"></div>
          <h2 :class="[isDarkMode?'h2dark':'h2light']">{{request_status}}</h2>
          <table>
            <thead>
              <tr>
                <th scope="col" class="text-bold" style="text-align:center" >User Id</th>
                <th scope="col" class="text-bold" style="text-align:center" >User Email</th>
                <th scope="col" class="text-bold" style="text-align:center" >Name</th>
                <th scope="col" class="text-bold" style="text-align:center" >Requested On</th>
                <th scope="col" class="text-bold" style="text-align:center"  >Action</th>
              </tr>
            </thead>
            <tbody>
                <tr v-for="user in requested_users.slice().reverse()" :key="user.user_id">
                    <td scope="col"><p>{{user.user_id}}</p></td>
                    <td scope="col"><p>{{user.user_email}}</p></td>
                    <td scope="col"><p>{{user.user_name}}</p></td>
                    <td scope="col"><p  class="x3">{{user.request_date}}</p></td>
                    <td scope="col" colspace=2>
                        <div class="buttons">
                            <a @click="grant(user,user.user_id)">
                              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-view-stacked x1 blue" viewBox="0 0 16 16">
                                <path d="M3 0h10a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2m0 1a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zm0 8h10a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2m0 1a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1z"/>
                              </svg>
                              <p class="x2">Grant</p>
                            </a>
                            <a @click="reject(user,user.user_id)">
                              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-return-left x1 red" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M14.5 1.5a.5.5 0 0 1 .5.5v4.8a2.5 2.5 0 0 1-2.5 2.5H2.707l3.347 3.346a.5.5 0 0 1-.708.708l-4.2-4.2a.5.5 0 0 1 0-.708l4-4a.5.5 0 1 1 .708.708L2.707 8.3H12.5A1.5 1.5 0 0 0 14 6.8V2a.5.5 0 0 1 .5-.5"/>
                              </svg>
                              <p class="x2">Reject</p>
                            </a>
                        </div>
                    </td>
                </tr>
            </tbody>
          </table>
          <h2 :class="[isDarkMode?'h2dark':'h2light']">{{grant_status}}</h2>
          <table>
            <thead>
              <tr>
                <th scope="col" class="text-bold" style="text-align:center" >User Id</th>
                <th scope="col" class="text-bold" style="text-align:center" >Email</th>
                <th scope="col" class="text-bold" style="text-align:center" >User Email</th>
                <th scope="col" class="text-bold" style="text-align:center" >Granted On</th>
                <th scope="col" class="text-bold" style="text-align:center"  >Action</th>
              </tr>
            </thead>
            <tbody>
                <tr v-for="user in granted_users.slice().reverse()" :key="user.user_id">
                    <td scope="col" ><p>{{user.user_id}}</p></td>
                    <td scope="col" ><p>{{user.user_email}}</p></td>
                    <td scope="col" ><p>{{user.user_name}}</p></td>
                    <td scope="col"><p  class="x3">{{user.issue_date}}</p></td>
                    <td scope="col"  colspace=1>
                        <div class="buttons">
                            <a @click="revoke(user.user_id)">
                              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-return-right x1 green" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M1.5 1.5A.5.5 0 0 0 1 2v4.8a2.5 2.5 0 0 0 2.5 2.5h9.793l-3.347 3.346a.5.5 0 0 0 .708.708l4.2-4.2a.5.5 0 0 0 0-.708l-4-4a.5.5 0 0 0-.708.708L13.293 8.3H3.5A1.5 1.5 0 0 1 2 6.8V2a.5.5 0 0 0-.5-.5"/>
                              </svg>
                              <p class="x2">Revoke User</p>
                            </a>
                        </div>
                    </td>
                </tr>
            </tbody>
          </table>
          <h2 :class="[isDarkMode?'h2dark':'h2light']">{{revoked_status}}</h2>
          <table>
            <thead>
              <tr>
                <th scope="col" class="text-bold" style="text-align:center" >User Id</th>
                <th scope="col" class="text-bold" style="text-align:center" >Email</th>
                <th scope="col" class="text-bold" style="text-align:center" >Name</th>
                <th scope="col" class="text-bold" style="text-align:center" >Revoked On</th>
                <th scope="col" class="text-bold" style="text-align:center" >Status</th>
              </tr>
            </thead>
            <tbody>
                <tr v-for="user in revoked_users.slice().reverse()" :key="user.user_id">
                    <td scope="col"><p>{{user.user_id}}</p></td>
                    <td scope="col"><p>{{user.user_email}}</p></td>
                    <td scope="col" ><p>{{user.user_name}}</p></td>
                    <td scope="col"><p class="x3">{{user.return_date}}</p></td>
                    <td scope="col"><p class="x3">{{user.status}}</p></td>
                </tr>
            </tbody>
          </table>
         
        </div>
  
        <!-- Footer -->
        <footer_page/>
  
        
       
    </div>
    
  
  </template>
  
  <script>
  import librarian_header from '../admin_module/admin_header.vue';
  import footer_page from './footer_page.vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router';
  export default {
     name: "request_page",
     data(){
      return{
        request_status:'Currently No Requests Received by users for privileged permission',
        grant_status:'Currently No Users Granted Privileged!',
        revoked_status:'Currently No Users Removed from privileged status',
        isDarkMode:false,
        requested_users:[],
        granted_users:[],
        revoked_users:[]
      }
     },
     setup(){
      const router=useRouter();
      return {router};
     },
     components:{
      librarian_header,
      footer_page
     }, 
     methods: {
      toggleDarkMode(isDark) {
        this.isDarkMode = isDark;
      },
      async grant(user,user_id){
        try{
          const r=await axios.post("http://127.0.0.1:5000/api/grantUser",
            JSON.stringify({
              'user_id':user_id,
            }),
            {
              headers:{
                'Content-Type':'application/json'
              }
            }
          );
  
          if(r.status===200){
            const userIndex = this.requested_users.indexOf(user);
            if (bookIndex !== -1) {
              this.requested_users.splice(userIndex, 1);
            }
            this.granted_users.push(user)
            // document.getElementById("display").innerHTML='<div class="alert alert-success" role="alert">\
            //     <strong>  Grant Successful </strong>\
            //     reload to see that update!</div>'
            // alert('Grant Successful reload to see that update!')
          }
          else{
            alert('Some Error!');
          }
        }
        catch(error){
          console.log(error)
        }
      },
      async reject(user,user_id){
        try{
          const r=await axios.post("http://127.0.0.1:5000/api/rejectUser",
            JSON.stringify({
              "user_id":user_id,
            }),
            {
              headers:{
                'Content-Type':'application/json'
              }
            }
          );
          if(r.status===200){
            const userIndex = this.requested_user.indexOf(user);
            if (userIndex !== -1) {
              this.requested_user.splice(userIndex, 1);
            }
            //  document.getElementById("display").innerHTML='<div class="alert alert-danger" role="alert">\
            //    <strong>  Reject Successful </strong>\
            //     reload to see that!</div>'
            // alert('');
          }
          else{
            alert('Some error!');
          }
        }
        catch(error){
          console.log(error)
        }
      },
      async revoke(user_id){
        localStorage.setItem("user_id",user_id);
        this.$router.push({name:"revokeUser",params:{id:user_id}});
      }
     },
     async mounted(){
      const access_token=localStorage.getItem("access_token")
      if(!access_token){
        alert('You need to login first to come here!')
        this.$router.push("/admin_page");
      }
      else{
          try{
          const r=await axios.post("http://127.0.0.1:5000/api/lib_check_permission",null,
            {
              headers:{
                Authorization:`Bearer ${access_token}`
              }
            }
          );
  
          if(r.status===200){
            const response=await axios.get(`http://127.0.0.1:5000/api/getAllRequests`);
            if(response.status===200){
              this.granted_users=response.data["issued_users"];
              this.requested_users=response.data["requested_users"];
              this.revoked_users=response.data["returned_users"];
              if(this.requested_users.length>0){
                this.request_status=`Total Number of requests sent are ${this.requested_users.length}`
              }
              if(this.revoked_users.length>0){
                this.revoked_status=`Total Number of users gave up privileged status are ${this.revoked_users.length}`
              }
              if(this.granted_users.length>0){
                this.grant_status=`Total Number of granted users  are ${this.granted_users.length}`
              }
            }
          }
          else{
            localStorage.removeItem("access_token");
            localStorage.removeItem("info");
            this.$router.push("/unauthorized")
          }
        }
        catch(error){
          console.log(error)
        }
      }
     
     }
  
  
  };
  </script> 
  
  
  <style scoped>
  
   .left,.right {
     float: left;
     width: 20%; /* The width is 20%, by default */
  } 
  .main {
    float: left;
    width: 60%; /* The width is 60%, by default */
  }
  
  /* Use a media query to add a breakpoint at 800px: */
   @media screen and (max-width: 800px) {
     .left,.main,.right {
         width: 100%; /* The width is 100%, when the viewport is 800px or smaller */
     } 
  }
  .main-class {
    display: flex;
    flex-direction: column;
   background-size: cover; 
   background-image: url('../../assets/images/dmp_index.png');
   background-repeat: no-repeat;
   min-height: 100vh;
  }
  
  .dark{
  display: flex;
    flex-direction: column;
   background-size: cover; 
   background-image: url('../../assets/images/section.jpg');
   background-repeat: no-repeat;
   min-height: 100vh;
  }
  .main-content{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    gap:40px;
    padding: 60px;
  }

body {
  font-family: 'Arial', sans-serif;
  background-color: #e8eaf6; /* Light violet background for the entire page */
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

table {
  width: 90%;
  border-collapse: collapse;
  background-color: rgba(255, 255, 255, 0.9); /* Slightly transparent white */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Soft shadow for depth */
  border-radius: 10px; /* Rounded corners */
  overflow: hidden; /* Ensures the border-radius applies */
  margin: 20px auto; /* Center the table */
}

th, td {
  padding: 12px 16px; /* Spacious padding for better readability */
  border: none; /* Removed default borders */
  text-align: center; /* Centered content for consistency */
  font-family: 'Arial', sans-serif; /* Clean and modern font */
}

th {
  background: linear-gradient(45deg, #6a1b9a, #7b1fa2); /* Gradient header */
  color: #fff; /* White text for contrast */
  text-transform: uppercase;
  letter-spacing: 1px; /* Slight spacing for a modern look */
  font-size: 16px; /* Larger font for headers */
  font-weight: bold;
}

tr:nth-child(even) {
  background-color: rgba(106, 27, 154, 0.1); /* Soft violet for alternating rows */
}

tr:hover {
  background-color: rgba(106, 27, 154, 0.2); /* Highlight on hover */
  transition: background-color 0.3s ease; /* Smooth hover effect */
}

td {
  font-size: 14px; /* Slightly smaller font for cell content */
  color: #4e4e4e; /* Neutral dark gray text */
}

p {
  color: #6a1b9a; /* Match text color to the violet theme */
  font-weight: bold;
}

.buttons a {
  display: flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  padding: 8px 12px;
  border-radius: 5px;
  background-color: #e1bee7; /* Light violet button background */
  color: #4a148c; /* Deep violet text for buttons */
  font-size: 14px;
  font-weight: 600;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.buttons a:hover {
  background-color: #ba68c8; /* Darker violet on hover */
  transform: scale(1.05); /* Subtle hover scaling */
}

.x1:hover {
  transform: translateX(5px); /* Smooth hover movement for icons */
}
h2{
  color:white;
}

  </style>