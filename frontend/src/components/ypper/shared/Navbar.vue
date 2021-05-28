<template>
  <div class="navbar-container">
    <div class="nav-item home">
      <p class="link" @click="navigate('home')">Home</p>
    </div>
    <div class="nav-item contact">
      <p class="link" @click="navigate('contact')">Contact</p>
    </div>
    <div class="nav-item projects">
      <p class="link" @click="navigate('projects')">Projects</p>
    </div>
    <!-- <div class="nav-item home">
      <router-link :to="{ name: 'home' }" class="link">Home</router-link>
    </div>
    <div class="nav-item contact">
      <router-link :to="{ name: 'contact' }" class="link">Contact</router-link>
    </div>
    <div class="nav-item projects">
      <router-link :to="{ name: 'projects' }" class="link"
        >Projects</router-link
      >
    </div> -->
    <!-- <div class="nav-item blog">
      <router-link :to="{ name: 'blog' }" class="link">Blog</router-link>
    </div> -->
  </div>
</template>

<script>
import stateNavigation from "@/modules/ypperNavigation";
import { onMounted } from 'vue'
export default {
  setup() {
    const { setNav } = stateNavigation;

    onMounted(() => {
      navigate('home')
    })

    function navigate(nav) {
      setNav(nav);
    }

    return {
      setNav,
      navigate,
    };
  },
};
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
  padding: 0 10px 0 10px;
  cursor: pointer;
  border-radius: 15px;
}
.nav-item:hover {
  background-color: #1c3334;
}
.link {
  text-decoration: none;
  color: #4c9192;
  font-weight: bold;
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