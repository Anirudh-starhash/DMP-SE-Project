<template>
  <div class="main-class">
    <!-- Include Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />

    <!-- Navbar -->
    <div class="main_nav container-fluid">
      <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container-fluid">
          <!-- Brand logo -->
          <a class="navbar-brand text-light brand" href="#">BLOB</a>

          <!-- Navbar toggle button -->
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>

          <!-- Links -->
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active text-light" aria-current="page" href="#">Home</a>
              </li>
            </ul>
            <div class="navig">
              <a href="/admin_page">
                <button class="btn btn-primary creative-btn">Admin</button>
              </a>
              <a href="/login_page">
                <button class="btn btn-primary creative-btn">Login</button>
              </a>
              <a href="/register_page">
                <button class="btn btn-secondary creative-btn">Register</button>
              </a>
            </div>
          </div>
        </div>
      </nav>
    </div>

    <!-- Header Section -->
    <div class="center container">
      <h1 class="fade-in">Blogs for Learning, Observing, and Building</h1>

      <!-- Intro Section -->
      <div class="intro">
        <div class="row1">
          <p><span>&#9733;</span> A platform to explore, write, and share unique blogs.</p>
          <p>Foster creativity and connect with a vibrant blogging community.</p>
          <p>Discover new perspectives and grow your voice through writing.</p>
        </div>
        <div class="row1">
          <img
            src="../../assets/images/blog_index.jpg"
            alt="Creative Blogging Workspace"
            class="workspace-image"
          />
        </div>
      </div>

      <!-- Developers Section -->
      <div class="developers">
        <h4>Developed by:</h4>
        <div class="dev-names">
          <p>Anirudh Pabbaraju (22CSB0A10)</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "index_page",
};
</script>

<style scoped>
/* General styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Times New Roman", serif;
}

/* Main container */
.main-class {
  display: flex;
  flex-direction: column;
  height: 150vh;
  position: relative;
  background: url('../../assets/images/dmp_index.png') no-repeat center center/cover;
  color: white;
}

/* Background overlay */
.main-class::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6); /* Dark overlay */
  z-index: 0;
}

.center {
  position: relative;
  z-index: 1; /* Bring content above the overlay */
}

/* Navbar */
.main_nav {
  background-color: rgba(0, 0, 0, 0.8);
}

.navbar-brand {
  font-size: 28px;
  font-weight: bold;
  text-shadow: 2px 2px 5px #007bff;
}

.nav-link:hover {
  color: #ffd700 !important;
  transition: color 0.3s ease-in-out;
}

/* Header */
h1 {
  font-size: 50px;
  margin-top: 20px;
  text-shadow: 3px 3px 10px rgba(0, 0, 0, 0.9); /* Strong shadow for contrast */
  animation: fadeIn 2s ease-in-out;
}

/* Intro Section */
.intro {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  gap: 40px;
  margin: 40px 0;
}

.row1 {
  flex: 1;
  font-size: 20px;
  color: #f2f2f2; /* Soft white text */
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.8); /* Text shadow for visibility */
}

.workspace-image {
  max-width: 80%;
  height: auto;
  border-radius: 10px;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.4);
  object-fit: cover;
}

/* Developers Section */
.developers h4 {
  margin-top: 20px;
  text-shadow: 1px 1px 3px #000;
}

.dev-names p {
  margin: 5px 0;
  font-size: 18px;
  color: #f9f9f9; /* Slightly brighter white */
  text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.7);
}

/* Buttons */
.creative-btn {
  border-radius: 30px;
  padding: 10px 20px;
  transition: all 0.3s ease-in-out;
}

.creative-btn:hover {
  transform: scale(1.1);
  background-color: #ffd700;
  color: black;
}

/* Animations */
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(-20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .intro {
    flex-direction: column;
    align-items: center;
  }

  .workspace-image {
    max-width: 90%;
  }
}
</style>

