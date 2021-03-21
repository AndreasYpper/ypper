<template>
  <div class="login-container">
    <div class="header">
      <h1>Sign in</h1>
    </div>
    <form class="login-form" @submit.prevent="login">
      <input
        class="input-email"
        v-model="form.email"
        type="text"
        placeholder="Email"
      />
      <span class="error" v-if="auth_error"
        >Wrong password or email address.</span
      >
      <input
        class="input-password"
        v-model="form.password"
        type="password"
        placeholder="Password"
      />
      <div class="button-group">
        <button type="submit" class="login-button">Sign in</button>
        <!-- <router-link :to="{name: 'ResetPassword'}" class="forgot-button">Glömt lösenord?</router-link> -->
      </div>
    </form>
  </div>
</template>

<script>
import { reactive } from "vue";
export default {
  setup() {
    const form = reactive({
      email: "",
      password: "",
    });

    function login() {
      console.log("Login");
    }

    return {
      form,
      login,
    };
  },
};
</script>

<style scoped>
.login-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.header {
  grid-column: 3 / 11;
  grid-row: 1;
  text-align: center;
}
.login-form {
  grid-column: 3 / 11;
  grid-row: 2;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.input-email {
  grid-column: 5 / 9;
  grid-row: 1;
  height: 2vw;
  border-radius: 5px;
  border: none;
  background-color: aliceblue;
  text-align: center;
  font-size: 1vw;
  margin: 5px;
}
.input-email:focus {
  outline: none;
}
.username-input::placeholder {
  font-size: 4vw;
  font-family: "Ubuntu", sans-serif;
}
.input-password {
  grid-column: 5 / 9;
  grid-row: 3;
  height: 2vw;
  border-radius: 5px;
  border: none;
  background-color: aliceblue;
  text-align: center;
  font-size: 1vw;
  margin: 5px;
}
.input-password:focus {
  outline: none;
}
.username-password::placeholder {
  font-size: 4vw;
  font-family: "Ubuntu", sans-serif;
}
.error {
  grid-row: 2;
  grid-column: 2 / 12;
  color: red;
  margin: 3px;
  font-size: 0.8vw;
  font-style: italic;
}
.button-group {
  grid-column: 5 / 9;
  grid-row: 4;
  margin: 5px;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.login-button{
  grid-row: 1;
  grid-column: 3 / 11;
  height: 2vw;
  font-family: "Ubuntu", sans-serif;
  font-size: 1vw;
  font-weight: 600;
  background-color: #1ffaa6;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  color: #2f4454;
}
</style>