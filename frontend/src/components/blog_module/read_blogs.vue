<template>
    <div class="blogs_body">
        <link href="https://fonts.googleapis.com/css2?family=Raleway" rel="stylesheet">
        <div class="wrapper">
            <div class="top">
                <div class="title">
                    <h1>My Blog</h1>
                    <button @click="back">Back</button>
                    <button @click="add_review">Submit A Review</button>
                    <button @click="read_review">Read All Reviews to this blog</button>
                </div>
            </div>
            <div class="content">
                <div class="card">
                    <h1>{{blog["blog_name"]}}</h1>
                    <h2>{{blog["blog_subtitle"]}}</h2>
                    <p>{{blog["blog_content"]}}</p>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
import { useRouter } from 'vue-router';
import axios from 'axios'

export default {
    name:'blogs_body',

    data(){
        return{
            blog:{},
            id:'',
            x_id:''
        }
    },

    setup(){
        const router=useRouter();
        return {router};
    },

    async mounted() {

      const access_token = localStorage.getItem("access_token")
      if (!access_token) {
        alert('You have to login first');
        this.$router.push("/");
      } 
      else {
        this.name_ = JSON.parse(localStorage.getItem('info')).name
        try {
          const r = await axios.post("http://127.0.0.1:5000/api/user_check_permission", null, {
            headers: {
              Authorization: `Bearer ${access_token}`
            }
          });
          if (r.status === 200) {
            const response=await axios.get(`http://127.0.0.1:5000/api/getInfoBlog/${this.$route.params.id}`,);
            if(response.status===200){
                this.blog=response.data.blog
            }
          } 
          else {
            localStorage.removeItem("access_token")
            localStorage.removeItem("info")
            localStorage.removeItem("book_id")
            localStorage.removeItem("section_id")
            this.$router.push("/unauthorized");
          }
        } 
        catch (error) {
          console.log(error);
        }
      }
    },
    methods:{
        back(){
            this.$router.go(-1);
        },
        add_review(){
            this.id=this.$route.params.id
            this.$router.push({path:`/create_review/${this.id}`});
        },
        read_review(){
            this.id=this.$route.params.id
            this.$router.push({path:`/read_review/${this.id}`});
        }
    }
    
}
</script>

<style scoped>
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
    .blogs_body{
        font-family: Arial, sans-serif;
        color: #333;
        display: flex;
        flex-direction: column;
        min-height: 100vh;
        background-color:#e2e8f0;
      }

      .title{
        display: flex;
        flex-direction: row;
        gap:20px;
      }
      button{
        width:150px;
        color:#020617;
        background-color: #fcd34d ;
        height:50px;
      }


</style>