<template>
  <div class="navbar-container">
    <div class="nav-item home" @click="navigate('home')">
      <p class="link">Home</p>
    </div>
    <div class="nav-item contact" @click="navigate('contact')">
      <p class="link">Contact</p>
    </div>
    <div class="nav-item projects" @click="navigate('projects')">
      <p class="link">Projects</p>
    </div>
  </div>
</template>

<script>
import stateNavigation from "@/modules/ypperNavigation";
import { onMounted } from "vue";
export default {
  setup() {
    const { setNav } = stateNavigation;

    onMounted(() => {
      navigate("home");
    });

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
  user-select: none; 
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
@media (min-width: 600px) {
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
    user-select: none; 
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
}
</style>