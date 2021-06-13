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
import { reactive, ref } from "vue";
import axios from "axios";
import stateUser from "@/modules/user";
export default {
  setup() {
    const { setUser } = stateUser;
    const form = reactive({
      email: "",
      password: "",
    });

    const auth_error = ref(false);

    function login() {
      if (!form.email || !form.password) {
        auth_error.value = true;
      } else {
        const request_login = {
          email: form.email,
          password: form.password,
        };
        axios
          .post(process.env.VUE_APP_API_URL + "login", request_login, {
            withCredentials: true,
          })
          .then((response) => {
            if (response.data.login) {
              setUser(
                response.data.first_name,
                response.data.last_name,
                response.data.email,
                response.data.phone,
                false,
                response.data.login
              );
            }
            window.location = '/profile'
          })
          .catch((error) => {
            if (error.response.status == 401) {
              auth_error.value = true;
            }
          });
      }
    }

    return {
      form,
      auth_error,
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
.input-email::placeholder {
  font-size: 1vw;
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
.input-password::placeholder {
  font-size: 1vw;
  font-family: "Ubuntu", sans-serif;
}
.error {
  grid-row: 2;
  grid-column: 2 / 12;
  color: rgb(223, 0, 0);
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
.login-button {
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