<template>
    <div :class="[isDarkMode?'dark':'main-class']">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <librarian_header :showMonitor="false" :showLib="false" :isDarkMode="isDarkMode" @toggleDarkMode="toggleDarkMode" />
        <div class="main-content">
          <h2 :class="[isDarkMode?'h2dark':'h2light']">Do you really want to Delete the blob?</h2>
          <div class="buttons">
            <button @click="delete_" class="btn btn-success a">Yes</button>
            <button @click="back" class="btn btn-danger a">No</button>
           </div>
        </div>
        <footer_page/>
       
    </div>
  
  </template>
  
  <script>
  import axios from 'axios'
  import { useRouter } from 'vue-router';
  import librarian_header from '../admin_module/admin_header.vue' 
  import footer_page from '../other_module/footer_page.vue'
  export default {
     name: "user_logout_page",
     setup(){
        const router=useRouter();
        return {router}
     },
     data(){
      return{
        request_status:'Currently No Requests Sent',
        stats_status:'Stats Page is up to date',
        issue_status:'No Books Issued Currently',
        return_status:'No Books to return Currently',
        isDarkMode:false,
        id:"",
      }
     },
     components:{
      librarian_header,
      footer_page
     },
     setup(){
      const router=useRouter();
      return {router};
     },
     methods: {
       toggleDarkMode(isDark) {
         this.isDarkMode = isDark;
       },
       back(){
           this.$router.go(-1);
        },
        async delete_(){
           const r=await axios.delete(`http://127.0.0.1:5000/api/delete_admin_blob/${this.$route.params.id}`);
           if(r.status==200){
               alert(r.data.msg);
               this.user_id=JSON.parse(localStorage.getItem("info")).id
               this.$router.push({ path:`/admin_dashboard`});
           }
        }
      },
      async mounted() {
        const access_token=localStorage.getItem("access_token")
        if(!access_token){ 
          alert('You need to login first to come here!')
          this.$router.push("/login_page");
        }
        else{
          this.id=JSON.parse(localStorage.getItem("info")).id;
          try{
            const r=await axios.post("http://127.0.0.1:5000/api/user_check_permission",null,
              {
                headers:{
                  Authorization:`Bearer ${access_token}`
                }
              }
            );
            if(r.status===200){}
            else{
              localStorage.removeItem("access_token")
              localStorage.removeItem("info")
              localStorage.removeItem("book_id")
              localStorage.removeItem("section_id")
              this.$router.push("/unauthorized");
            }
          }
          catch(error){
            console.log(error);
          }
        }
      }
  };
  </script> 
  
  
  <style scoped>
  .main-class {
    display: flex;
    flex-direction: column;
    background-image: url('../../assets/images/dmp_index.png'); /* Light mode background */
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    min-height: 100vh;
    color: #333;
    /* Ensure footer stays at the bottom */
    justify-content: space-between; /* This ensures that footer stays at the bottom */
  }
  
  /* Main Content Centering */
  .main-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding:250px;
    backdrop-filter: blur(6px); /* Adds a slight blur for the text to stand out */
    border-radius: 8px;
    flex-grow: 1; /* Allows the content to take up remaining space */
  }
  
  /* Heading Styling */
  .h2light {
    font-size: 26px;
    color: white;
    font-weight: bold;
    margin-bottom: auto;
    font-family: 'Poppins', sans-serif;
  }
  
  /* Buttons Styling */
  .buttons {
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 20px;
  }
  
  .btn {
    width: 120px;
    height: 40px;
    font-size: 16px;
    border-radius: 20px;
    font-weight: 600;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  
  .btn-success {
    background-color: #28a745;
    border: none;
    color: white;
  }
  
  .btn-success:hover {
    background-color: #218838;
    transform: scale(1.05);
  }
  
  .btn-danger {
    background-color: #dc3545;
    border: none;
    color: white;
  }
  
  .btn-danger:hover {
    background-color: #c82333;
    transform: scale(1.05);
  }
  
  /* Responsive Design */
  @media screen and (max-width: 800px) {
    .main-class, .dark {
      background-size: contain;
    }
  
    .h2light, .h2dark {
      font-size: 20px;
    }
  
    .btn {
      width: 100px;
      font-size: 14px;
    }
  }
  
  /* Footer Styling */
  footer_page {
    margin-top: auto; /* Pushes the footer to the bottom */
  }
  </style>