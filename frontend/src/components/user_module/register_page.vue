<template>
  <div class="abc">
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
      </h1>
      <h2>{{ message }}</h2>

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
          <button class="btn btn-secondary action-btn">
            SIGN IN
          </button>
        </a>
        <a href="/">
          <button class="btn btn-secondary action-btn">
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
h2{
  color:white;
  font-size:12px;
}

</style>
