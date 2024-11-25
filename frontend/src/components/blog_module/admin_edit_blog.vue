<template>
    <div class="blogs">
        <link href="https://fonts.googleapis.com/css2?family=Raleway" rel="stylesheet">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
        <div class="wrapper">
            <div class="top">
                <div class="title"><h1>Edit The blog</h1></div>
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
                        <label for="floatingInput">Subtitle</label>
                      </div>
                      <div class="form-floating">
                        <textarea name=""  class="form-control" id="floatingInput" placeholder="name@example.com" cols="30" rows="10" v-model="body"></textarea>
                        <label for="floatingPassword">Content</label>
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
            admin_id:''
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
          const r = await axios.delete("http://127.0.0.1:5000/api/user_check_permission", null, {
            headers: {
              Authorization: `Bearer ${access_token}`
            }
          });
          if (r.status === 200) {
            const response=await axios.get(`http://127.0.0.1:5000/api/getInfoBlog/${this.$route.params.id}`);
            if(response.status==200){
                this.title=response.data.blog['blog_subtitle'];
                this.name=response.data.blog['blog_name'];
                this.body=response.data.blog['blog_content']

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
                const response=await axios.post(`http://127.0.0.1:5000/api/edit_blob/${this.$route.params.id}`,
                    JSON.stringify({
                    title:this.name,
                    subtitle:this.title,
                    body:this.body,
                    id: this.$route.params.id
                    }), {
                    headers:{
                        'Content-Type':'application/json'
                    }
                }

             
          );
          if(response.status==200){
            alert('Editted Successfully');
            this.admin_id=JSON.parse(localStorage.getItem("info")).id
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
    /* General Styling */
/* General Styling */
body {
  margin: 0; /* Remove default margin */
  padding: 0; /* Remove default padding */
  font-family: 'Raleway', sans-serif;
  color: #333;
  background: url('../../assets/images/dmp_index.png') no-repeat center center fixed;
  background-size: cover;
  backdrop-filter: blur(5px);
}
.blogs {
  margin: 0; /* Ensure no extra margin at the top of this container */
  padding: 0; /* Remove padding if any */
  background: url('../../assets/images/dmp_index.png') no-repeat center center fixed;
  background-size: cover;
  backdrop-filter: blur(5px);
}
/* Go Back Button */
p button {
  background-color: #fcd34d;
  color: black;
  font-weight: bold;
  padding: 10px 20px;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  transition: transform 0.3s ease, background-color 0.3s ease;
}

p button:hover {
  transform: translateX(10px);
  background-color: #ffe87d;
}
form button:hover {
  background: linear-gradient(to right, #43658b, #36454f);
  transform: scale(1.05);
}

/* Wrapper */
.wrapper {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    margin: 0 auto;
    width: 100%;
    min-height: 100vh;
    text-align: center;
    border-radius: 10px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    padding-top: 0; /* Remove top padding for the header */
}

/* Top Section */
.top {
    background: linear-gradient(to right, #4e89ae, #43658b);
    width: 100%;
    height: 180px;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    border-bottom: 5px solid #36454f;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
    position: sticky; /* Makes it stay at the top when scrolling */
    top: 0;
    z-index: 10; /* Ensures it stays above other elements */
}

.top .title h1 {
    font-size: 36px;
    font-weight: bold;
    color: #ffffff;
}

/* Form Styling */
form {
    display: flex;
    flex-direction: column;
    gap: 25px;
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    width: 100%;
    max-width: 600px;
    margin-top: 20px; /* Add some spacing from the header */
}

/* Other CSS remains unchanged */

form {
  display: flex;
  flex-direction: column;
  gap: 25px;
  background: rgba(255, 255, 255, 0.9); /* Slight transparency for a modern look */
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3); /* Deeper shadow for a lifted appearance */
  width: 100%;
  max-width: 800px; /* Increased width for better visibility */
  margin-top: 20px; /* Space from the header */
}

form .form-floating {
  position: relative;
}

form .form-floating input,
form .form-floating textarea {
  border: 2px solid #818cf8;
  border-radius: 12px; /* Smooth, modern edges */
  padding: 15px 20px;
  font-size: 18px; /* Larger font for readability */
  line-height: 1.5; /* Better spacing within the input */
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.8); /* Subtle background */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Light shadow for depth */
}

form .form-floating input:focus,
form .form-floating textarea:focus {
  border-color: #4e89ae;
  outline: none;
  box-shadow: 0 4px 10px rgba(78, 137, 174, 0.5); /* Highlighted shadow on focus */
}

form .form-floating textarea {
  min-height: 200px; /* Ensure a large textarea */
  max-height: 400px; /* Optional: limit max height for large content */
  resize: vertical; /* Allow users to adjust height if needed */
}

form .form-floating label {
  color: #6b7280;
  font-weight: bold;
  transition: color 0.3s ease, transform 0.3s ease;
}

form .form-floating input:focus + label,
form .form-floating textarea:focus + label {
  color: #4e89ae;
  transform: scale(0.95) translateY(-10px); /* Subtle animation on focus */
}

/* Submit Button */
form button {
  background: linear-gradient(to right, #4e89ae, #43658b);
  color: white;
  font-weight: bold;
  font-size: 20px;
  border: none;
  border-radius: 30px; /* Fully rounded button */
  padding: 15px 25px;
  cursor: pointer;
  transition: all 0.3s ease;
}

form button:hover {
  background: linear-gradient(to right, #43658b, #36454f);
  transform: scale(1.05); /* Slight hover effect */
}
/* Top Section */
.top {
  background: linear-gradient(to right, #4e89ae, #43658b);
  width: 100%;
  height: 140px; /* Reduced the height for a smaller header */
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  border-bottom: 5px solid #36454f;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  position: static; /* Make it not fixed */
  top: 0;
  z-index: 10; /* Ensures it stays above other elements if required */
}

.top .title h1 {
  font-size: 28px; /* Reduced font size */
  font-weight: bold;
  color: #ffffff;
  margin: 0;
}

/* Adjust for when fixed is preferred */
.top.sticky {
  position: sticky; /* Sticky, but won't overlap the form */
  top: 0;
  z-index: 10;
}

/* Wrapper adjustments for spacing */
.wrapper {
  margin-top: 10px; /* Add space between header and content */
}




/* Responsive Design */
@media screen and (max-width: 768px) {
    .wrapper {
        padding-top: 0; /* No padding for smaller screens */
    }

    form {
        width: 90%;
        margin-top: 15px; /* Adjust spacing for smaller screens */
    }

    .top .title h1 {
        font-size: 28px;
    }
      form {
        padding: 20px;
        width: 90%;
        margin-top: 15px;
    }

    form .form-floating input,
    form .form-floating textarea {
        font-size: 16px; /* Adjust for smaller screens */
    }

    form button {
        font-size: 18px;
    }
    .top {
        height: 100px; /* Smaller header for smaller screens */
    }

    .top .title h1 {
        font-size: 22px; /* Further reduced font size for small devices */
    }

    .wrapper {
        margin-top: 10px; /* Ensure spacing below header */
    }
}

p{
  color:white;
}
    

</style>