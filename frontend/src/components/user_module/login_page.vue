<template>
  <div class="abc">
    <link
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
      rel="stylesheet"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />

    <div class="main">
      <h1 class="title">
        SIGN IN
      </h1>

      <div class="row">
        <form @submit.prevent="user_login">
          <div class="mb-4">
            <label for="exampleInputEmail1" class="form-label">
              <p class="label-text">Email Address</p>
            </label>
            <input
              type="email"
              class="form-control glowing-input"
              id="exampleInputEmail1"
              aria-describedby="emailHelp"
              v-model="email"
              required
            />
          </div>
          <div class="mb-4 password-container">
            <label for="exampleInputPassword1" class="form-label">
              <p class="label-text">Password</p>
            </label>
            <div class="input-group">
              <input
                type="password"
                class="form-control glowing-input"
                id="exampleInputPassword1"
                v-model="password"
              />
              <span class="input-group-text" id="togglePassword">
                <i class="fas fa-eye"></i>
              </span>
            </div>
          </div>
          <button type="submit" class="btn btn-primary login-btn">SIGN IN</button>
        </form>
      </div>

      <div class="buttons">
        <a href="/register_page">
          <button class="btn btn-secondary action-btn">SIGN UP</button>
        </a>
        <a href="/">
          <button class="btn btn-secondary action-btn">Home</button>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useRouter } from "vue-router";
export default {
  name: "login_page",
  data() {
    return {
      email: "",
      isDarkMode: true,
      password: "",
    };
  },
  mounted() {
    const togglePassword = document.querySelector("#togglePassword");
    const password = document.querySelector("#exampleInputPassword1");

    togglePassword.addEventListener("click", function () {
      const type = password.getAttribute("type") === "password" ? "text" : "password";
      password.setAttribute("type", type);
      this.querySelector("i").classList.toggle("fa-eye-slash");
    });
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  methods: {
    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode;
    },
    async user_login() {
      try {
        const response = await axios.post(
          "http://127.0.0.1:5000/api/user_login",
          JSON.stringify({
            email: this.email,
            password: this.password,
          }),
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );

        if (response.status === 200) {
          const access_token = response.data.access_token;
          const info = response.data.info;
          localStorage.setItem("access_token", access_token);
          localStorage.setItem("info", JSON.stringify(info));
          this.$router.push(`/user_dashboard/${info.id}`);
        } else if (response.status === 201) {
          alert("Redirecting to register Page");
          this.$router.push("/register_page");
        } else {
          alert("Password is wrong. Re-enter!");
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>

<style scoped>
/* Main Container */
.abc {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: url("../../assets/images/dmp_index.png") no-repeat center center/cover;
  color: var(--text-color, #333);
  transition: all 0.3s ease;
}

h1{
  color:white;
}


.title {
  font-size: 42px;
  font-weight: bold;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
  margin-bottom: 20px;
  text-align: center;
}

/* Form */
.row {
  background: ghostwhite;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 8px 15px yellow;
  width: 500px;
  max-width: 100%;
  transition: all 0.5s ease;
}


/* Glowing Inputs */
.glowing-input {
  border: 2px solid #ddd;
  padding: 10px;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.glowing-input:focus {
  box-shadow: 0 0 10px 2px var(--focus-glow-color, blue);
  border-color: var(--focus-glow-color, blue);
}

.dark .glowing-input:focus {
  --focus-glow-color: white; /* White glow in dark mode */
}



/* Buttons */
.buttons {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.action-btn,
.login-btn {
  border-radius: 20px;
  padding: 10px 20px;
  font-size: 16px;
}

.action-btn:hover {
  background-color: #ffd700;
  color: black;
}

.login-btn:hover {
  transform: scale(1.05);
}

/* Password Toggle Icon */
.toggle-icon {
  cursor: pointer;
}

.toggle-icon i {
  font-size: 18px;
  color: #555;
}
p{
  font-weight: bold;
  color:black;
}
</style>
