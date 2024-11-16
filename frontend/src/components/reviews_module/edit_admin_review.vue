<template>
    <div class="blogs">
        <link href="https://fonts.googleapis.com/css2?family=Raleway" rel="stylesheet">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
        <div class="wrapper">
            <div class="top">
                <div class="title"><h1>Edit The Review</h1></div>
            </div>
            <div class="abc">
                <main class="container">
                    <form @submit.prevent="edit_blog">
                  
                      <div class="form-floating">
                        <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com" fdprocessedid="mzryah" v-model="name">
                        <label for="floatingInput">Title</label>
                      </div>
                      <div class="form-floating">
                        <input type="text" class="form-control" id="floatingInput" placeholder="name@example.com" fdprocessedid="mzryah" v-model="title">
                        <label for="floatingInput">Rating</label>
                      </div>
                      <div class="form-floating">
                        <textarea name=""  class="form-control" id="floatingInput" placeholder="name@example.com" cols="30" rows="10" v-model="body"></textarea>
                        <label for="floatingPassword">Description</label>
                      </div>
                      <button class="btn btn-primary w-100 py-2" type="submit" fdprocessedid="e845cp">Edit</button>
            
                    </form>
                    <p>Don't Wanna Edit? &nbsp; &nbsp; &nbsp; &nbsp;<button @click="back" class="add"> Go Back </button></p>
                </main>
            </div>
          
           

            
        </div>
    </div>
    
</template>

<script>
import { useRouter } from 'vue-router';
import axios from 'axios'

export default {
    name:'blogs',

    data(){
        return{
            admin_blogs:[],
            my_blogs:[],
            id:'',
            name:'',
            title:'',
            body:'',
            user_id:''
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
        this.id = JSON.parse(localStorage.getItem('info')).id
        try {
          const r = await axios.post("http://127.0.0.1:5000/api/user_check_permission", null, {
            headers: {
              Authorization: `Bearer ${access_token}`
            }
          });
          if (r.status === 200) {
            const response=await axios.get(`http://127.0.0.1:5000/api/getAdminInfoReview/${this.$route.params.id}`);
            if(response.status==200){
                this.title=response.data.review['rating'];
                this.name=response.data.review['review_name'];
                this.body=response.data.review['description']

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
        async edit_blog(){
            try{
                this.id=JSON.parse(localStorage.getItem("info")).id
                const response=await axios.put(`http://127.0.0.1:5000/api/edit_admin_review/${this.$route.params.id}/${this.id}`,
                    JSON.stringify({
                    title:this.name,
                    rating:this.title,
                    description:this.body,
                    id: this.$route.params.id
                    }), {
                    headers:{
                        'Content-Type':'application/json'
                    }
                }

             
          );
          if(response.status==200){
            alert('Editted Successfully');
            this.user_id=JSON.parse(localStorage.getItem("info")).id
            this.$router.push({ path: `/admin_dashboard` });

          }
          else{
            alert(response.data.msg);
          }
            }
            catch(error){
                console.log(error);
            }
            
        }
    }
}
</script>

<style scoped>
    .abc {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: #0f172a;
        width: 100%;
        padding: 1.5rem;
        height: calc(100vh - 180px); /* Adjusted to account for the top header */
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
    .blogs{
        font-family: Arial, sans-serif;
        color: #333;
        display: flex;
        flex-direction: column;
        min-height: 100vh;
        background-color:#e2e8f0;
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
    .container{
        display:flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap:20px;
      }
      h1{
        color:#818cf8;
      }
      label{
        color:white;
      }
      .form-floating label{
        color:black;
        font-weight:bold;
      }
      form{
        display: flex;
        flex-direction: column;
        gap:20px;
        width:600px;
      }
      p{
        color:white;
      }
      
      .form-floating textarea {
        min-height: 200px;  /* Increase minimum height as needed */
        width: 100%;        /* Ensure it takes up full width */
        padding: 15px;
        resize: vertical;   /* Allow user to resize vertically if needed */
    }
    

</style>