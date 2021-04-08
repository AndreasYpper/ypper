<template>
  <div class="projects-container">
    <div class="nav-item">
      <router-link :to="{ name: 'machine_news_home' }" class="link">
        <h1>Machine News</h1>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.nav-item {
  cursor: pointer;
  border-radius: 15px;
}
.nav-item:hover {
  background-color: #1c3334;
}
.link {
  padding: 10px;
  font-weight: bold;
  text-decoration: none;
  color: #4c9192;
}
</style>