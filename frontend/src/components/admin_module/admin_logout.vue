<template>
    <div :class="[isDarkMode?'dark':'main-class']">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  
         <!-- header-->
         <librarian_header :showMonitor="false" :showLib="false" />
  
  
        <div class="main-content">
           <h2 :class="[isDarkMode?'h2dark':'h2light']">Do you really want to Logout?</h2>
           <div class="buttons">
            <button @click="logout" class="btn btn-success a">Yes</button>
            <button @click="back" class="btn btn-danger a">No</button>
           </div>
        </div>
  
        <!-- Footer -->
        <footer_page/>
  
        
       
    </div>
    
  
  </template>
  
  <script>
  import axios from 'axios'
  import { useRouter } from 'vue-router';
  import librarian_header from './admin_header.vue';
  import footer_page from '../other_module/footer_page.vue'
  export default {
     name: "logout_page",
     data(){
      return{
        request_status:'Currently No Requests Receive',
        stats_status:'Stats Page is up to date',
        monitor_status:'No Users to Monitor Currently',
        isDarkMode:false
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
        back(){
            this.$router.push("/admin_dashboard");
        },
        async logout(){
            const access_token=localStorage.getItem("access_token")
            try{
                const response=await axios.post("http://127.0.0.1:5000/api/admin_logout",null,
                    {
                        headers:{
                            Authorization:`Bearer ${access_token}`
                        }
                    }
                );
                if(response.status===200){
                    localStorage.removeItem("access_token");
                    localStorage.removeItem("info");
                    localStorage.removeItem("section_id")
                    localStorage.removeItem("book_id")
                    this.$router.push("/admin_page");
                }
                else{
                    alert('Some Error!')
                }
            }catch(error){
                console.log(error)
            }
        }

  },
  async mounted(){
    const access_token=localStorage.getItem("access_token")
    if(!access_token){
      alert('You need to login first to come here!')
      this.$router.push("/librarian_page");
    }
    else{
      try{
        const response=await axios.post("http://127.0.0.1:5000/api/lib_check_permission",null,
                    {
                        headers:{
                            Authorization:`Bearer ${access_token}`
                        }
                    }
         );
         if(response.status!==200){
            localStorage.removeItem("access_token");
            localStorage.removeItem("info");
            localStorage.removeItem("section_id")
            localStorage.removeItem("book_id")
            this.$router.push("/unauthorized");
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
/* Background Styling */
.main-class {
  display: flex;
  flex-direction: column;
  background-image: url('../../assets/images/dmp_index.png'); /* Light mode background */
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  min-height: 100vh;
  color: #333;
}

/* Main Content Centering */
.main-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  gap: 20px;
  padding: 60px;
  backdrop-filter: blur(6px); /* Adds a slight blur for the text to stand out */
  border-radius: 8px;
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
</style>
