<template>
  <div class="register-container">
    <div class="header">
      <h1>Register user</h1>
    </div>
    <form class="register-form" @submit.prevent="register">
      <div class="form-field">
        <input
          class="input-email"
          v-model="form.email"
          type="text"
          placeholder="Email"
        />
        <span class="error" v-if="errors.email">{{ errors.email }}</span>
      </div>
      <div class="form-field">
        <input
          class="input-first-name"
          v-model="form.first_name"
          type="text"
          placeholder="First Name"
        />
        <span class="error" v-if="errors.first_name">{{
          errors.first_name
        }}</span>
      </div>
      <div class="form-field">
        <input
          class="input-last-name"
          v-model="form.last_name"
          type="text"
          placeholder="Last Name"
        />
        <span class="error" v-if="errors.last_name">{{
          errors.last_name
        }}</span>
      </div>
      <div class="form-field">
        <input
          class="input-phone"
          v-model="form.phone"
          type="text"
          placeholder="Phone"
        />
        <span class="error" v-if="errors.phone">{{ errors.phone }}</span>
      </div>
      <div class="form-field">
        <input
          class="input-password"
          v-model="form.password"
          type="password"
          placeholder="Password"
        />
        <span class="error" v-if="errors.password">{{ errors.password }}</span>
      </div>
      <div class="form-field">
        <input
          class="input-confirmation-password"
          v-model="form.confirmation_password"
          type="password"
          placeholder="Confirm Password"
        />
        <span class="error" v-if="errors.confirmation_password">{{
          errors.confirmation_password
        }}</span>
      </div>
      <div class="button-group">
        <button type="submit" class="register-button">Register</button>
        <!-- <router-link :to="{name: 'ResetPassword'}" class="forgot-button">Glömt lösenord?</router-link> -->
      </div>
    </form>
  </div>
</template>

<script>
import { reactive, getCurrentInstance } from "vue";
import axios from "axios";
export default {
  setup() {
    const instance = getCurrentInstance();

    const form = reactive({
      email: "",
      first_name: "",
      last_name: "",
      phone: "",
      password: "",
      confirmation_password: "",
    });

    const errors = reactive({
      email: "",
      first_name: "",
      last_name: "",
      phone: "",
      password: "",
      confirmation_password: "",
    });

    const register_user = reactive({
      first_name: "",
      last_name: "",
      email: "",
      phone: "",
      password: "",
    });

    function validateEmail() {
      var at = form.email.indexOf("@");
      var dot = form.email.lastIndexOf(".");
      if (
        form.email.length > 0 &&
        at > 0 &&
        dot > at + 1 &&
        dot < form.email.length &&
        form.email[at + 1] !== "." &&
        form.email.indexOf(" ") === -1 &&
        form.email.indexOf("..") === -1
      ) {
        errors.email = "";
        return true;
      } else {
        errors.email = "Not an valid email address.";
        return false;
      }
    }

    function validateFirstName() {
      if (form.first_name.length < 2) {
        errors.first_name = "First name requires atleast 2 characters.";
        return false;
      }
      errors.first_name = "";
      return true;
    }
    function validateLastName() {
      if (form.last_name.length < 2) {
        errors.last_name = "Last name requires atleast 2 characters.";
        return false;
      }
      errors.last_name = "";
      return true;
    }
    function validatePhone() {
      form.phone = form.phone.split(" ").join("");
      form.phone = form.phone.split("-").join("");
      if (form.phone.length < 9 || form.phone.length > 10) {
        errors.phone = "Should only be digits.";
        return false;
      } else if ([...form.phone].every((c) => "0123456789".includes(c))) {
        errors.phone = "";
        return true;
      } else {
        errors.phone = "Should only be digits.";
        return false;
      }
    }
    function validatePassword() {
      var strongRegex = new RegExp(
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,})"
      );
      if (strongRegex.test(form.password)) {
        errors.password = "";
        return true;
      } else {
        errors.password =
          "Must contain atleast one capital letter, one small letter, one digit and one special character. Password needs to be 8 characters long.";
        return false;
      }
    }
    function validateConfirmationPassword() {
      if (form.confirmation_password == form.password) {
        errors.confirmation_password = "";
        return true;
      } else {
        errors.confirmation_password = "Does not match.";
        return false;
      }
    }
    function register() {
      if (
        validateEmail() &&
        validateFirstName() &&
        validateLastName() &&
        validatePhone() &&
        validatePassword() &&
        validateConfirmationPassword()
      ) {
        register_user.first_name = form.first_name.trim();
        register_user.last_name = form.last_name.trim();
        register_user.email = form.email.trim().toLowerCase();
        register_user.password = form.password;
        if (form.phone.length === 10) {
          register_user.phone = "+46" + form.phone.slice(-9);
        } else if (form.phone.length === 9) {
          register_user.phone = "+46" + form.phone;
        }
        axios
          .post(process.env.VUE_APP_API_URL + "register", register_user)
          .then((response) => {
            if (response.data.registered) {
              instance.parent.setupState.register_show = false;
            }
          })
          .catch((error) => {
            if (error.response.status == 409) {
              errors.email = "Email address is already registered.";
            } else {
              alert(error.response);
            }
          });
      } else {
        validateEmail();
        validateFirstName();
        validateLastName();
        validatePhone();
        validatePassword();
        validateConfirmationPassword();
      }
    }
    return {
      form,
      register,
      validateEmail,
      validateFirstName,
      validateLastName,
      validatePhone,
      validatePassword,
      validateConfirmationPassword,
      errors,
    };
  },
};
</script>

<style scoped>
.register-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.header {
  grid-column: 3 / 11;
  grid-row: 1;
  text-align: center;
}
.register-form {
  grid-column: 3 / 11;
  grid-row: auto;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.form-field {
  grid-column: 1 / 13;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.form-field input {
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
.form-field input:focus {
  outline: none;
}
.form-field input::placeholder {
  font-size: 1vw;
  font-family: "Ubuntu", sans-serif;
}
.error {
  grid-row: 2;
  grid-column: 5 / 9;
  color: rgb(223, 0, 0);
  margin: 3px;
  font-size: 0.8vw;
  font-style: italic;
}
.button-group {
  grid-column: 5 / 9;
  grid-row: 7;
  margin: 5px;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.register-button {
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