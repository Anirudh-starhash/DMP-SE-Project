<template>
    <div>
      <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
      <header class="d-flex flex-wrap justify-content-center py-3 mb-2 h">
        <div class="content">
          <div class="left">
            <p class="nav-item dashboard" @click="userdash">Dashboard</p>
          </div>
          <div class="right">
            <p class="nav-item" v-if="showOtherUsers" @click="otherusers">Other-Users-Page</p>
            <p class="nav-item" v-if="showMonitor" @click="monitor">Monitor</p>
            <p class="nav-item" v-if="showStats" @click="stats">Stats</p>
            <p class="nav-item" v-if="showRequests" @click="requests_form">Requests-Admin</p>
            <p class="nav-item" v-if="showStatus" @click="status">Privileged Status</p>
            <p class="nav-item logout" @click="logout">Logout</p>
          </div>
        </div>
      </header>
    </div>
</template>
<script>

  export default{
    name:'user_header',
    data(){
        return{
        }
    },
    props: {
        showStats: {
            type: Boolean,
            default: true
        },
        showStatus: {
            type: Boolean,
            default: false
        },
        showRequests: {
            type: Boolean,
            default: true
        },
        showProfile: {
            type: Boolean,
            default: true
        },
        showOtherUsers: {
            type: Boolean,
            default: true
        },
        isDarkMode: {
            type: Boolean,
            default: false
        }
        
    },
    methods: {
      toggleDarkMode() {
        this.$emit('toggleDarkMode', !this.isDarkMode);
      },
      userdash(){
        var userInfo = JSON.parse(localStorage.getItem('info'));
        var userId = userInfo.id;
        this.$router.push({name:'user_dashboard',params:{id:userId}});
      },
      stats(){
        var userInfo = JSON.parse(localStorage.getItem('info'));
        var userId = userInfo.id;
        this.$router.push({name:'user_stats_page',params:{id:userId}});
      },
      status(){
        var userInfo = JSON.parse(localStorage.getItem('info'));
        var userId = userInfo.id;
        this.$router.push({name:'user_status_page',params:{id:userId}});
      },
      otherusers(){
        var userInfo = JSON.parse(localStorage.getItem('info'));
        var userId = userInfo.id;
        this.$router.push({name:'other_users_page',params:{id:userId}});
      },
      requests_form(){
        var userInfo = JSON.parse(localStorage.getItem('info'));
        var userId = userInfo.id;
        this.$router.push({name:'user_request_page',params:{id:userId}});
      },
      logout(){
        var userInfo = JSON.parse(localStorage.getItem('info'));
        var userId = userInfo.id;
        this.$router.push({name:'user_logout_page',params:{id:userId}});
      },
      profile(){
        var userInfo = JSON.parse(localStorage.getItem('info'));
        var userId = userInfo.id;
        this.$router.push({name:'profile_page',params:{id:userId}});
      },
      
    }
  }

</script>
<style scoped>
header {
  height: 60px;
  background-color: #343a40;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Content Wrapper */
.content {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  max-width: 1200px; /* Optional: Limit the width for better aesthetics */
}

/* Left Section (Dashboard) */
.left {
  flex: 1;
  display: flex;
  align-items: center;
}

.dashboard {
  color: #ffc107;
  font-size: 20px;
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  cursor: pointer;
}

/* Right Section (Other Items) */
.right {
  display: flex;
  align-items: center;
  gap: 30px;
}

.nav-item {
  color: #ced4da;
  font-size: 20px;
  font-family: 'Poppins', sans-serif;
  font-weight: 500;
  cursor: pointer;
  transition: color 0.3s ease, transform 0.2s ease;
}

.nav-item:hover {
  color: #ffffff; /* Bright white on hover */
  transform: translateY(-2px);
}

/* Logout Styling */
.logout {
  color: #dc3545;
}

.logout:hover {
  color: #ff6b6b;
}

/* Media Query for Responsiveness */
@media (max-width: 768px) {
  .header {
    flex-direction: column;
    align-items: stretch;
    height: auto;
  }

  .content {
    flex-direction: column;
    align-items: stretch;
  }

  .right {
    justify-content: flex-end;
  }

  .nav-item {
    font-size: 14px;
    margin: 10px 0;
  }

  .dashboard {
    font-size: 18px;
  }
}
</style>