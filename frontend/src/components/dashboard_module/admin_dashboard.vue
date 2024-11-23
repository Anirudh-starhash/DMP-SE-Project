<template>
    <div :class="[isDarkMode?'dark':'main-class']">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

         <!-- header-->
          <admin_header :showSections="false" :showLib="false" :isDarkMode="isDarkMode" @toggleDarkMode="toggleDarkMode" />
          <h1 :class="[isDarkMode ? 'h1dark' : 'h1light']" class="y">Hey Admin</h1>
          <div class="y">
            <a href="/change_password">
              <button :class="['btn', isDarkMode ? 'btn-dark' : 'btn-outline-primary', 'p-3', 'lh-1']">Change Password</button>
            </a>
          </div>

          <div class="container">
            <div class="left-content">
                <div class="main-content">
                    <div class="blogs">
                        <link href="https://fonts.googleapis.com/css2?family=Raleway" rel="stylesheet">
                        <div class="wrapper">
                            <div class="top">
                                <div class="title"><h1>Blogs created by You</h1></div>
                            </div>
                            <div v-for="x in admin_blogs" :key="x.admin_blog_id" class="content">
                                <div class="card">
                                    <!-- Display the blog name as the title -->
                                    <h2>{{ x.admin_blog_name }}</h2>
                                    
                                    <!-- Display the blog subtitle -->
                                    <p class="text">{{ x.admin_blog_subtitle }}</p>
                                    
                                    <!-- Link to the full blog post using blog_id -->
                                     <div class="x345">
                                      <a :href="'/admin_blogs/' + x.admin_blog_id">Read</a>
                                      <a :href="'/edit_admin_blogs/' + x.admin_blog_id">Edit</a>
                                      <a :href="'/delete_admin_blogs/' + x.admin_blog_id">Delete</a>
                                     </div>
                                   
                                </div>
                            </div>
                            
                            <div class="top">
                                <div class="title"><h1>User Blogs</h1></div>
                            </div>
                            
                            <div v-for="x in user_blogs" :key="x.id" class="content">
                                <div class="card">
                                      <!-- Display the blog name as the title -->
                                      <h2>{{ x.blog_name }}</h2>
                                    
                                      <!-- Display the blog subtitle -->
                                      <p class="text">{{ x.blog_subtitle }}</p>
                                      
                                      <!-- Link to the full blog post using blog_id -->
                                       <div class="x345">
                                          <a :href="'/blogs/' + x.blog_id">Read</a>
                                          <a :href="'/admin_edit_blog/' + x.blog_id">Edit</a>
                                          <a :href="'/admin_delete_blog/' + x.blog_id">Delete</a>
                                       </div>
                                     
                                </div>
                            </div>
                            <div v-if="!user_blog_count" class="content">
                                <div class="card">
                                    <h2>No Blogs</h2>
                                </div>
                            </div>
                            <div class="button-wrapper">
                                <button @click="create_blog" class="add">Create BLOGS</button>
                            </div>
                           
                
                            
                        </div>
                    </div>
                   
                   
                </div>
                   
            </div>
        </div>

        <!-- Footer -->
        <footer_page/>

        
       
    </div>
    
  
</template>

<script>
  import admin_header from '../admin_module/admin_header.vue';
  import footer_page from '../other_module/footer_page.vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router';
  export default {
     name: "librarian_dashboard",
     data(){
      return{
        admin_blogs:[],
        user_blogs:[],
        user_blog_count:0,
        isDarkMode:false,
        id:'',
        name_:''
      }
     },
     components:{
      admin_header,
      footer_page
     }, 
     methods: {
      toggleDarkMode(isDark) {
      this.isDarkMode = isDark;
    },
    create_blog(){
            this.id =JSON.parse(localStorage.getItem("info")).id
            this.$router.push(`/create_admin_blog/${this.id}`)
        }
  },
  setup(){
    const router=useRouter();
    return {router};
  },
  async mounted(){
    this.name_=JSON.parse(localStorage.getItem("info")).name
    const access_token=localStorage.getItem("access_token");
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
         else{
          const response=await axios.get(`http://127.0.0.1:5000/api/getAllInfo`);
                // console.log("Hello")
                if(response.status===200){
                  this.admin_blogs=response.data.blogs;
                  this.user_blogs=response.data.user_blogs;
                  this.user_blog_count=this.user_blogs.length;
                }

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
  #add{ 
    width: 70px; 
    height: 70px; 
    padding: 10px 16px; 
    border-radius: 35px; 
    font-size: 30px; 
    text-align: center; 
} 
.y{
    display:flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
  #add:hover{
    transform: translate(2px);
    background-color: blue;
    color: white;
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
 .left-content {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center; /* Align items vertically centered */
  width:100%;
}
.main-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    gap: 40px;
    padding-bottom: 100px;
    padding-top: 10px;
    width:100%;
}
.add {
    margin-top: auto;
    width: 200px;
    height: 50px;
}
.x345{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap:30px;
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
body{
    background: #efeff3;
    margin: 0;
    font-family: 'Raleway', sans-serif;
    -webkit-font-smoothing: antialiased;
    color:#212121;
}
.wrapper{
    position: relative;
    clear:both;
    margin: 0 auto 75px auto;
    width: 100%;
    overflow: hidden;
}
.top{
    background: #4e89ae;
    height: 180px;
    border-top: 20px solid #43658b;
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

.content{
    margin: -80px auto 100px;
    padding-bottom: 20px;
}

.card{
    position: relative;
    background: #fff;
    padding:50px;
    width: 600px;
    margin: 20px auto 0 auto;
    box-shadow: 0 2px 4px rgba(100,100,100,.1);
}

.card h2 {
    font-size:21px;
    font-weight:500;
}

.card h2 a {
    color:#CC0000;
    text-decoration:none;
}

.card .text {
    color:#212121;
    margin-top:20px;
    font-size:15px;
    line-height:22px;
}

footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #43658b;
    color: white;
    text-align: center;
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
</style>