<template>
  <div class="app-container">
    <div class="logo">
      <router-link :to="{name:'home'}" class="link">
        <h1>Ypper.se</h1>
      </router-link>
    </div>
    <div class="navbar">
      <Navbar />
    </div>
    <div class="content">
      <router-view></router-view>
    </div>
    <div class="footer">
      <p>Copyright Ypper</p>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/ypper/shared/Navbar";
export default {
  name: "App",
  components: {
    Navbar,
  },
};
</script>

<style>
#app {
  font-family: "Ubuntu", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100%;
}
.app-container {
  display: grid;
  min-height: 98vh;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto 1fr auto;
  background-color: #2f4454;
  color: aliceblue;
}
.logo {
  margin-top: 20px;
  cursor: pointer;
  grid-row: 1;
  grid-column: 2 / 5;
  text-decoration: none;
}
.logo .link{
  text-decoration: none;
}
.logo h1 {
  margin: 0;
  color: #baf5f8;
}
.navbar {
  margin-top: 20px;
  grid-column: 5 / 12;
  grid-row: 1;
  justify-items: center;
  align-items: center;
}
.content {
  margin-top: 30px;
  grid-column: 2 / 12;
  grid-row: 2;
  overflow: auto;
}
.footer {
  grid-column: 1 / 13;
  grid-row: 3;
  color: aliceblue;
}
</style>
