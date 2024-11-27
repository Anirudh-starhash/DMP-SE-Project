<template>
    <div class="blogs_body">
        <link href="https://fonts.googleapis.com/css2?family=Raleway" rel="stylesheet">
        <div class="wrapper">
            <div class="top">
                <div class="title">
                    <h1>Admin's Blog</h1>
                    <button @click="back">Back</button>
                    <button v-if="ifyes" @click="add_review">Submit a Review</button>
                    <button v-if="ifyes2" @click="read_review">Read All Reviews To This Blog</button>
                </div>
            </div>
            <div class="content">
                <div class="card">
                    <h1>{{blog["admin_blog_name"]}}</h1>
                    <h2>{{blog["admin_blog_subtitle"]}}</h2>
                    <p>{{blog["admin_blog_content"]}}</p>
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
            const response=await axios.get(`http://127.0.0.1:5000/api/getAInfoBlog/${this.$route.params.id}`,);
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
            this.$router.push({path:'/admin_dashboard'})
        },
        add_review(){
            this.id=this.$route.params.id
            this.$router.push({path:`/create_admin_review/${this.id}`});
        },
        read_review(){
            this.id=this.$route.params.id
            this.$router.push({path:`/read_admin_review/${this.id}`});
        }
    },
    computed:{
        ifyes(){
            let role=JSON.parse(localStorage.getItem("info")).role
            if(role=="user") return 0;
            else return 1;
        },
        ifyes2(){
            let role=JSON.parse(localStorage.getItem("info")).role
            if(role=="user") return 0;
            else return 1;
        }
    }
}
</script>

<style scoped>
body {
    background: linear-gradient(to bottom, #e0eafc, #cfdef3); /* Subtle gradient background */
    margin: 0;
    font-family: 'Raleway', sans-serif;
    -webkit-font-smoothing: antialiased;
    color: #212121;
  }
  
  .wrapper {
    margin: 0 auto;
    width: 100%;
    overflow: hidden;
  }
  
  .top {
    background: linear-gradient(to right, #4e89ae, #43658b); /* Gradient for the header */
    height: 180px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow for depth */
  }
  
  .top .title {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 15px;
    text-align: center;
  }
  
  .title h1 {
    font-size: 36px;
    color: #fff;
    font-weight: bold;
  }
  
  .title button {
    background-color: #fcd34d;
    color: #020617;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 8px;
    cursor: pointer;
    transition: transform 0.2s ease, background-color 0.3s ease;
  }
  
  .title button:hover {
    background-color: #ffe87d;
    transform: scale(1.05); /* Slight pop effect */
  }
  
  .content {
    margin: -60px auto 50px;
    padding-bottom: 20px;
    display: flex;
    justify-content: center;
  }
  
  .card {
    background: #fff;
    padding: 40px;
    width: 80%;
    max-width: 800px;
    border-radius: 12px; /* Smooth, modern edges */
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    animation: fadeIn 0.5s ease; /* Add a fade-in effect */
  }
  
  .card h1 {
    font-size: 30px;
    font-weight: bold;
    color: #4e89ae;
    text-align: center;
    margin-bottom: 10px;
  }
  
  .card h2 {
    font-size: 24px;
    font-weight: 500;
    color: #43658b;
    text-align: center;
    margin-bottom: 20px;
  }
  
  .card p {
    color: #333;
    font-size: 18px;
    line-height: 1.6;
    text-align: justify;
  }
  
  footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #43658b;
    color: white;
    text-align: center;
    padding: 10px 0;
  }
  
  footer p {
    margin: 0;
    font-size: 14px;
  }
  
  /* Responsive Design */
  @media screen and (max-width: 768px) {
    .card {
      padding: 20px;
      width: 90%;
    }
  
    .title h1 {
      font-size: 28px;
    }
  
    .title button {
      padding: 8px 16px;
      font-size: 14px;
    }
  }
  
  /* Keyframes for fade-in effect */
  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(-20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }


</style>