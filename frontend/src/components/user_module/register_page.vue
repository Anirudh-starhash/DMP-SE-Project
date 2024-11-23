<template>
  <div v-bind:class="['abc', { dark: isDarkMode }, { 'dark-background': isDarkMode }]">
    <link
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
      rel="stylesheet"
    />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />

    <div class="main">
      <h1>
        SIGN UP
        <button @click="toggleDarkMode" class="btn btn-primary mt-3 toggle-btn">
          <i v-if="isDarkMode" class="fas fa-sun"></i>
          <i v-else class="fas fa-moon"></i>
        </button>
        <span class="toggle-text x11" v-if="isDarkMode"> &nbsp; &nbsp; Light Mode!</span>
        <span class="toggle-text x11" v-else> &nbsp; &nbsp; Dark Mode!</span>
      </h1>
      <p>{{ message }}</p>

      <div class="row">
        <form method="post" @submit.prevent="user_register">
          <div class="mb-4">
            <label for="exampleInputFirstName" class="form-label">
              <p class="label-text">Name</p>
            </label>
            <input
              type="text"
              class="form-control glowing-input"
              id="exampleInputFirstName"
              required
              v-model="name"
            />
          </div>

          <div class="mb-4">
            <label for="exampleInputEmail1" class="form-label">
              <p class="label-text">Email Address</p>
            </label>
            <input
              type="email"
              class="form-control glowing-input"
              id="exampleInputEmail1"
              required
              v-model="email"
            />
          </div>
          <div v-if="email_error" class="error-text">Email not properly formatted</div>

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

          <div class="mb-4 password-container">
            <label for="exampleInputPassword2" class="form-label">
              <p class="label-text">Confirm Password</p>
            </label>
            <div class="input-group">
              <input
                type="password"
                class="form-control glowing-input"
                id="exampleInputPassword2"
                v-model="confirm_password"
              />
              <span class="input-group-text" id="togglePassword1">
                <i class="fas fa-eye"></i>
              </span>
            </div>
          </div>

          <button type="submit" class="btn btn-primary register-btn">SIGN UP</button>
        </form>
      </div>

      <div class="buttons">
        <a href="/login_page">
          <button :class="['btn', isDarkMode ? 'btn-dark' : 'btn-primary', 'p-3', 'lh-1']">
            SIGN IN
          </button>
        </a>
        <a href="/">
          <button :class="['btn', isDarkMode ? 'btn-dark' : 'btn-primary', 'p-3', 'lh-1']">
            Home
          </button>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useRouter } from "vue-router";

export default {
  name: "register_page",
  data() {
    return {
      message: "Welcome to Sign Up Page",
      email: "",
      email_error: "",
      isDarkMode: true,
      password: "",
      name: "",
      confirm_password: "",
    };
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  mounted() {
    const togglePassword = document.querySelector("#togglePassword");
    const password = document.querySelector("#exampleInputPassword1");

    togglePassword.addEventListener("click", function () {
      const type = password.getAttribute("type") === "password" ? "text" : "password";
      password.setAttribute("type", type);
      this.querySelector("i").classList.toggle("fa-eye-slash");
    });

    const togglePassword1 = document.querySelector("#togglePassword1");
    const password1 = document.querySelector("#exampleInputPassword2");

    togglePassword1.addEventListener("click", function () {
      const type = password1.getAttribute("type") === "password" ? "text" : "password";
      password1.setAttribute("type", type);
      this.querySelector("i").classList.toggle("fa-eye-slash");
    });
  },
  methods: {
    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode;
    },
    async user_register() {
      try {
        if (this.confirm_password !== this.password) {
          alert("Password and Confirm Password didn't match");
          this.confirm_password = "";
          this.$router.push("/register_page");
        } else {
          const response = await axios.post(
            "http://127.0.0.1:5000/api/user_register",
            JSON.stringify({
              name: this.name,
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
            this.$router.push("/login_page");
          } else {
            alert("Redirecting to Login Page, already Registered!");
            this.$router.push("/login_page");
          }
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
  background-color: var(--bg-color);
  color: var(--text-color);
  transition: all 0.3s ease;
}

.dark {
  background: #2c2c2c;
  background-image: none;
}

/* Typography */
.row p{
  color:white;
}
.main>p{
  color:black;
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

.label-text {
  font-size: 18px;
  color: var(--text-color);
}

.dark .label-text {
  color: white;
}

.x {
  font-size: 18px;
}

/* Form Styling */
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

/* Glowing Inputs */
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
  --focus-glow-color: white;
}

.glowing-input:focus {
  --focus-glow-color: blue;
}

/* Buttons Styling */
.buttons {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.register-btn {
  border-radius: 20px;
  padding: 10px 30px;
  font-size: 18px;
}

.action-btn:hover {
  background-color: #ffd700;
  color: black;
}

.register-btn:hover {
  transform: scale(1.1);
}
</style>
