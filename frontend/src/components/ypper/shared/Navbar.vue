<template>
  <div class="navbar-container">
    <div class="nav-item home">
      <router-link :to="{ name: 'home' }" class="link">Home</router-link>
    </div>
    <div class="nav-item contact">
      <router-link :to="{ name: 'contact' }" class="link">Contact</router-link>
    </div>
    <div class="nav-item projects">
      <router-link :to="{ name: 'projects' }" class="link">Projects</router-link>
    </div>
    <!-- <div class="nav-item blog">
      <router-link :to="{ name: 'blog' }" class="link">Blog</router-link>
    </div> -->
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.navbar-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  justify-items: center;
  align-items: center;
}
.nav-item {
    cursor: pointer;
    padding: 10px;
    border-radius: 15px;
    font-weight: bold;
}
.nav-item:hover{
    background-color: #1c3334;
}
.link {
    text-decoration: none;
    color: #4c9192;
}
.home {
  grid-column: 2 / 3;
}
.contact {
  grid-column: 4 / 5;
}
.projects {
  grid-column: 6 / 7;
}
.blog {
  grid-column: 9 / 10;
}
</style>