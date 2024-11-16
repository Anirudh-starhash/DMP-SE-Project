<template>
    <div class="main-class">
      <!-- Include Bootstrap CSS -->
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    
      <div class="main_nav container-fluid">
        <nav class="navbar navbar-expand-lg navbar-light">
          <div class="container-fluid">
            <!-- Brand logo or name -->
            <a class="navbar-brand text-light me-5 co" href="#">Disaster Management System</a>
    
            <!-- Navbar toggle button for mobile -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
    
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <!-- Links on the left side -->
              <ul class="nvbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item me-3">
                  <a class="nav-link active text-light co" aria-current="page" href="#">Home</a>
                </li>
              </ul>
    
              <!-- Buttons on the right side -->
              <div class="navig">
                <a href="/admin_page"><button class="btn btn-primary me-3 creative-btn">Admin</button></a>
                <a href="/login_page"><button class="btn btn-primary me-3 creative-btn">Login</button></a>
                <a href="/register_page"><button class="btn btn-secondary creative-btn">Register</button></a>
              </div>
            </div>
          </div>
        </nav>
      </div>
    
      <div class="center container">
        <div>
          <h1>DISASTER MANAGEMENT SYSTEM</h1>
        </div>
    
        <div class="intro">
          <div class="row1">
            <p><span>&#9733;</span> A disaster management system that connects people with authorities and NGOs</p>
            <p>Provides alert services, rescue coordination, and guidance during disasters</p>
            <p>Enables communication between users and emergency responders</p>
          </div>
          <div class="row1">
            <img src="../../assets/images/disaster_management.jpg" alt="disaster_management_system" style="max-width: 150%; height: 50%; object-fit: cover; border-radius: 5%;" class="center"/>
          </div>
        </div>
        <div class="developers">
            <h4>Developed by:</h4>
            <div class="dev-names">
              <p>Anirudh Pabbaraju (22CSB0A10)</p>
              <p>Sandilya Voleti (22CSB0A18)</p>
              <p>Pavan Kalyan (22CSB0A19)</p>
            </div>
        </div>
  
        <!-- Developer Names below row1 content -->
        
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "index_page",
  };
  </script>
  
  <style scoped>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  html, body {
    height: 100%;
  }
  
  .main-class {
    display: flex;
    flex-direction: column;
    height: 150vh; /* Full screen height */
    background-size: cover;
    background-image: url('../../assets/images/dmp_index.png');
    background-position: center;
    background-repeat: no-repeat;
    opacity: 1; /* Darkened opacity */
    color: white; /* Ensure text is visible over the background */
  }
  
  .main_nav {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80px;
    background-color: rgba(0, 0, 0, 0.7); /* Darker transparent navbar */
  }
  
  .navig {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    gap: 10px;
  }
  
  h1 {
    color: #f8f9fa;
    text-align: center;
    font-family: 'Arial', sans-serif;
    font-weight: bold;
    font-size: 45px;
    margin-top: 20px;
    text-shadow: 3px 3px 10px rgba(0, 123, 255, 0.8); /* Added text-shadow for brightness */
  }
  
  p, a {
    font-family: "Courier New", Courier, "Lucida Sans Typewriter", "Lucida Typewriter", monospace;
    font-size: 20px;
    color: #f8f9fa;
  }
  
  .co, p {
    color:darkblue;
    font-weight: bold;
    font-size: 25px;
  }
  
  .center {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  
  .row1 {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 500px;
    font-size: 30px; /* Increased font size */
    color: #333; /* Darker text color */
    margin: 20px 0;
  }
  
  .intro {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    gap: 60px;
    width: 100%;
    margin: 20px 0;
    flex-grow: 1;
  }
  
  .developers {
    display:flex;
    flex-direction: column;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: black;
  }
  
  .developers p {
    color: darkblue;
    font-weight: bold;
  }
  
  .dev-names {
    display: flex;
    flex-direction: columns;
    justify-content: space-evenly;
    gap: 40px;
  }
  
  .creative-btn {
    border-radius: 30px;
    font-size: 18px;
    padding: 12px 24px;
    text-transform: uppercase;
    transition: all 0.3s ease-in-out;
  }
  
  .creative-btn:hover {
    background-color: #007bff;
    transform: scale(1.1);
    box-shadow: 0px 5px 15px rgba(0, 123, 255, 0.6);
  }
  
  @media (max-width: 768px) {
    .intro {
      flex-direction: column;
    }
  
    .row1 {
      margin-bottom: 20px;
    }
  
    .dev-names {
      flex-direction: column; /* Stack developer names vertically on small screens */
      gap: 10px;
    }
  }
  </style>
  