<template>
  <div class="app-container">
    <div class="ypper" v-if="site == 'ypper'">
      <div class="logo-ypper">
        <router-link :to="{ name: 'home' }" class="link">
          <h1>Ypper.se</h1>
        </router-link>
      </div>
      <div class="navbar-ypper">
        <Navbar />
      </div>
      <div class="content">
        <router-view></router-view>
      </div>
      <div class="footer">
        <p>Copyright Ypper</p>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "@/components/ypper/shared/Navbar";
import stateSite from "@/modules/site";
import stateUser from '@/modules/user'
export default {
  name: "App",
  components: {
    Navbar,
  },
  setup() {
    const { getSite } = stateSite;
    const site = getSite();
    const { getUser } = stateUser
    const user = getUser()

    return {
      getSite,
      site,
      getUser,
      user
    };
  },
};
</script>

<style>
#app {
  font-family: "Ubuntu", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* color: #2c3e50; */
  width: 100%;
  height: 100%;
}
.app-container {
  display: grid;
  min-height: 100vh;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto 1fr auto;
}
.ypper {
  grid-column: 1 / 13;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto 1fr auto;
  background-color: #2f4454;
  color: aliceblue;
  min-height: 100vh;
}
.logo-ypper {
  margin-top: 20px;
  cursor: pointer;
  grid-row: 1;
  grid-column: 2 / 5;
  text-decoration: none;
}
.logo-ypper .link {
  text-decoration: none;
}
.logo-ypper h1 {
  margin: 0;
  color: #baf5f8;
}
.navbar-ypper {
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
  color: #a9a9a9;
}
</style>
