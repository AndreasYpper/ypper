<template>
  <div class="app-container">
    <div class="logo">
      <h1>Ypper.se</h1>
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
import Navbar from "@/components/shared/Navbar";
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
  margin-top: 60px;
}
.app-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto 1fr auto;
  align-items: center;
  background-color: #2f4454;
  color: aliceblue;
}
.logo {
  cursor: pointer;
  grid-row: 1;
  grid-column: 2 / 5;
}
.logo h1 {
  margin: 0;
  color: #baf5f8;
}
.navbar {
  grid-column: 5 / 12;
  grid-row: 1;
  justify-items: center;
  align-items: center;
}
.content {
  grid-column: 2 / 12;
  grid-row: 2;
  overflow: auto;
}
.footer {
  grid-column: 1 / 13;
  grid-row: 3;
  color: #1c3334;
  background-color: #2e151b;
}
</style>
