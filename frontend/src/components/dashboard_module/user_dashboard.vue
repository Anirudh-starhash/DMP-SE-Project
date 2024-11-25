<template>
    <div class="main-class">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"> 
     

        <user_header :isDarkMode="isDarkMode" @toggleDarkMode="toggleDarkMode"  :showRequests="computedShowRequests" :showStatus="computedStatRequests" />
        
        <h1 class="h1light">Hey {{ name_ }} <span v-if="status == 1">(Privileged)</span> </h1>
        <div class="y">
            <h3>If You want to Change Password -> &nbsp;</h3>
            <a href="/change_password">
              <button :class="['btn','btn-success', 'p-3', 'lh-1']">Change Password</button>
            </a>
        </div>
        <div class="container">
            <div class="left-content">
                <div class="main-content">
                    <div class="blogs">
                        <link href="https://fonts.googleapis.com/css2?family=Raleway&display=swap" rel="stylesheet">
                        <div class="wrapper">
                            <div class="top">
                                <div class="title"><h1>Blogs created by Admin</h1></div>
                            </div>
                            <div v-for="x in admin_blogs" :key="x.blog_id" class="content">
                                <div class="card">
                                    <!-- Display the blog name as the title -->
                                    <h2>{{ x.admin_blog_name }}</h2>
                                    
                                    <!-- Display the blog subtitle -->
                                    <p class="text">{{ x.admin_blog_subtitle }}</p>
                                    
                                    <!-- Link to the full blog post using blog_id -->
                                    <a :href="'/admin_blogs/' + x.admin_blog_id">Read</a>
                                </div>
                            </div>
                            
                            <div class="top">
                                <div class="title"><h1>Your Blogs</h1></div>
                            </div>
                            
                            <div v-for="x in my_blogs" :key="x.id" class="content">
                                <div class="card">
                                      <!-- Display the blog name as the title -->
                                      <h2>{{ x.blog_name }}</h2>
                                    
                                      <!-- Display the blog subtitle -->
                                      <p class="text">{{ x.blog_subtitle }}</p>
                                      
                                      <!-- Link to the full blog post using blog_id -->
                                       <div class="x345">
                                          <a :href="'/blogs/' + x.blog_id">Read</a>
                                          <a :href="'/edit_blog/' + x.blog_id">Edit</a>
                                          <a :href="'/delete_blog/' + x.blog_id">Delete</a>
                                       </div>
                                     
                                </div>
                            </div>
                            <div v-if="!my_blog_count" class="content">
                                <div class="card">
                                    <h2>No Blogs</h2>
                                </div>
                            </div>
                            <div class="button-wrapper">
                                <button @click="create_blog" :class="['btn','btn-success', 'p-3', 'lh-1']">Create Blog</button>
                            </div>
                           
                
                            
                        </div>
                    </div>
                   
                   
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
        status:''
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
            this.id =JSON.parse(localStorage.getItem("info")).id
            this.$router.push({path:`/send_alert_form/${this.id}`})

            if(r.status==200){
                alert('Alert Message sent Successful!');
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
                const response=await axios.get(`http://127.0.0.1:5000/api/getInfo/${this.$route.params.id}`);
                // console.log("Hello")
                if(response.status===200){
                  this.admin_blogs=response.data.blogs;
                  this.my_blogs=response.data.my_blogs;
                  this.my_blog_count=this.my_blogs.length;
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
    .y{
        display:flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
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
    .container-fluid {
        display: flex;
        justify-content: center;
        align-content: center;
        flex-direction: column;
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
        font-size:20px;
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
    .container {
        display: flex;
        
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
    .add:hover {
        transform: translate(2px);
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
        font-size:40px;
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
    .card p{
        font-size:20px;
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
        font-size:20px;
    }
   
    .blogs {
        font-family: Arial, sans-serif;
        color: #333;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        min-height: 100vh; /* Ensures the content takes up at least the full height of the viewport */
        background-color: gainsboro;
        text-align: center; /* Centers the text inside the blog items */
    }
    h2{
        font-weight:bold;
        font-size:20px;
        color:blue;
        font-family: 'Courier New', Courier, monospace;
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
    h3{
        color:white;
        font-size:16px;
    }
    span{
        color:white;
    }



</style >