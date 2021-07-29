<template>
  <div class="auth-container">
    <transition name="login" appear>
      <div class="login" v-if="!register_show">
        <LoginForm />
        <button class="toggleButton" @click="toggleRegister">Register new user</button>
      </div>
    </transition>
    <transition name="register" appear>
      <div class="register" v-if="register_show">
        <RegisterForm />
        <button class="toggleButton" @click="toggleRegister">Already have an account?</button>
      </div>
    </transition>
  </div>
</template>

<script>
import LoginForm from "@/components/authentication/LoginForm";
import RegisterForm from "@/components/authentication/RegisterForm";
import { ref } from "vue";
export default {
  components: {
    LoginForm,
    RegisterForm,
  },
  setup() {
    const register_show = ref(false);

    function toggleRegister() {
      register_show.value = !register_show.value
    }

    return {
      register_show,
      toggleRegister
    };
  },
};
</script>

<style scoped>
.auth-container {
  overflow: hidden;
  display: grid;
  grid-template-rows: auto;
  grid-template-columns: repeat(12, 1fr);
}
.login {
  grid-row: 1;
  grid-column: 1 / 13;
}
.login-enter-from {
  opacity: 0;
  transform: translateX(-100px);
}
.login-enter-to {
  opacity: 1;
  transform: translateX(0);
}
.login-enter-active {
  transition: all 1s ease;
  transition-delay: 0.7s;
}
.login-leave-from {
  opacity: 1;
  transform: translateX(0);
}
.login-leave-to {
  opacity: 0;
  transform: translateX(100px);
}
.login-leave-active {
  transition: all 1s ease;
}
.register {
  grid-row: 1;
  grid-column: 1 / 13;
}
.register-enter-from {
  opacity: 0;
  transform: translateX(-100px);
}
.register-enter-to {
  opacity: 1;
  transform: translateX(0);
}
.register-enter-active {
  transition: all 1s ease;
  transition-delay: 0.7s;
}
.register-leave-from {
  opacity: 1;
  transform: translateX(0);
}
.register-leave-to {
  opacity: 0;
  transform: translateX(100px);
}
.register-leave-active {
  transition: all 1s ease;
}
.toggleButton {
  margin: 10px;
  border: none;
  font-family: "Ubuntu", sans-serif;
  background-color: #2f4454;
  color: aliceblue;
  font-size: 0.8vw;
  font-style: italic;
  outline: none;
  cursor: pointer;
}
</style>