<template>
  <div :class="['abc', { dark: isDarkMode }]">
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
        ADMIN SIGN IN
        <button @click="toggleDarkMode" class="btn btn-primary mt-3 toggle-btn">
          <i v-if="isDarkMode" class="fas fa-sun"></i>
          <i v-else class="fas fa-moon"></i>
        </button>
        <span class="toggle-text x11" v-if="isDarkMode"> &nbsp; &nbsp; Light Mode!</span>
        <span class="toggle-text x11" v-else> &nbsp; &nbsp; Dark Mode!</span>
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
          <button type="submit" class="btn btn-primary login-btn">ADMIN SIGN IN</button>
        </form>
      </div>

      <div class="buttons">
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
          "http://127.0.0.1:5000/api/admin_login",
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
          this.$router.push(`/admin_dashboard`);
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
  color: var(--text-color);
  transition: all 0.3s ease;
}

.dark {
  background: #2c2c2c;
  background-image: none;
}

/* Typography */
.title {
  font-size: 42px;
  font-weight: bold;
  color: var(--text-color);
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
}

/* Form */
.row {
  background: var(--form-bg-color, rgba(0, 0, 0, 0.6));
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  width: 450px;
  transition: all 0.3s ease;
}

.dark .row {
  background: rgba(0, 0, 0, 0.9);
  box-shadow: 0 0 25px rgba(255, 255, 0, 0.7); /* Yellow shadow in dark mode */
}

p,h1{
  color:white;
}
.dark p{
 
  color:white;
}
.dark h1{
  color:gainsboro;
}
.x11{
  font-size:10px;
}
/* Glowing inputs */
.glowing-input {
  border: 2px solid;
  padding: 10px;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.glowing-input:focus {
  box-shadow: 0 0 10px 2px var(--focus-glow-color);
  border-color: var(--focus-glow-color);
}

.dark .glowing-input:focus {
  --focus-glow-color: white; /* White glow in dark mode */
}

.glowing-input:focus {
  --focus-glow-color: blue; /* Blue glow in light mode */
}

/* Buttons */
.buttons {
  display: flex;
  justify-content: center;
  flex-direction: row;
  align-items: center;
  gap: 10px; /* Reduced gap between buttons */
  margin-top: 20px;
}

.action-btn,
.login-btn {
  border-radius: 20px;
  padding: 10px 30px;
  font-size: 18px;
}

.action-btn:hover {
  background-color: #ffd700;
  color: black;
}

.login-btn:hover {
  transform: scale(1.1);
}
</style>
