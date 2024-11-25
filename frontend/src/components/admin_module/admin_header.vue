<template>
  <div>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <header class="header">
      <div class="content">
        <div class="left">
          <p class="nav-item dashboard" @click="home">Dashboard</p>
        </div>
        <div class="right">
          <p class="nav-item" v-if="showRequests" @click="requests">Requests</p>
          <p class="nav-item" v-if="showMonitor" @click="monitor">Monitor</p>
          <p class="nav-item" v-if="showStats" @click="stats">Stats</p>
          <p class="nav-item logout" @click="logout">Logout</p>
        </div>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  name: 'librarian_header',
  props: {
    showRequests: { type: Boolean, default: true },
    showStats: { type: Boolean, default: true },
    showMonitor: { type: Boolean, default: true },
    isDarkMode: { type: Boolean, default: false }
  },
  methods: {
    home() { this.$router.push("/admin_dashboard"); },
    logout() { this.$router.push({ path: '/logout_page' }); },
    requests() { this.$router.push("/request_page"); },
    stats() { this.$router.push("/admin_stats_page"); },
    monitor() { this.$router.push("/admin_monitor"); }
  }
};
</script>

<style scoped>
/* Header Styling */
.header {
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
