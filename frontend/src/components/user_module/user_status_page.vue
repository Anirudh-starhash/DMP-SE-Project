<template>
  <div :class="[isDarkMode ? 'dark' : 'main-class']">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />

    <!-- Fixed Header -->
    <div class="header-container">
      <user_header
        :isDarkMode="isDarkMode"
        @toggleDarkMode="toggleDarkMode"
        :showRequests="computedShowRequests"
        :showStatus="computedStatRequests"
      />
    </div>

    <h1 :class="[isDarkMode ? 'h1dark' : 'h1light']">
      Hey {{ name_ }} <span v-if="status == 1">(Privileged) &nbsp;</span>
      <button class="btn btn-success" @click="send1">
        Send Response
      </button>
    </h1>

    <!-- Content Area -->
    <div class="user-info-container">
      <!-- Display user name, email, and ID -->
      <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">
        Name: {{ this.user_info.user_name }}
      </h2>
      <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">
        Email: {{ this.user_info.user_email }}
      </h2>
      <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">
        User ID: {{ this.user_info.user_id }}
      </h2>

      <!-- Display privilege status if the user is privileged -->
      <div v-if="this.user_info.is_privileged">
        <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">
          You are privileged! You will be privileged till
          {{ this.user_info.due_date }}.
        </h2>
        <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">
          You got privileged on {{ this.user_info.doi }}.
        </h2>
      </div>

      <!-- Display a message if the user is not privileged -->
      <div v-else>
        <h2 :class="[isDarkMode ? 'h2dark' : 'h2light']">
          You are not privileged.
        </h2>
      </div>

      <!-- Buttons -->
      <div class="d-flex mt-3 x">
        <button @click="returnPrivilegeStatus" class="btn custom-btn">Return Privilege Status</button>
        <div @click="getreport" class="ml-3">
          <button class="btn custom-btn">Get Report</button>
        </div>
      </div>
    </div>

    <!-- Fixed Footer -->
    <div class="footer-container">
      <footer_page />
    </div>
  </div>
</template>

<script>
   import user_header from "../user_module/user_header.vue";
import footer_page from "../other_module/footer_page.vue";
import axios from "axios";
import { useRouter } from "vue-router";

export default {
  name: "user_dashboard",
  data() {
    return {
      name_: "",
      isDarkMode: false,
      time: "",
      admin_blogs: [],
      my_blogs: [],
      my_blog_count: 0,
      id: "",
      alertmessage: "",
      status: "",
      user_info: "",
    };
  },
  components: {
    user_header,
    footer_page,
  },
  methods: {
    toggleDarkMode(isDark) {
      this.isDarkMode = isDark;
    },
    async send1() {
      this.alertmessage = prompt("Enter the disaster name\n");
      this.id = JSON.parse(localStorage.getItem("info")).id;
      const r = await axios.post(
        `http://127.0.0.1:5000/api/sendAlert/${this.id}`,
        JSON.stringify({
          alertMsg: this.alertmessage,
        }),
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (r.status == 200) {
        alert("Alert Message sent Successful!");
      }
    },
    async returnPrivilegeStatus() {
      alert("Returning privilege status...");
      this.id = JSON.parse(localStorage.getItem("info")).id;
      const response = await axios.get(
        `http://127.0.0.1:5000/api/return_Status/${this.id}`
      );
      if (response.status === 200) {
        alert("Privilege status returned!");
        let info = JSON.parse(localStorage.getItem("info"));
        info.status = "0";
        localStorage.setItem("info", JSON.stringify(info));
        this.$router.push({ path: `/user_dashboard/${info.id}` });
      }
    },
    async getreport() {
      try {
        let info = JSON.parse(localStorage.getItem("info"));
        const r = await axios.get(
          `http://127.0.0.1:5000/api/generate_user_report/${info.id}`
        );
        if (r.status == 200) {
          alert(`Report Sent to Your Mail! Check it out.`);
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
  setup() {
    const router = useRouter();
    return { router };
  },
  async mounted() {
    const access_token = localStorage.getItem("access_token");
    if (!access_token) {
      alert("You have to login first");
      this.$router.push("/login_page");
    } else {
      this.name_ = JSON.parse(localStorage.getItem("info")).name;
      this.status = JSON.parse(localStorage.getItem("info")).status;
      try {
        const r = await axios.post(
          "http://127.0.0.1:5000/api/user_check_permission",
          null,
          {
            headers: {
              Authorization: `Bearer ${access_token}`,
            },
          }
        );
        if (r.status === 200) {
          const response = await axios.get(
            `http://127.0.0.1:5000/api/getUserInfo/${this.$route.params.id}`
          );
          if (response.status === 200) {
            this.user_info = response.data.user_info;
          }
        } else {
          localStorage.removeItem("access_token");
          localStorage.removeItem("info");
          this.$router.push("/unauthorized");
        }
      } catch (error) {
        console.log(error);
      }
    }
  },
};
</script>

<style scoped>
/* General Styles */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: violet;
}

.main-class,
.dark {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-image: url("../../assets/images/dmp_index.png");
  background-size: cover;
  background-repeat: no-repeat;
  min-height: 100vh;
  color: white;
}

.header-container {
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000;
  background: rgba(0, 0, 0, 0.8);
}
.x{
  display: flex;
  flex-direction: row;
  gap:20px;
}
.h1light {
  color: red;
  margin-top: 80px; /* To avoid overlap with the fixed header */
  font-size:20px;
}

.h1dark {
  color: red;
  margin-top: 80px; /* To avoid overlap with the fixed header */
}

/* Content Box with Shadow */
.user-info-container {
  background: white;
  padding: 20px;
  border-radius: 15px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  margin: 20px auto;
  width: 100%;
  max-width: 800px;
}

.h2light,.user-info-container{
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap:20px;
  font-size:20px;
  color:blue;
 }
.custom-btn {
  background-color: #6c63ff;
  color: white;
  transition: transform 0.3s, background-color 0.3s;
}

.custom-btn:hover {
  background-color: #5146d8;
  transform: scale(1.1);
}

/* Fixed Footer */
.footer-container {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background: rgba(0, 0, 0, 0.8);
  color: white;
  text-align: center;
  padding: 10px;
}

</style>

