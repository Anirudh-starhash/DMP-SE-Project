<template>
  <footer class="footer bg-light text-dark py-2">
    <div class="container d-flex justify-content-between align-items-center flex-wrap">
      <!-- Left Section -->
      <div class="footer-left">
        <p class="mb-0">&copy; 2024 Anirudh Pabbaraju</p>
      </div>

      <!-- Right Section -->
      <div class="footer-right d-flex gap-3">
        <a href="https://www.instagram.com/anirudhpabbaraju/?hl=en" class="footer-link">
          Instagram
        </a>
        <a href="https://x.com/home?lang=en" class="footer-link">
          Twitter
        </a>
        <a href="https://github.com/Anirudh-starhash/Anirudh-starhash/tree/main" class="footer-link">
          GitHub
        </a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "FooterPage",
};
</script>

<style scoped>
/* General Footer Styles */
.footer {
  background-color: #f8f9fa; /* Subtle light gray background */
  color: #343a40; /* Dark gray text for good contrast */
  font-size: 14px;
  border-top: 1px solid #dee2e6; /* Soft border for separation */
}

.footer-left {
  font-weight: 500; /* Slightly bold for emphasis */
}

.footer-right {
  display: flex;
  gap: 15px;
  font-size: 14px;
}

.footer-link {
  color: #007bff; /* Standard blue for links */
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-link:hover {
  color: #0056b3; /* Darker blue on hover */
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .footer-right {
    justify-content: center;
    margin-top: 10px;
  }
}
a,p{
  font-weight: bold;
}
</style>
